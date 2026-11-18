#!/usr/bin/env python3
"""Preparation belongs to the complete readiness BDD packet, never a precheck."""
import json
import os
from pathlib import Path
import shutil
import sys
import tarfile
import tempfile
from common import BOOK_BASE, PARSER_BASE, FAILED_BASE, CONTRACT_DIGEST, TARGETS, PROFILES, Evidence, copy_source, demand, record, sha, source_hashes

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = Path(os.environ['READINESS47_EVIDENCE']).absolute()
EVIDENCE.mkdir(parents=True, exist_ok=False)
CONSUMERS = Path(tempfile.mkdtemp(prefix='cucumber-readiness47-consumers-')).resolve()
RUNTIME = {'root':str(ROOT),'evidence':str(EVIDENCE),'consumerRoot':str(CONSUMERS),
           'workRoot':str(CONSUMERS/'cucumber'),'gherkinRoot':str(CONSUMERS/'gherkin'),
           'legacyParserRoot':str(CONSUMERS/'legacy-parser'),'baseRoot':str(CONSUMERS/'book-base'),
           'failedRoot':str(CONSUMERS/'failed-minimum'),'targetRoot':str(CONSUMERS/'target'),
           'oracleRoot':str(CONSUMERS/'oracles'),'pythonExecutable':sys.executable,
           'nodeDirectory':str(Path(shutil.which('node')).resolve().parent),
           'resolverToolchain':os.environ.get('READINESS47_RESOLVER','nightly-2026-11-18'),
           'contractDigest':CONTRACT_DIGEST}
RUN = Evidence(EVIDENCE,RUNTIME)
record(CONSUMERS/'.readiness47-owned.json', {'kind':'readiness47-disposable-consumers','root':str(ROOT),'evidence':str(EVIDENCE)})


def archive(repo, revision, destination):
    archive_path = EVIDENCE/(destination.name+'.tar')
    RUN.run(['git','archive','--format=tar','--output',archive_path,revision],repo)
    destination.mkdir()
    with tarfile.open(archive_path) as archive_file:
        for member in archive_file.getmembers():
            demand(not member.issym() and not member.islnk() and (destination/member.name).resolve().is_relative_to(destination), 'unsafe immutable snapshot member')
        archive_file.extractall(destination)
    return {'revision':revision,'archive':str(archive_path),'sha256':sha(archive_path)}


try:
    contract=json.loads((ROOT/'.kbd-orchestrator/phases/phase-47-contribution-readiness/adopted-contract.json').read_text())
    demand(contract['identity']['contractDigest']==CONTRACT_DIGEST,'wrong adopted contract')
    record(EVIDENCE/'source-before.json',source_hashes(ROOT))
    for argv in (['rustc','-Vv'],['cargo','-Vv'],['node','--version'],['npm','--version'],[sys.executable,'--version']):
        RUN.run(argv,ROOT)
    demand(RUN.commands[0]['exitCode']==0,'consumer toolchain unavailable')
    demand('rustc 1.88.0' in (EVIDENCE/'0001-stdout.txt').read_text(), 'Rust consumer identity is not 1.88.0')
    demand((EVIDENCE/'0003-stdout.txt').read_text().strip()=='v26.5.0','Node consumer identity is not 26.5.0')
    demand(sys.version_info[:3]==(3,11,3),'Python consumer identity is not 3.11.3')
    for label, repository in (('cucumber', ROOT), ('gherkin', ROOT.parent/'gherkin')):
        previous = repository/'Cargo.lock'
        if previous.exists():
            preserved = EVIDENCE/(label+'-Cargo.lock.before')
            shutil.copy2(previous, preserved)
            record(EVIDENCE/(label+'-lock-before.json'), {'path':str(previous),'sha256':sha(preserved),'existed':True})
        else:
            record(EVIDENCE/(label+'-lock-before.json'), {'path':str(previous),'existed':False})
        RUN.run(['cargo','generate-lockfile'], repository)
    shutil.copy2(ROOT/'Cargo.lock',EVIDENCE/'root-Cargo.lock')
    shutil.copy2(ROOT.parent/'gherkin/Cargo.lock',EVIDENCE/'gherkin-Cargo.lock')
    copy_source(ROOT,Path(RUNTIME['workRoot']))
    parser_repo=ROOT.parent/'gherkin'
    copy_source(parser_repo,Path(RUNTIME['gherkinRoot']))
    snapshots=[archive(parser_repo,PARSER_BASE,Path(RUNTIME['legacyParserRoot'])),
               archive(ROOT,BOOK_BASE,Path(RUNTIME['baseRoot'])),archive(ROOT,FAILED_BASE,Path(RUNTIME['failedRoot']))]
    record(EVIDENCE/'immutable-snapshots.json',snapshots)
    oracle=Path(RUNTIME['oracleRoot']);oracle.mkdir()
    boundaries=[]
    for relative in ('interop','interop/gherkin43','interop/expressions','interop/rerun'):
        source=ROOT/'tests'/relative;destination=oracle/relative;destination.mkdir(parents=True,exist_ok=True)
        names=['package.json','package-lock.json']+[p.name for p in sorted(source.glob('*.mjs'))]
        for name in names: shutil.copy2(source/name,destination/name)
        command=['npm','ci','--ignore-scripts','--no-audit','--no-fund','--prefix',str(destination)]
        RUN.run(command,destination)
        boundaries.append({'relative':relative,'packageJsonSha256':sha(source/'package.json'),
                           'packageLockSha256':sha(source/'package-lock.json'),
                           'scripts':{name:sha(source/name) for name in names if name.endswith('.mjs')},
                           'install':{'argv':command,'exitCode':0}})
    record(oracle/'oracle-prepared.json',{'schemaVersion':1,'root':str(oracle),'boundaries':boundaries})
    record(EVIDENCE/'oracle-prepared.json',{'schemaVersion':1,'root':str(oracle),'boundaries':boundaries})
    # Acquisition and identity checks occur here, inside the adopted boundary.
    RUN.run(['rustup','toolchain','install',RUNTIME['resolverToolchain'],'--profile','minimal'],ROOT)
    resolver=RUN.run(['rustc','+'+RUNTIME['resolverToolchain'],'-Vv'],ROOT)
    demand('59cbdee2e' in resolver['stdout'],'BLOCKED: resolver identity differs from adopted observed nightly')
    RUN.run(['cargo','+'+RUNTIME['resolverToolchain'],'-Vv'],ROOT)
    RUN.run(['rustup','toolchain','install','1.100.0','--profile','minimal'],ROOT)
    RUN.run(['rustc','+1.100.0','-Vv'],ROOT)
    RUNTIME['sourceHashes']=source_hashes(ROOT)
    RUNTIME['targets']=TARGETS;RUNTIME['profiles']=PROFILES
    record(EVIDENCE/'runtime.json',RUNTIME)
    (ROOT/'tests/readiness/runtime.json').write_text(json.dumps(RUNTIME,indent=2)+'\n')
    record(EVIDENCE/'preparation-complete.json',{'status':'PREPARED','commands':RUN.commands,
        'note':'No acceptance claimed; original/fresh snapshots, collaborators and tool identities retained.'})
except BaseException as error:
    record(EVIDENCE/'preparation-failure.json',{'status':'BLOCKED','error':repr(error),'commands':RUN.commands,'consumerRoot':str(CONSUMERS)})
    raise
