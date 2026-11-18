"""The ten adopted real-application behaviors, invoked by outer Gherkin only."""
import ast
import copy
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tomllib
from common import CONTRACT_DIGEST, TARGETS, PROFILES, Evidence, bdd_counts, copy_source, demand, record, sha, source_hashes

RUNTIME=json.loads(Path(sys.argv[1]).read_text()); CASE,MODE=sys.argv[2:4]
ROOT=Path(RUNTIME['root']);WORK=Path(RUNTIME['workRoot']);OWNED=Path(RUNTIME['consumerRoot'])
EVIDENCE=Path(RUNTIME['evidence']);CASE_DIR=EVIDENCE/(CASE+'-'+MODE);CASE_DIR.mkdir()
RUN=Evidence(CASE_DIR,RUNTIME);OBS=[]
FIXTURES=json.loads((ROOT/'tests/readiness/fixtures.json').read_text())
CACHE=OWNED/'acceptance-cache';CACHE.mkdir(exist_ok=True)


def reject(operation,label):
    try: operation()
    except AssertionError as error: OBS.append({'control':label,'rejected':str(error)})
    else: raise AssertionError('Misleading result accepted: '+label)


def consumer(name,source,dependency,features=None,modern=False,toolchain='1.88.0',warnings=False):
    directory=OWNED/'applications'/name
    receipt=CACHE/(name+'-'+toolchain+'.json')
    if receipt.exists():
        result=json.loads(receipt.read_text());demand(sha(result['binary'])==result['binarySha256'],'cached native consumer changed')
        demand(sha(source)==result['sourceSha256'],'cached consumer source changed')
        return result
    directory.mkdir(parents=True,exist_ok=True);(directory/'src').mkdir(exist_ok=True)
    shutil.copy2(source,directory/'src/main.rs')
    if name.startswith('parser-'):
        dependencies='gherkin = { path = '+json.dumps(str(dependency))+' }\nserde_json = "1"\n'
        configuration='[features]\nmodern = []\n'
        active=['modern'] if modern else []
    else:
        active=features or []
        dependencies='cucumber = { path = '+json.dumps(str(dependency))+', default-features = false }\nfutures = "0.3"\nregex = "1"\nserde_json = "1"\ntracing = { version = "0.1", optional = true }\n'
        configuration='[features]\n'+''.join(name+' = ["cucumber/'+name+'"'+(', "dep:tracing"' if name=='tracing' else '')+']\n' for name in PROFILES if name!='none')
    manifest='[package]\nname = '+json.dumps(name)+'\nversion = "0.0.0"\nedition = "2024"\nrust-version = "1.88"\n[workspace]\n[dependencies]\n'+dependencies+configuration
    (directory/'Cargo.toml').write_text(manifest)
    flags=['--features',','.join(active)] if active else []
    env={'RUSTUP_TOOLCHAIN':toolchain,'CARGO_TARGET_DIR':str(OWNED/('target-'+toolchain))}
    if warnings: env['RUSTFLAGS']='-Dwarnings'
    RUN.run(['cargo','generate-lockfile'],directory,extra_env=env)
    RUN.run(['cargo','build','--locked',*flags],directory,extra_env=env)
    binary=Path(env['CARGO_TARGET_DIR'])/'debug'/name
    metadata=json.loads(RUN.run(['cargo','metadata','--locked','--format-version','1',*flags],directory,extra_env=env)['stdout'])
    provenance=[{'name':p['name'],'version':p['version'],'source':p['source'],'manifestPath':p['manifest_path']} for p in metadata['packages']]
    result={'binary':str(binary),'binarySha256':sha(binary),'sourceSha256':sha(source),'manifest':manifest,
            'manifestDir':str(directory),'lockSha256':sha(directory/'Cargo.lock'),'packages':provenance,'features':active,'toolchain':toolchain}
    record(receipt,result);record(CASE_DIR/(name+'-'+toolchain+'-consumer.json'),result)
    return result


def parser(name,requests):
    paths={'fork':Path(RUNTIME['gherkinRoot']),'vendor':WORK/'vendor/gherkin','base':Path(RUNTIME['legacyParserRoot'])}
    built=consumer('parser-'+name,ROOT/'tests/readiness/consumers/parser.rs',paths[name],modern=name!='base')
    result=json.loads(RUN.run([built['binary']],OWNED,json.dumps(requests))['stdout'])
    demand(Path(result['manifestDir']).resolve()==Path(built['manifestDir']).resolve(),'wrong parser consumer provenance')
    dependency=[p for p in built['packages'] if p['name']=='gherkin']
    demand(len(dependency)==1 and Path(dependency[0]['manifestPath']).parent.resolve()==paths[name].resolve(),'wrong linked parser source')
    return result['responses']


def official(source):
    script=Path(RUNTIME['oracleRoot'])/'interop/gherkin43/oracle.mjs'
    return json.loads(RUN.run(['node',script,'readiness.feature'],OWNED,source)['stdout'])


def native_from_official(graph):
    feature=graph['gherkinDocument']['feature'];scenarios=[]
    for child in feature['children']:
        scenario=child['scenario'];examples=[]
        for example in scenario['examples']:
            rows=[example['tableHeader']]+example['tableBody']
            examples.append([[cell['value'] for cell in row['cells']] for row in rows])
        scenarios.append({'name':scenario['name'],'steps':[{'text':step['text'],
            'table':[[cell['value'] for cell in row['cells']] for row in step['dataTable']['rows']] if 'dataTable' in step else None,
            'docstring':None} for step in scenario['steps']],'examples':examples})
    return {'name':feature['name'],'scenarios':scenarios}


def equal(actual,expected,label): demand(actual==expected,label+' differs: '+json.dumps({'actual':actual,'expected':expected},ensure_ascii=False))


def cr001(control):
    requests=[{'operation':'parse','source':FIXTURES[name],'policy':policy} for name in ('examples','stepTable') for policy in ('default','new','latest','explicit43')]
    baseline=parser('base',[{'operation':'parse','source':FIXTURES[name],'policy':policy} for name in ('examples','stepTable') for policy in ('default','new')])
    demand(all(not result['ok'] for result in baseline),'immutable legacy parser did not reject exact historical slash')
    truth=[native_from_official(official(FIXTURES[name])) for name in ('examples','stepTable')]
    results={name:parser(name,requests) for name in ('fork','vendor')}
    for name,responses in results.items():
        for index,response in enumerate(responses):
            if index%4==3: demand(response['ok'],'explicit43 rejected official input');equal(response['feature'],truth[index//4],name+' official43 cells/following step')
            else: demand(not response['ok'],name+' silently enabled new table policy')
    recognized=[{'operation':'parse','source':FIXTURES['recognized'],'policy':policy} for policy in ('default','new','latest','explicit43')]
    recognized_truth=native_from_official(official(FIXTURES['recognized']))
    for name in ('fork','vendor'):
        for response in parser(name,recognized):
            demand(response['ok'],'recognized escape rejected');equal(response['feature'],recognized_truth,'recognized escapes and following step')
    OBS.append({'legacyBaseRejected':len(baseline),'constructors':['default','new','latest'],'explicitPolicyMatchesOfficial':True,'recognizedEscapeValues':['a\nb','a|b','a\\b']})
    if control:
        reject(lambda:demand(results['fork'][2]['ok'],'latest vocabulary retains legacy rejection'),'latest vocabulary is not policy opt-in')
        corrupted=copy.deepcopy(truth[1]);corrupted['scenarios'][0]['steps'][0]['table'][0][0]='invented'
        reject(lambda:equal(results['fork'][7]['feature'],corrupted,'corrupted cell'),'changed literal table cell')


def canonical_error(result):
    value=copy.deepcopy(result)
    if 'diagnostic' in value:
        text=value['diagnostic'];match=re.fullmatch(r'(Error at \d+:\d+: )(\{.*\})(.*)',text)
        demand(match is not None,'unexpected classic diagnostic format')
        tokens=ast.literal_eval(match[2]);value['diagnostic']={'prefix':match[1],'tokens':sorted(tokens) if isinstance(tokens,set) else [],'detail':match[3]}
    return value


def cr002(control):
    fixture=OWNED/'diagnostic.feature';fixture.write_text('not a feature\n')
    missing=OWNED/'missing-feature.feature'
    requests=[{'operation':'file','path':str(fixture)},{'operation':'file','path':str(missing)},
              {'operation':'parse','source':FIXTURES['valid'],'policy':'default'}]
    baseline=parser('base',requests)
    demand(not baseline[0]['ok'] and baseline[0]['variant']=='Parsing' and baseline[0]['position']['line']>=1,'immutable parser did not return positioned parsing error')
    demand(baseline[1]['variant']=='Reading' and baseline[1]['ioKind']=='NotFound','reading error variant changed')
    for name in ('fork','vendor'):
        results=parser(name,requests)
        for actual,expected in zip(results,baseline): equal(canonical_error(actual),canonical_error(expected),'public classic diagnostics/'+name)
        markdown=parser(name,[{'operation':'markdown','source':FIXTURES['markdownMalformed']},{'operation':'parse','source':FIXTURES['valid'],'policy':'default'}])
        demand(not markdown[0]['ok'] and markdown[0]['position']['line']>=1 and markdown[0]['position']['column']==1,'additive Markdown positioned error missing')
        demand(markdown[1]['ok'],'valid parse after error failed')
    OBS.append({'originalPublicErrors':baseline,'immutableExpectedTokensNormalizedOnly':True,'markdownErrorAndRecovery':True})
    if control:
        corrupted=copy.deepcopy(baseline[0]);corrupted['position']['line']+=1
        reject(lambda:equal(canonical_error(corrupted),canonical_error(baseline[0]),'position'),'changed error location')
        corrupted=copy.deepcopy(baseline[0]);corrupted['path']+='-wrong'
        reject(lambda:equal(canonical_error(corrupted),canonical_error(baseline[0]),'path'),'changed original error path')


def parser_identity(directory):
    files={str(path.relative_to(directory)):sha(path) for path in sorted((directory/'src').rglob('*')) if path.is_file()}
    files['build.rs']=sha(directory/'build.rs')
    manifest=tomllib.loads((directory/'Cargo.toml').read_text())
    manifest.pop('dev-dependencies',None);manifest.pop('test',None)
    manifest['package']['include']=[entry for entry in manifest['package']['include'] if not entry.lstrip('/').startswith('tests/')]
    return {'production':files,'manifest':manifest,'manifestSha256':sha(directory/'Cargo.toml')}


def cr003(control):
    fork=Path(RUNTIME['gherkinRoot']);vendor=WORK/'vendor/gherkin'
    first,second=parser_identity(fork),parser_identity(vendor)
    equal(first['production'],second['production'],'fork/vendor production identities')
    equal(first['manifest'],second['manifest'],'only documented dev/test packaging manifest differences')
    requests=[{'operation':'document','source':'# only a comment\n','policy':'explicit43'},
              {'operation':'parse','source':'not gherkin','policy':'default'},
              {'operation':'parse','source':FIXTURES['recognized'],'policy':'default'},
              {'operation':'parse','source':FIXTURES['stepTable'],'policy':'explicit43'}]
    left,right=parser('fork',requests),parser('vendor',requests)
    # Error token HashSet order is intentionally non-contractual.
    for a,b in zip(left,right): equal(canonical_error(a),canonical_error(b),'fork/vendor actual observations')
    demand(left[0]=={'ok':True,'feature':None} and left[1]['ok'] is False,'featureless/malformed semantic obligations')
    OBS.append({'sourceIdentity':first,'vendorManifestSha256':second['manifestSha256'],'behavioralObservations':left,'independentSemantics':'CR47-001 official/base comparison'})
    if control:
        disposable=OWNED/'corrupt-parser';shutil.copytree(vendor,disposable)
        target=disposable/'src/lib.rs'
        original=target.read_bytes()
        target.write_bytes(bytes([original[0] ^ 1])+original[1:])
        reject(lambda:equal(first['production'],parser_identity(disposable)['production'],'source identity'),'one-byte disposable parser mutation')
        corrupted=copy.deepcopy(right);corrupted[0]['feature']={'name':'invented'}
        reject(lambda:equal(left,corrupted,'behavior'),'corrupt parser observation')
        shutil.rmtree(disposable);OBS.append({'cleanup':str(disposable),'removed':not disposable.exists()})


def cr004(control):
    path=OWNED/('undefined.feature' if control else 'matched.feature')
    path.write_text('Feature: Consumer\n Scenario: dispatch\n  Given '+('undefined operation' if control else 'a registered application action')+'\n')
    for profile in PROFILES:
        built=consumer('profile-'+profile,ROOT/'tests/readiness/consumers/profiles.rs',WORK,
                       features=[] if profile=='none' else [profile],warnings=True)
        output=json.loads(RUN.run([built['binary'],path],OWNED)['stdout'])
        if control:
            demand(output['sideEffects']==0 and output['executionFailed'] and output['passed']==0,'undefined step invoked handler or passed/'+profile)
            demand(output['failed']+output['skipped']>0,'undefined outcome absent/'+profile)
        else:
            demand(output['sideEffects']==1 and output['passed']==1 and output['failed']==0 and output['skipped']==0 and not output['executionFailed'],'matched consumer behavior/'+profile)
        demand(output['parsingErrors']==0 and output['hookErrors']==0,'consumer infrastructure failed/'+profile)
        if profile=='output-messages':
            messages=[json.loads(line) for line in output['special'].splitlines()]
            statuses=[e['testStepFinished']['testStepResult']['status'] for e in messages if 'testStepFinished'in e]
            demand(statuses==(['UNDEFINED'] if control else ['PASSED']),'Messages feature result absent')
        elif profile=='output-json':
            document=json.loads(output['special']);demand(document and document[0]['elements'],'JSON profile absent')
        elif profile=='output-junit': demand('<testsuite' in output['special'] and '<testcase' in output['special'],'JUnit feature absent')
        elif profile=='libtest': demand(any(json.loads(line).get('type')=='test' for line in output['special'].splitlines()),'libtest feature absent')
        elif profile=='timestamps': demand(output['events'] and all(event.get('timestampNanos') for event in output['events']),'real event timestamp missing')
        elif profile=='tracing' and not control: demand('profile handler evidence' in output['basic'],'actual handler tracing integration missing')
        OBS.append({'profile':profile,'observation':output,'consumer':built['binarySha256'],'rustflags':'-Dwarnings'})


def validate_generated(output):
    # Detailed independent fixture truth is provided below the generated source
    # contract; never derive expectations from the returned Messages itself.
    demand(output['generic']['trace']==['generic:init','generic:7'],'derived default-generic handler/initializer changed')
    demand(output['custom']['trace']==['custom:init','custom:42'],'custom initializer not used')
    demand(output['generic']['generatedExpressionMetadata'] is True and output['generic']['inventorySpecialization']=='Generic<usize>' and output['generic']['arbitraryGenericInventory'] is False, 'default-generic generated options contract changed')
    demand(output['legacy']['trace']==['legacy:body'], 'ordinary legacy World stopped working')
    for key in ('generic','custom','legacy'):
        messages=output[key]['messages']
        definitions=[e['stepDefinition'] for e in messages if 'stepDefinition'in e]
        demand(definitions and all(d.get('pattern',{}).get('source') for d in definitions),'generated DefinitionOptions metadata missing/'+key)
        demand([e['testStepFinished']['testStepResult']['status'] for e in messages if 'testStepFinished'in e]==['PASSED'],'derived handler did not pass/'+key)
    messages=output['contexts']['messages']
    demand(output['contexts']['trace']==['contexts:init','contexts:1'],'attachment/completion context sequence changed')
    attachments=[e['attachment'] for e in messages if 'attachment'in e]
    demand(len(attachments)==1 and attachments[0]['body']=='context payload','actual attachment missing')
    starts={(e['testStepStarted']['testCaseStartedId'],e['testStepStarted']['testStepId']) for e in messages if 'testStepStarted'in e}
    demand((attachments[0]['testCaseStartedId'],attachments[0]['testStepId']) in starts,'attachment misassociated')
    demand([e['testStepFinished']['testStepResult']['status'] for e in messages if 'testStepFinished'in e]==['SKIPPED'],'explicit completion result absent')
    demand(output['contexts']['explicitTimeout'] is True and 50 in output['contexts']['timerMilliseconds'] and 999 not in output['contexts']['timerMilliseconds'], 'actual explicit timeout override not used')
    demand(output['contexts']['attachmentClosed'] is True and output['contexts']['completionClosed'] is True, 'finished context scope remains usable')


def cr005(control):
    built=consumer('generated-options',ROOT/'tests/readiness/consumers/generated.rs',WORK,features=['macros','output-messages'])
    directory=OWNED/('generated-'+MODE);directory.mkdir()
    output=json.loads(RUN.run([built['binary'],directory],OWNED)['stdout']);validate_generated(output)
    OBS.append({'actualGeneratedWorlds':output,'limitation':'Default generic inventory only; arbitrary generic instantiations are not claimed.'})
    if control:
        corrupted=copy.deepcopy(output);corrupted['generic']['messages']=[e for e in corrupted['generic']['messages'] if 'stepDefinition'not in e]
        reject(lambda:validate_generated(corrupted),'removed generated definition metadata')
        corrupted=copy.deepcopy(output)
        next(e['attachment'] for e in corrupted['contexts']['messages'] if 'attachment'in e)['testStepId']='foreign-step'
        reject(lambda:validate_generated(corrupted),'misassociated attachment scope')


def target(name,root=WORK,expected=None,cache=True,extra_env=None):
    key=('parser-' if name=='step_arguments' else '')+name
    receipt=CACHE/(key+'.json')
    if cache and receipt.exists():
        result=json.loads(receipt.read_text());demand(result['scope']==list(expected or TARGETS[name]),'cached BDD scope differs');return result
    flags=[] if name=='step_arguments' else ['--all-features']
    result=RUN.run(['cargo','test','--locked',*flags,'--test',name],root,extra_env=extra_env)
    counts=bdd_counts(result['stdout'],list(expected or TARGETS[name]),name)
    observation={'target':name,'scope':list(expected or TARGETS[name]),'counts':counts,'process':result['record'],'sourceRoot':str(root)}
    if cache: record(receipt,observation)
    return observation


def cr006(control):
    OBS.append({'actualDryRun':target('dry_run')})
    executions=Path(RUNTIME['oracleRoot'])/'executions'
    demand(executions.is_dir() and any(executions.iterdir()),'fresh oracle invocation evidence missing')
    OBS.append({'oracleExecutions':str(executions),'lockSha256':sha(WORK/'tests/interop/package-lock.json')})
    if control:
        source=Path(RUNTIME['oracleRoot'])/'interop';disposable=OWNED/'missing-query';shutil.copytree(source,disposable)
        shutil.rmtree(disposable/'node_modules/@cucumber/query')
        for script in ('consume.mjs','scenario-hooks.mjs'):
            result=RUN.run(['node',disposable/script],disposable,'{}\n',allowed=(1,))
            demand('@cucumber/query' in result['stderr'] and ('ERR_MODULE_NOT_FOUND'in result['stderr'] or 'Cannot find package'in result['stderr']),'oracle failed for unrelated reason')
            OBS.append({'control':script+' missing query','process':result['record'],'explicitFailure':result['stderr']})
        shutil.rmtree(disposable);OBS.append({'cleanup':str(disposable),'removed':not disposable.exists()})


def cr007(control):
    directory=OWNED/('minimum-rejected' if control else 'minimum-fixed')
    copy_source(Path(RUNTIME['failedRoot']) if control else WORK,directory)
    lock=directory/'Cargo.lock'
    if lock.exists(): lock.unlink()
    resolver=RUNTIME['resolverToolchain']
    RUN.run(['cargo','+'+resolver,'update','-Z','minimal-versions'],directory)
    packages=tomllib.loads(lock.read_text())['package']
    versions={name:sorted(p['version'] for p in packages if p['name']==name) for name in ('jsonschema','idna','idna_adapter','icu_normalizer','zerovec','yoke')}
    record(CASE_DIR/'minimum-graph.json',{'versions':versions,'lockSha256':sha(lock),'resolver':resolver})
    shutil.copy2(lock,CASE_DIR/'minimum-Cargo.lock')
    environment={'CARGO_TARGET_DIR':str(OWNED/('minimal-target-'+MODE))}
    if control:
        demand('1.0.2'in versions['idna'] and '0.10.4'in versions['zerovec'] and '0.6.0'in versions['yoke'] and '0.7.3'in versions['yoke'],'BLOCKED: immutable graph did not reproduce recorded incompatible identities')
        result=RUN.run(['cargo','test','--locked','--all-features','--test','messages_corpus'],directory,allowed=(101,),extra_env=environment)
        demand('yoke'in result['stderr'] and ('trait bound'in result['stderr'] or 'different versions'in result['stderr']),'incompatible graph failed for an unrelated reason')
        OBS.append({'control':'actual incompatible dev/schema graph','versions':versions,'process':result['record']})
    else:
        observation=target('messages_corpus',directory,cache=False,extra_env=environment)
        OBS.append({'actualMinimumSchemaPath':observation,'versions':versions,'resolver':resolver,'consumerRust':'1.88.0'})


def rust_block(text):
    match=re.search(r'^```rust\n(.*?)^```\s*$',text,re.M|re.S);demand(match is not None,'bound introduction Rust block missing')
    return '\n'.join(line[2:] if line.startswith('# ') else '' if line=='#' else line for line in match[1].splitlines())+'\n'


def cr008(control):
    baseline=Path(RUNTIME['baseRoot']);book=baseline/'book/src/introduction.md'
    original=book.read_text();source=rust_block(original)
    gherkin=re.search(r'^```gherkin\n(.*?)^```\s*$',original,re.M|re.S).group(1)
    demand(rust_block((WORK/'book/src/introduction.md').read_text())==source,'introduction example differs from adopted immutable base')
    outputs=[]
    for toolchain in ('1.88.0','1.100.0'):
        for name,dependency in (('base',baseline),('head',WORK)):
            directory=OWNED/('book-'+name+'-'+toolchain+('-missing' if control else ''))
            (directory/'src').mkdir(parents=True);(directory/'tests/features/readme').mkdir(parents=True)
            (directory/'src/main.rs').write_text(source);(directory/'tests/features/readme/readme.feature').write_text(gherkin)
            manifest='[package]\nname="book-consumer"\nversion="0.0.0"\nedition="2024"\nrust-version="1.88"\n[workspace]\n[dependencies]\ncucumber={path='+json.dumps(str(dependency))+'}\n'
            if not control: manifest+='tokio={version="1",features=["macros","rt-multi-thread","time"]}\n'
            (directory/'Cargo.toml').write_text(manifest)
            environment={'RUSTUP_TOOLCHAIN':toolchain,'CARGO_TARGET_DIR':str(directory/'target')}
            RUN.run(['cargo','generate-lockfile'],directory,extra_env=environment)
            build=RUN.run(['cargo','build','--locked','--message-format=json'],directory,allowed=(101,) if control else (0,),extra_env=environment)
            if control:
                demand('tokio'in build['stdout']+build['stderr'],'book missing dependency did not cause failure')
                outputs.append({'snapshot':name,'toolchain':toolchain,'missingDependencyRejected':True,'process':build['record']})
            else:
                artifacts=[json.loads(line) for line in build['stdout'].splitlines() if line.startswith('{')]
                binary=next(item['executable'] for item in artifacts if item.get('reason')=='compiler-artifact' and item.get('executable'))
                output=RUN.run([binary],directory,extra_env=environment)
                counts=bdd_counts(output['stdout'],[1,3],'immutable introduction consumer')
                outputs.append({'snapshot':name,'toolchain':toolchain,'counts':counts,'binarySha256':sha(binary),
                    'artifactPaths':[filename for item in artifacts if item.get('reason')=='compiler-artifact' for filename in item.get('filenames',[])],
                    'process':output['record']})
    OBS.append({'immutableBase':RUNTIME['baseRoot'],'bookSha256':sha(book),'sourceSha256':__import__('hashlib').sha256(source.encode()).hexdigest(),
                'actualConsumers':outputs,'remoteMdBookCause':'UNKNOWN: external linkage/layout comparison is retained; unchanged remote mdBook path remains a separate gate.'})


def cr009(control):
    observations=[]
    for name in TARGETS: observations.append(target(name))
    observations.append(target('step_arguments',Path(RUNTIME['gherkinRoot']),[73,241]))
    OBS.append({'exactDedicatedEntryPoints':observations,'legacyEmptyStepHarnessUnchanged':True})
    if control:
        for label,args in [('wrong-tag',['--tags','@readiness47_absent']),('empty-path',['--input',str(OWNED/'empty-features'/'*.feature')])]:
            (OWNED/'empty-features').mkdir(exist_ok=True)
            result=RUN.run(['cargo','test','--locked','--all-features','--test','compatibility','--',*args],WORK,allowed=(0,))
            reject(lambda:bdd_counts(result['stdout'],TARGETS['compatibility'],label),'new boundary guard '+label)
            OBS.append({'actualEmptySelection':label,'process':result['record'],'childExit':result['exit']})


def cr010(control):
    observations=[target(name) for name in TARGETS]
    observations.append(target('step_arguments',Path(RUNTIME['gherkinRoot']),[73,241]))
    packet=EVIDENCE/'installed-sdk';receipt=CACHE/'sdk-packet.json'
    if not receipt.exists():
        sdk_env={'SDK46_EVIDENCE':str(packet)}
        # The existing preparation and actual native package cases remain intact.
        RUN.run([RUNTIME['pythonExecutable'],WORK/'sdk/acceptance/prepare.py'],WORK,extra_env=sdk_env)
        frozen_map = WORK/'tests/readiness/sdk-source-identities.json'
        expected_map_hash = RUNTIME['sourceHashes']['tests/readiness/sdk-source-identities.json']
        demand(sha(frozen_map) == expected_map_hash, 'frozen successor SDK identity map changed')
        retained_map = packet/'successor-source-identities.json'
        shutil.copy2(frozen_map, retained_map)
        sdk_runtime_path = WORK/'sdk/acceptance/runtime.json'
        sdk_runtime = json.loads(sdk_runtime_path.read_text())
        sdk_runtime['successorSourceIdentities'] = {'path':str(retained_map),'sha256':expected_map_hash}
        sdk_runtime['successorPhaseContractDigest'] = CONTRACT_DIGEST
        record(packet/'successor-runtime.json', sdk_runtime)
        sdk_runtime_path.write_text(json.dumps(sdk_runtime,indent=2)+'\n')
        for tag in ('@sdk46','@sdk46_negative'):
            result=RUN.run(['cargo','test','--locked','--manifest-path',WORK/'sdk/Cargo.toml','--test','language_sdk','--','--tags',tag],WORK,extra_env=sdk_env)
            bdd_counts(result['stdout'],[11,33],tag)
        proof=json.loads((packet/'outer-messages-proof.json').read_text())
        demand(proof['cases']==22 and proof['steps']==66 and proof['status']=='PASS','fresh installed SDK packet incomplete')
        demand(json.loads((packet/'cleanup-complete.json').read_text())['removed'],'SDK-owned cleanup missing')
        record(receipt,{'packet':str(packet),'proof':proof})
    sdk=json.loads(receipt.read_text())
    OBS.append({'freshAffectedTargets':observations,'installedNativeSdk':sdk,'rootExpected':[797,3399],'parserExpected':[73,241]})
    if control:
        current=source_hashes(ROOT);equal(current,RUNTIME['sourceHashes'],'original source/fixture identity')
        changed=copy.deepcopy(current);key=next(k for k in changed if k.startswith('tests/fixtures/'));changed[key]='0'*64
        reject(lambda:equal(changed,current,'fixture identity'),'changed original fixture hash')
        for case in ('SDK-001','SDK-006','SDK-010','SDK-011'):
            actual=json.loads((packet/(case+'-control')/'receipt.json').read_text())
            demand(actual['status']=='PASS' and actual['observations'],'actual SDK native/attempt/reference controls absent')
            OBS.append({'existingControlExecuted':case,'receiptSha256':sha(packet/(case+'-control')/'receipt.json')})


try:
    demand(RUNTIME['contractDigest']==CONTRACT_DIGEST,'stale readiness contract')
    equal(source_hashes(ROOT),RUNTIME['sourceHashes'],'sources changed after phase preparation')
    globals()['cr'+CASE.split('-')[1]](MODE=='control')
    equal(source_hashes(ROOT),RUNTIME['sourceHashes'],'sources changed during acceptance')
    receipt={'case':CASE,'mode':MODE,'status':'PASS','contractDigest':CONTRACT_DIGEST,
             'observations':OBS,'originalSourcesUnchanged':True,'commands':RUN.commands}
    record(CASE_DIR/'receipt.json',receipt);print(json.dumps(receipt))
except BaseException as error:
    record(CASE_DIR/'failure.json',{'case':CASE,'mode':MODE,'status':'FAIL','error':repr(error),'observations':OBS,'commands':RUN.commands})
    raise
