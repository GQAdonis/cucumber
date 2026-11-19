"""Shared evidence support, executed only within the adopted whole-phase BDD."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

TARGETS = {
    'compatibility': [20,115], 'portability': [1,5], 'hooks': [9,42],
    'messages': [20,97], 'scheduling': [8,50], 'sources': [21,81],
    'messages_source': [19,80], 'messages_retries': [6,40], 'messages_hooks': [10,70],
    'messages_consumer': [2,8], 'messages_docstrings': [15,86], 'interpolation': [9,41],
    'messages_errors': [6,30], 'messages_backgrounds': [12,64], 'messages_logs': [7,46],
    'messages_versions': [3,12], 'step_hooks': [10,51], 'expression_compat': [53,159],
    'messages_corpus': [62,236], 'messages_attachments': [9,36], 'messages_documents': [11,41],
    'run_hooks': [14,62], 'scenario_hook_records': [18,76], 'messages_support_code': [14,56],
    'messages_run_hooks': [6,34], 'messages_markdown': [21,78], 'messages_markdown_runtime': [14,54],
    'messages_scenario_hooks': [13,64], 'messages_expression_metadata': [19,85], 'timeouts': [14,50],
    'execution_control_formats': [18,54], 'composable_filters': [12,56], 'execution_control': [20,87],
    'dry_run': [14,59], 'line_selection': [38,178], 'messages_custom_metadata': [16,78],
    'dry_run_formats': [9,30], 'retry_policy': [16,56], 'ordered_scheduling': [19,81],
    'lexical_semantics': [25,110], 'vlbv_adapter': [47,175], 'source_paths': [13,44],
    'dynamic_assignment': [14,55], 'messages_table_columns': [11,53], 'timeout_preparation': [17,69],
    'expression_names': [12,47], 'generated_ordering': [10,45], 'messages_rerun': [19,73],
    'messages_markdown_precedence': [21,100],
}
PROFILES = ['none','macros','timestamps','output-json','output-junit','libtest','tracing','output-messages']
CONTRACT_DIGEST = os.environ.get('READINESS47_CONTRACT_DIGEST')
if not CONTRACT_DIGEST:
    raise SystemExit('READINESS47_CONTRACT_DIGEST must identify the current supported complete-boundary binding')
BOOK_BASE = 'd95872541ee2a43d71089c64bd3fa8848e24c922'
PARSER_BASE = '4c30e3a48a0226bf907053a0a9e738e91cf06727'
FAILED_BASE = 'ee22c6aa024cc010e499241e3cdcd01009fbf9bb'


def demand(condition, message):
    if not condition: raise AssertionError(message)


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(path, value):
    with Path(path).open('x') as output:
        json.dump(value, output, indent=2, ensure_ascii=False)
        output.write('\n')


def source_hashes(root):
    result = {}
    root = Path(root)
    for base in ('src','codegen/src','vendor/gherkin/src','sdk/src','bindings','tests','book/src'):
        for path in sorted((root/base).rglob('*')):
            if path.is_file() and not any(part in ('target','node_modules','__pycache__','.venv') for part in path.parts):
                if path.name == 'runtime.json' or path.suffix in ('.node','.dylib','.so','.pyc'): continue
                result[str(path.relative_to(root))] = sha(path)
    for name in ('Cargo.toml','codegen/Cargo.toml','vendor/gherkin/Cargo.toml','vendor/gherkin/build.rs','Makefile','.github/workflows/ci.yml'):
        if (root/name).is_file(): result[name] = sha(root/name)
    return result


def copy_source(source, destination):
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(
        '.git','target','node_modules','__pycache__','.venv','.aws','.codex','.agents',
        '.DS_Store','runtime.json','*.node','*.dylib','*.so','*.pyc','build'))


class Evidence:
    def __init__(self, directory, runtime=None):
        self.directory = Path(directory)
        self.runtime = runtime or {}
        self.counter = 0
        self.commands = []

    def run(self, argv, cwd, payload='', allowed=(0,), extra_env=None, timeout=3600):
        self.counter += 1
        label = f'{self.counter:04d}'
        env = os.environ.copy()
        for name in ('NODE_PATH','NODE_OPTIONS','PYTHONPATH','PYTHONHOME','VIRTUAL_ENV'):
            env.pop(name, None)
        env.update({'PYTHONNOUSERSITE':'1','RUSTUP_TOOLCHAIN':'1.88.0','CARGO_TERM_COLOR':'never'})
        for name,key in [('CARGO_TARGET_DIR','targetRoot'),('CUCUMBER_ORACLE_ROOT','oracleRoot')]:
            if key in self.runtime: env[name] = self.runtime[key]
        if 'nodeDirectory' in self.runtime: env['PATH'] = self.runtime['nodeDirectory'] + os.pathsep + env['PATH']
        env.update(extra_env or {})
        start = datetime.datetime.now(datetime.timezone.utc).isoformat()
        stdin = self.directory/(label+'-stdin.txt'); stdin.write_text(payload)
        stdout_path, stderr_path = self.directory/(label+'-stdout.txt'), self.directory/(label+'-stderr.txt')
        entry = {'argv':[str(x) for x in argv], 'cwd':str(cwd), 'startedAt':start,
                 'environment':{name:env[name] for name in ('RUSTUP_TOOLCHAIN','RUSTFLAGS','CARGO_TARGET_DIR','CUCUMBER_ORACLE_ROOT','SDK46_EVIDENCE') if name in env},
                 'stdinSha256':sha(stdin)}
        try:
            with stdout_path.open('x') as stdout, stderr_path.open('x') as stderr:
                completed = subprocess.run(entry['argv'], cwd=cwd, input=payload, text=True,
                                           stdout=stdout, stderr=stderr, env=env, timeout=timeout)
            entry['exitCode'] = completed.returncode
        except BaseException as error:
            entry['exception'] = repr(error)
            entry['exitCode'] = None
            raise
        finally:
            entry['finishedAt'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            record(self.directory/(label+'-process.json'), entry)
            self.commands.append(entry)
        demand(entry['exitCode'] in allowed, f'child {label} returned {entry["exitCode"]}; original logs retained in {self.directory}')
        return {'stdout':stdout_path.read_text(), 'stderr':stderr_path.read_text(), 'exit':entry['exitCode'], 'record':str(self.directory/(label+'-process.json'))}


def bdd_counts(output, expected, label):
    plain = re.sub(r'\x1b\[[0-9;]*m','',output)
    scenarios = re.findall(r'^\s*(\d+) scenarios?(?: \(([^\n]*)\))?\s*$', plain, re.M)
    steps = re.findall(r'^\s*(\d+) steps?(?: \(([^\n]*)\))?\s*$', plain, re.M)
    demand(scenarios and steps, label + ': missing actual BDD summary')
    actual = [int(scenarios[-1][0]), int(steps[-1][0])]
    demand(actual == expected and all(actual), f'{label}: scope {actual} differs from {expected}')
    for count, details in (scenarios[-1],steps[-1]):
        demand(details == count+' passed', label + ': skipped/failed/retried or incomplete result: '+details)
    return {'scenarios':actual[0],'steps':actual[1],'passed':True}
