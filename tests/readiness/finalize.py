#!/usr/bin/env python3
"""Validate exact current/retained BDD evidence before owned-current cleanup."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import sys
import tempfile

runtime = json.loads(Path(sys.argv[1]).read_text())
evidence = Path(runtime['evidence']).resolve()
consumer = Path(runtime['consumerRoot'])
root = Path(runtime['root']).resolve()

def require(condition, reason):
    if not condition:
        raise SystemExit('Refusing cleanup: ' + reason)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

require(not consumer.is_symlink(), 'symlink consumer root')
consumer = consumer.resolve()
expected_owner = {'kind': 'readiness47-disposable-consumers', 'root': str(root), 'evidence': str(evidence)}
actual_owner = json.loads((consumer / '.readiness47-owned.json').read_text())
require(actual_owner == expected_owner and consumer.parent == Path(tempfile.gettempdir()).resolve() and consumer.name.startswith('cucumber-readiness47-consumers-') and not consumer.is_relative_to(root) and consumer.stat().st_uid == os.getuid(), 'disposable-root identity mismatch')
all_ids = [f'CR47-{number:03d}' for number in range(1, 11)]
repair = runtime.get('repair')
current_ids, retained_ids = all_ids, []
prior = None
if repair:
    current_ids = ['CR47-004','CR47-006','CR47-007','CR47-009','CR47-010']
    retained_ids = ['CR47-001','CR47-002','CR47-003','CR47-005','CR47-008']
    require(repair['kind'] == 'readiness47-b5-repair1' and repair['affectedIds'] == current_ids and repair['retainedIds'] == retained_ids, 'wrong repair boundary')
    prior = Path(repair['priorEvidence']).resolve()
    require(prior != evidence, 'repair overwrote original evidence')
    for name, expected in repair['priorArtifactHashes'].items():
        require(sha(prior/name) == expected, 'prior evidence changed: '+name)
    previous = json.loads((prior/'runtime.json').read_text())
    require(previous['sourceHashes'] == repair['priorSourceHashes'] and previous['contractDigest'] == runtime['contractDigest'] and Path(previous['root']).resolve() == root, 'prior source/contract identity differs')
    changed = sorted(name for name in set(previous['sourceHashes']) | set(runtime['sourceHashes']) if previous['sourceHashes'].get(name) != runtime['sourceHashes'].get(name))
    require(changed == repair['changedSources'] and repair['invalidationRationale'], 'repair invalidation record differs')

receipts = []
for case in all_ids:
    directory = evidence if case in current_ids else prior
    for mode in ('positive', 'control'):
        path = directory / (case + '-' + mode) / 'receipt.json'
        receipt = json.loads(path.read_text())
        require(receipt['case'] == case and receipt['mode'] == mode and receipt['status'] == 'PASS' and receipt['contractDigest'] == runtime['contractDigest'] and receipt['originalSourcesUnchanged'] and receipt['observations'], 'passing case/control receipt required: '+case+'-'+mode)
        receipts.append({'case':case,'mode':mode,'status':'PASS','path':str(path),
                         'sha256':sha(path),'retained':directory != evidence})

def messages_proof(directory, filename, mode, packet_tag, feature_name, selected_ids, original_failed_run=False):
    """Retained cases need real PASSED events, never a relabeled failed run."""
    path = directory / filename
    raw = path.read_bytes()
    envelopes = [json.loads(line) for line in raw.decode('utf-8').splitlines()]
    def values(kind):
        return [envelope[kind] for envelope in envelopes if kind in envelope]
    def check(condition, reason):
        require(condition, str(path)+': '+reason)
    def indexed(kind, key):
        items = values(kind)
        result = {item[key]: item for item in items}
        check(len(result) == len(items), 'duplicate '+kind+' identities')
        return result
    check(all(isinstance(envelope, dict) and len(envelope) == 1 for envelope in envelopes), 'invalid Messages envelope')
    check(not values('parseError'), 'outer BDD parse error')
    run_started, run_finished = values('testRunStarted'), values('testRunFinished')
    check(len(run_started) == len(run_finished) == 1, 'exactly one completed run required')
    check(run_finished[0]['success'] is (not original_failed_run), 'unexpected whole-run result')
    check(run_finished[0].get('testRunStartedId') == run_started[0].get('id'), 'run identity mismatch')
    expected_source = (root/'tests/features/contribution_readiness'/feature_name).read_text()
    check(any(Path(source['uri']).name == feature_name and source['data'] == expected_source for source in values('source')), 'exact adopted feature source missing')
    pickles, cases = indexed('pickle','id'), indexed('testCase','id')
    starts, finishes = indexed('testCaseStarted','id'), indexed('testCaseFinished','testCaseStartedId')
    run_ids = all_ids if original_failed_run else selected_ids
    run_count = len(run_ids)
    check(len(starts) == len(finishes) == run_count and starts.keys() == finishes.keys(), 'wrong completed run case count')
    step_starts, step_finishes = values('testStepStarted'), values('testStepFinished')
    check(len(step_starts) == len(step_finishes) == run_count*3, 'wrong started/finished step count')
    start_pairs = [(value['testCaseStartedId'],value['testStepId']) for value in step_starts]
    finish_pairs = [(value['testCaseStartedId'],value['testStepId']) for value in step_finishes]
    check(len(set(start_pairs)) == len(set(finish_pairs)) == run_count*3 and set(start_pairs) == set(finish_pairs), 'step identities missing or duplicated')
    observed_run, selected_starts = [], []
    for start_id, start in starts.items():
        check(start['attempt'] == 0 and finishes[start_id]['willBeRetried'] is False, 'unexpected outer retry')
        check(start['testCaseId'] in cases, 'missing test case reference')
        case = cases[start['testCaseId']]
        check(case['pickleId'] in pickles, 'missing pickle reference')
        pickle = pickles[case['pickleId']]
        check(Path(pickle['uri']).name == feature_name, 'different feature')
        tags = {tag['name'] for tag in pickle['tags']}
        check(packet_tag in tags, 'wrong packet tag')
        ids = [tag[1:] for tag in tags if tag.startswith('@CR47-')]
        check(len(ids) == 1, 'missing/ambiguous adopted scenario identity')
        observed_run.extend(ids)
        expected_steps = {step['id'] for step in case['testSteps']}
        actual_steps = {step for case_start, step in finish_pairs if case_start == start_id}
        check(len(expected_steps) == 3 and expected_steps == actual_steps, 'case lacks its three adopted steps')
        if ids[0] in selected_ids:
            selected_starts.append(start_id)
    check(sorted(observed_run) == run_ids, 'run scenario set differs')
    check(len(selected_starts) == len(selected_ids), 'selected cases missing or duplicated')
    selected_results = [value for value in step_finishes if value['testCaseStartedId'] in selected_starts]
    check(len(selected_results) == len(selected_ids)*3 and all(value['testStepResult']['status'] == 'PASSED' for value in selected_results), 'selected cases contain nonpassing steps')
    return {'path':str(path),'mode':mode,'sha256':hashlib.sha256(raw).hexdigest(),
            'cases':len(selected_ids),'steps':len(selected_ids)*3,
            'runSuccess':run_finished[0]['success'],'scenarioIds':selected_ids,
            'retained':original_failed_run,'originalRunCases':run_count,
            'note':'Only selected individual cases are accepted; original whole-run failure retained.' if original_failed_run else 'Fresh targeted run passed.'}

outer_messages = []
for filename,mode,tag,feature in (
        ('functional-messages.ndjson','positive','@readiness47','readiness.feature'),
        ('controls-messages.ndjson','control','@readiness47_negative','controls.feature')):
    outer_messages.append(messages_proof(evidence,filename,mode,tag,feature,current_ids))
    if repair:
        outer_messages.append(messages_proof(prior,filename,mode,tag,feature,retained_ids,True))
require(sum(packet['cases'] for packet in outer_messages) == 20 and sum(packet['steps'] for packet in outer_messages) == 60, 'combined evidence count differs')
from common import TARGETS, source_hashes
require(source_hashes(root) == runtime['sourceHashes'], 'current source/fixture identity changed')
for target, expected in {**TARGETS, 'parser-step_arguments':[73,241]}.items():
    result=json.loads((consumer/'acceptance-cache'/(target+'.json')).read_text())
    require(result['scope'] == expected and result['counts']['passed'], 'incomplete affected BDD packet')
sdk=json.loads((evidence/'installed-sdk/outer-messages-proof.json').read_text())
require(sdk['status'] == 'PASS' and sdk['cases'] == 22 and sdk['steps'] == 66, 'installed SDK packet incomplete')
with (evidence/'outer-messages-proof.json').open('x') as out:
    json.dump({'packets':outer_messages,'receipts':receipts,'cases':20,'steps':60,'freshCases':len(current_ids)*2,'retainedCases':len(retained_ids)*2,'status':'PASS'},out,indent=2)
with (evidence/'cleanup-start.json').open('x') as out:
    json.dump({'consumerRoot':str(consumer),'owner':actual_owner,'receipts':receipts,'outerMessages':outer_messages,'startedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()},out,indent=2)
shutil.rmtree(consumer)
with (evidence/'cleanup-complete.json').open('x') as out:
    json.dump({'consumerRoot':str(consumer),'removed':not consumer.exists(),'artifactsRetained':str(evidence),
               'priorConsumerRootRetained':previous['consumerRoot'] if repair else None,
               'priorRetentionReason':'Original failed-attempt snapshots retained for root audit and separately validated cleanup; not represented as cleaned.' if repair else None,
               'finishedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()},out,indent=2)
print('Removed only the verified current packet consumers; original failed-attempt evidence and snapshots retained.')
