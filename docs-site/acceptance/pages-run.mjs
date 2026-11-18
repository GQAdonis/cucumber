// Finite BDD boundary: preserve original artifacts and refuse zero selection.
import { spawn } from 'node:child_process';
import { readFile, mkdir, writeFile, readdir, open } from 'node:fs/promises';
import { finished as streamFinished } from 'node:stream/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const cwd = resolve(fileURLToPath(new URL('..', import.meta.url)));
if (!process.env.PAGES_EVIDENCE) throw new Error('Set PAGES_EVIDENCE to a fresh absolute evidence directory');
const evidence = resolve(process.env.PAGES_EVIDENCE);
await mkdir(evidence, { recursive: true });
const preparation = new Set(['source-before-boundary.json', 'repair-reason.md', 'packet.txt']);
if ((await readdir(evidence)).some((name) => !preparation.has(name))) {
  throw new Error('Refusing to overwrite existing evidence: choose a fresh directory');
}
// Exclusive claim prevents two simultaneous launchers from sharing a directory.
const claim = await open(resolve(evidence, '.run-claimed'), 'wx');
await claim.close();
const logFile = await open(resolve(evidence, 'bdd.log'), 'wx');
const log = logFile.createWriteStream();
const argv = ['node_modules/@cucumber/cucumber/bin/cucumber.js', '--config', 'acceptance/pages.cucumber.mjs'];
let code;
try {
  code = await new Promise((done, reject) => {
    const child = spawn(process.execPath, argv, { cwd, env: process.env, stdio: ['ignore', 'pipe', 'pipe'] });
    child.stdout.on('data', (chunk) => { process.stdout.write(chunk); log.write(chunk); });
    child.stderr.on('data', (chunk) => { process.stderr.write(chunk); log.write(chunk); });
    child.on('error', reject);
    child.on('close', (code, signal) => done(signal ? 1 : code));
  });
} finally {
  log.end();
  await streamFinished(log);
}
let messageError;
let started = 0, finished = 0, runSuccess = false;
try {
  for (const line of (await readFile(resolve(evidence, 'messages.ndjson'), 'utf8')).split('\n').filter(Boolean)) {
    const envelope = JSON.parse(line);
    if (envelope.testCaseStarted) started++;
    if (envelope.testCaseFinished) finished++;
    if (envelope.testRunFinished) runSuccess = envelope.testRunFinished.success;
  }
} catch (error) { messageError = String(error); }
const passed = code === 0 && started === 4 && finished === 4 && runSuccess && !messageError;
const receipt = { argv: [process.execPath, ...argv], cwd, code, expectedScenarios: 4, started, finished, runSuccess, messageError, passed };
await writeFile(resolve(evidence, 'boundary-receipt.json'), JSON.stringify(receipt, null, 2));
if (!passed) console.error('Public Pages BDD boundary failed:', receipt);
process.exitCode = passed ? 0 : 1;
