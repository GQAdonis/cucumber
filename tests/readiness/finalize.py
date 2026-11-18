#!/usr/bin/env python3
"""Clean only this packet's owned disposable consumers after 20 passing receipts and the affected packet."""
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
if consumer.is_symlink():
    raise SystemExit('Refusing symlink consumer root')
consumer = consumer.resolve()
expected_owner = {'kind': 'readiness47-disposable-consumers', 'root': str(root), 'evidence': str(evidence)}
actual_owner = json.loads((consumer / '.readiness47-owned.json').read_text())
if actual_owner != expected_owner or consumer.parent != Path(tempfile.gettempdir()).resolve() or not consumer.name.startswith('cucumber-readiness47-consumers-') or consumer.is_relative_to(root) or consumer.stat().st_uid != os.getuid():
    raise SystemExit('Refusing cleanup: disposable-root identity mismatch')
receipts = []
for number in range(1, 11):
    for mode in ('positive', 'control'):
        case = f'CR47-{number:03d}'
        receipt = json.loads((evidence / (case + '-' + mode) / 'receipt.json').read_text())
        if receipt['case'] != case or receipt['mode'] != mode or receipt['status'] != 'PASS' or not receipt['originalSourcesUnchanged'] or not receipt['observations']:
            raise SystemExit('Refusing cleanup: full passing packet receipts are required')
        receipts.append({'case': case, 'mode': mode, 'status': 'PASS'})

def messages_proof(filename, mode, packet_tag, feature_name):
    """Validate original outer runner events before deleting any consumer."""
    path = evidence / filename
    raw = path.read_bytes()
    envelopes = [json.loads(line) for line in raw.decode('utf-8').splitlines()]
    def values(kind):
        return [envelope[kind] for envelope in envelopes if kind in envelope]
    def require(condition, reason):
        if not condition:
            raise SystemExit('Refusing cleanup: ' + filename + ': ' + reason)
    def indexed(kind, key):
        items = values(kind)
        result = {item[key]: item for item in items}
        require(len(result) == len(items), 'duplicate ' + kind + ' identities')
        return result
    require(all(isinstance(envelope, dict) and len(envelope) == 1 for envelope in envelopes), 'invalid Messages envelope')
    require(not values('parseError'), 'outer BDD parse error')
    run_started, run_finished = values('testRunStarted'), values('testRunFinished')
    require(len(run_started) == len(run_finished) == 1, 'exactly one completed run required')
    require(run_finished[0]['success'] is True, 'outer BDD run failed')
    require(run_finished[0].get('testRunStartedId') == run_started[0].get('id'), 'run identity mismatch')
    sources = values('source')
    expected_source = (root / 'tests/features/contribution_readiness' / feature_name).read_bytes().decode('utf-8')
    require(any(Path(source['uri']).name == feature_name and source['data'] == expected_source for source in sources), 'exact adopted feature source missing')
    pickles = indexed('pickle', 'id')
    cases = indexed('testCase', 'id')
    starts = indexed('testCaseStarted', 'id')
    finishes = indexed('testCaseFinished', 'testCaseStartedId')
    require(len(starts) == len(finishes) == 10 and starts.keys() == finishes.keys(), 'ten complete cases required')
    step_finishes = values('testStepFinished')
    step_starts = values('testStepStarted')
    require(len(step_starts) == len(step_finishes) == 30, 'thirty started and finished steps required')
    start_pairs = [(value['testCaseStartedId'], value['testStepId']) for value in step_starts]
    finish_pairs = [(value['testCaseStartedId'], value['testStepId']) for value in step_finishes]
    require(len(set(start_pairs)) == len(set(finish_pairs)) == 30 and set(start_pairs) == set(finish_pairs), 'step identities missing or duplicated')
    require(all(value['testStepResult']['status'] == 'PASSED' for value in step_finishes), 'nonpassing outer BDD step')
    observed_cases = []
    for start_id, start in starts.items():
        require(start['attempt'] == 0 and finishes[start_id]['willBeRetried'] is False, 'unexpected outer retry')
        require(start['testCaseId'] in cases, 'missing test case reference')
        case = cases[start['testCaseId']]
        require(case['pickleId'] in pickles, 'missing pickle reference')
        pickle = pickles[case['pickleId']]
        require(Path(pickle['uri']).name == feature_name, 'case came from a different feature')
        tags = {tag['name'] for tag in pickle['tags']}
        require(packet_tag in tags, 'wrong outer packet tag')
        ids = [tag[1:] for tag in tags if tag.startswith('@CR47-')]
        require(len(ids) == 1, 'missing or ambiguous adopted scenario identity')
        observed_cases.extend(ids)
        expected_steps = {step['id'] for step in case['testSteps']}
        actual_steps = {step for case_start, step in finish_pairs if case_start == start_id}
        require(len(expected_steps) == 3 and expected_steps == actual_steps, 'case does not contain exactly its three adopted steps')
    require(sorted(observed_cases) == [f'CR47-{number:03d}' for number in range(1, 11)], 'adopted scenario set differs')
    return {'path': str(path), 'mode': mode, 'sha256': hashlib.sha256(raw).hexdigest(),
            'cases': 10, 'steps': 30, 'runSuccess': True, 'scenarioIds': sorted(observed_cases)}

outer_messages = [messages_proof('functional-messages.ndjson', 'positive', '@readiness47', 'readiness.feature'),
                  messages_proof('controls-messages.ndjson', 'control', '@readiness47_negative', 'controls.feature')]
with (evidence / 'outer-messages-proof.json').open('x') as out:
    json.dump({'packets': outer_messages, 'cases': 20, 'steps': 60, 'status': 'PASS'}, out, indent=2)
from common import TARGETS, source_hashes
if source_hashes(root) != runtime['sourceHashes']:
    raise SystemExit('Refusing cleanup: original source/fixture identity changed')
for target, expected in {**TARGETS, 'parser-step_arguments':[73,241]}.items():
    result=json.loads((consumer/'acceptance-cache'/(target+'.json')).read_text())
    if result['scope'] != expected or not result['counts']['passed']:
        raise SystemExit('Refusing cleanup: incomplete fixed affected BDD packet')
sdk=json.loads((evidence/'installed-sdk/outer-messages-proof.json').read_text())
if sdk['status'] != 'PASS' or sdk['cases'] != 22 or sdk['steps'] != 66:
    raise SystemExit('Refusing cleanup: installed SDK packet incomplete')
with (evidence / 'cleanup-start.json').open('x') as out:
    json.dump({'consumerRoot': str(consumer), 'owner': actual_owner, 'receipts': receipts, 'outerMessages': outer_messages, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}, out, indent=2)
shutil.rmtree(consumer)
with (evidence / 'cleanup-complete.json').open('x') as out:
    json.dump({'consumerRoot': str(consumer), 'removed': not consumer.exists(), 'artifactsRetained': str(evidence), 'finishedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}, out, indent=2)
print('Removed the verified packet disposable consumers; original artifacts and receipts retained.')
