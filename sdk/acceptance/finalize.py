#!/usr/bin/env python3
"""Clean only this packet's owned disposable consumers after 22 passing receipts."""
from pathlib import Path
import datetime
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
expected_owner = {'kind': 'sdk46-disposable-consumers', 'root': str(root), 'evidence': str(evidence)}
actual_owner = json.loads((consumer / '.sdk46-owned.json').read_text())
if actual_owner != expected_owner or consumer.parent != Path(tempfile.gettempdir()).resolve() or not consumer.name.startswith('cucumber-sdk46-consumers-') or consumer.is_relative_to(root) or consumer.stat().st_uid != os.getuid():
    raise SystemExit('Refusing cleanup: disposable-root identity mismatch')
receipts = []
for number in range(1, 12):
    for mode in ('positive', 'control'):
        case = f'SDK-{number:03d}'
        receipt = json.loads((evidence / (case + '-' + mode) / 'receipt.json').read_text())
        if receipt['case'] != case or receipt['mode'] != mode or receipt['status'] != 'PASS' or not receipt['oracleArtifactsUnchanged'] or not receipt['observations']:
            raise SystemExit('Refusing cleanup: full passing packet receipts are required')
        receipts.append({'case': case, 'mode': mode, 'status': 'PASS'})
with (evidence / 'cleanup-start.json').open('x') as out:
    json.dump({'consumerRoot': str(consumer), 'owner': actual_owner, 'receipts': receipts, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}, out, indent=2)
shutil.rmtree(consumer)
with (evidence / 'cleanup-complete.json').open('x') as out:
    json.dump({'consumerRoot': str(consumer), 'removed': not consumer.exists(), 'artifactsRetained': str(evidence / 'artifacts'), 'finishedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}, out, indent=2)
print('Removed the verified packet disposable consumers; original artifacts and receipts retained.')
