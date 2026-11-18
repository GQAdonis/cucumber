import { After, AfterAll, Before, BeforeAll, Given, When, Then, setDefaultTimeout } from '@cucumber/cucumber';
import { chromium } from 'playwright-core';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { readFile, writeFile, mkdir, readdir, stat, cp, mkdtemp, rm } from 'node:fs/promises';
import { resolve, join, relative, extname, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

setDefaultTimeout(180_000);
const siteRoot = resolve(fileURLToPath(new URL('../..', import.meta.url)));
const repoRoot = resolve(siteRoot, '..');
assert(process.env.DOCS_EVIDENCE, 'DOCS_EVIDENCE must identify a fresh evidence directory');
const evidence = resolve(process.env.DOCS_EVIDENCE);
const sites = {
  cucumber: { root: siteRoot, heading: 'Cucumber for Rust' },
  gherkin: { root: resolve(process.env.GHERKIN_REPO || resolve(repoRoot, '../gherkin'), 'docs-site'), heading: 'Gherkin for Rust' },
};
let browser;
let server;
let origin;
let sequence = 0;
const receipts = [];
const cleanup = [];
const digest = (data) => createHash('sha256').update(data).digest('hex');

async function command(cwd, argv, label, env = {}) {
  const startedAt = new Date().toISOString();
  const result = await new Promise((done, reject) => {
    const child = spawn(argv[0], argv.slice(1), {
      cwd, env: { ...process.env, ...env }, stdio: ['ignore', 'pipe', 'pipe'],
    });
    let stdout = '', stderr = '';
    child.stdout.on('data', (part) => { stdout += part; });
    child.stderr.on('data', (part) => { stderr += part; });
    child.on('error', reject);
    child.on('close', (code, signal) => done({ code, signal, stdout, stderr }));
  });
  await writeFile(join(evidence, label + '.stdout.log'), result.stdout);
  await writeFile(join(evidence, label + '.stderr.log'), result.stderr);
  receipts.push({ cwd, argv, env, label, startedAt, finishedAt: new Date().toISOString(), code: result.code, signal: result.signal,
    stdoutSha256: digest(result.stdout), stderrSha256: digest(result.stderr) });
  await writeFile(join(evidence, 'commands.json'), JSON.stringify(receipts, null, 2));
  return result;
}

async function inventory(root, exclusions = new Set()) {
  const files = {};
  async function walk(directory) {
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      if (exclusions.has(entry.name) || entry.isSymbolicLink()) continue;
      const path = join(directory, entry.name);
      if (entry.isDirectory()) await walk(path);
      else if (entry.isFile()) files[relative(root, path)] = digest(await readFile(path));
    }
  }
  await walk(root);
  return files;
}

BeforeAll({ timeout: 300_000 }, async function () {
  await mkdir(evidence, { recursive: true });
  for (const [name, site] of Object.entries(sites)) {
    site.prefix = '/preview/' + name + '/';
    site.build = join(site.root, 'build');
    const result = await command(site.root, ['npm', 'run', 'build'], name + '-production-build', { DOCS_BASE_URL: site.prefix });
    assert.equal(result.code, 0, name + ' production build failed; retained complete build logs');
    await writeFile(join(evidence, name + '-build-sha256.json'), JSON.stringify(await inventory(site.build), null, 2));
  }
  server = createServer(async (request, response) => {
    try {
      const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
      const site = Object.values(sites).find((item) => pathname.startsWith(item.prefix));
      if (!site) { response.writeHead(404); response.end('Unknown documentation root'); return; }
      const suffix = pathname.slice(site.prefix.length);
      let path = resolve(site.build, suffix);
      if (path !== site.build && !path.startsWith(site.build + sep)) { response.writeHead(400); response.end(); return; }
      let status = 200;
      try {
        if ((await stat(path)).isDirectory()) path = join(path, 'index.html');
        await stat(path);
      } catch {
        path = join(site.build, '404.html');
        status = 404;
      }
      const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };
      response.writeHead(status, { 'content-type': types[extname(path)] || 'application/octet-stream' });
      response.end(await readFile(path));
    } catch (error) {
      response.writeHead(500); response.end(String(error));
    }
  });
  await new Promise((done) => server.listen(0, '127.0.0.1', done));
  origin = 'http://127.0.0.1:' + server.address().port;
  browser = await chromium.launch({ channel: process.env.DOCS_BROWSER_CHANNEL || 'chrome', headless: true });
  await writeFile(join(evidence, 'environment.json'), JSON.stringify({ node: process.version, platform: process.platform, architecture: process.arch, browser: browser.version(), origin, sites }, null, 2));
});

Before(async function ({ pickle }) {
  this.id = String(++sequence).padStart(2, '0');
  this.name = pickle.name;
  this.context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, colorScheme: 'light' });
  this.page = await this.context.newPage();
  this.errors = [];
  this.page.on('pageerror', (error) => this.errors.push(String(error)));
  this.page.on('requestfailed', (request) => this.errors.push(request.url() + ': ' + request.failure()?.errorText));
  this.page.on('response', (response) => {
    if (response.url().startsWith(origin) && response.status() >= 400) this.errors.push(response.status() + ' ' + response.url());
  });
});

After(async function ({ result }) {
  if (this.page) {
    await this.page.screenshot({ path: join(evidence, this.id + '-page.png'), fullPage: true });
    await writeFile(join(evidence, this.id + '-observation.json'), JSON.stringify({ name: this.name, status: result?.status, url: this.page.url(), errors: this.errors }, null, 2));
  }
  await this.context?.close();
  if (this.scratch) {
    await rm(this.scratch, { recursive: true, force: true });
    cleanup.push({ path: this.scratch, removed: true });
    await writeFile(join(evidence, 'cleanup.json'), JSON.stringify(cleanup, null, 2));
  }
});

AfterAll(async function () {
  await browser?.close();
  if (server) await new Promise((done) => server.close(done));
  cleanup.push({ browserClosed: Boolean(browser), serverClosed: Boolean(server) });
  await writeFile(join(evidence, 'cleanup.json'), JSON.stringify(cleanup, null, 2));
});

Given('the production documentation for {string} is served below a non-root path', function (name) {
  assert(sites[name], 'Unknown project');
  this.site = sites[name];
});
When('a reader opens the home page', async function () {
  const response = await this.page.goto(origin + this.site.prefix, { waitUntil: 'networkidle' });
  assert.equal(response.status(), 200);
});
Then('the page identifies the GQAdonis fork without upstream endorsement', async function () {
  assert.equal(await this.page.getByRole('heading', { level: 1 }).textContent(), this.site.heading);
  assert.match(await this.page.locator('main').innerText(), /GQAdonis/);
  assert.match(await this.page.getByRole('contentinfo').innerText(), /Not endorsed by the upstream/);
});
Then('the reader can open the compatibility and evidence pages', async function () {
  await this.page.locator('.navbar').getByRole('link', { name: 'Compatibility', exact: true }).click();
  await this.page.getByRole('heading', { name: 'Compatibility', exact: true, level: 1 }).waitFor();
  assert(this.page.url().startsWith(origin + this.site.prefix));
  await this.page.locator('.navbar').getByRole('link', { name: 'Evidence', exact: true }).click();
  await this.page.getByRole('heading', { name: 'Evidence', exact: true, level: 1 }).waitFor();
  assert.match(await this.page.locator('main').innerText(), /73.*241/);
  const links = await this.page.locator('main a[href*="github.com/GQAdonis/"]').evaluateAll((nodes) => nodes.map((node) => node.href));
  assert(links.some((link) => /[a-f0-9]{40}.*evidence/.test(link)), 'Evidence must link a preserved commit');
});
Then('no local asset request or browser runtime error has failed', function () {
  assert.deepEqual(this.errors, []);
});
When('a reader opens the getting-started deep link with a phone viewport', async function () {
  await this.page.setViewportSize({ width: 390, height: 844 });
  const response = await this.page.goto(origin + this.site.prefix + 'getting-started/', { waitUntil: 'networkidle' });
  assert.equal(response.status(), 200);
  await this.page.getByRole('heading', { name: 'Getting started', exact: true, level: 1 }).waitFor();
});
Then('the page explains a pinned checkout instead of an unpublished registry release', async function () {
  const text = await this.page.locator('main').innerText();
  assert.match(text, /pinned checkout/i);
  assert.match(text, /path\s*=|git checkout/);
  assert.match(text, /not.*(?:crates.io|registry)|unpublished/i);
});
Then('the navigation is usable with the keyboard', async function () {
  const toggle = this.page.getByRole('button', { name: 'Toggle navigation bar' });
  let toggleReached = false;
  for (let attempt = 0; attempt < 30; attempt++) {
    await this.page.keyboard.press('Tab');
    if (await toggle.evaluate((element) => document.activeElement === element)) { toggleReached = true; break; }
  }
  assert(toggleReached, 'Navigation toggle must be reachable by Tab');
  await this.page.keyboard.press('Enter');
  const compatibility = this.page.locator('.navbar-sidebar__item:not([inert])').getByRole('link', { name: 'Compatibility', exact: true });
  await compatibility.waitFor({ state: 'visible' });
  let linkReached = false;
  for (let attempt = 0; attempt < 30; attempt++) {
    await this.page.keyboard.press('Tab');
    if (await compatibility.evaluate((element) => document.activeElement === element)) { linkReached = true; break; }
  }
  assert(linkReached, 'Active navigation link must be reachable by Tab');
  await this.page.keyboard.press('Enter');
  await this.page.getByRole('heading', { name: 'Compatibility', exact: true, level: 1 }).waitFor();
  assert(this.page.url().startsWith(origin + this.site.prefix));
});
Then('the page has no horizontal overflow', async function () {
  const dimensions = await this.page.evaluate(() => ({ width: document.documentElement.clientWidth, content: document.documentElement.scrollWidth }));
  assert(dimensions.content <= dimensions.width + 1, JSON.stringify(dimensions));
  assert.deepEqual(this.errors, []);
});
When('a reader opens the SDK page', async function () {
  const response = await this.page.goto(origin + this.site.prefix + 'sdk/', { waitUntil: 'networkidle' });
  assert.equal(response.status(), 200);
});
Then('both Behave and pytest-bdd are identified as unverified adapter tracks', async function () {
  const text = await this.page.locator('main').innerText();
  assert.match(text, /Behave/); assert.match(text, /pytest-bdd/);
  assert.match(text, /not.*(?:implemented|verified|available)|unverified|proposed/i);
});
Then('the page does not offer an npm or Python package installation as available', async function () {
  const text = await this.page.locator('main').innerText();
  assert.match(text, /not.*(?:published|available)|unpublished|no.*published/i);
  const code = await this.page.locator('main pre').allTextContents();
  assert(!code.some((item) => /(?:npm install|pip install)/.test(item)));
  assert.deepEqual(this.errors, []);
});
When('a reader opens an unknown documentation path', async function () {
  const response = await this.page.goto(origin + this.site.prefix + 'missing-documentation-page/', { waitUntil: 'networkidle' });
  assert.equal(response.status(), 404);
});
Then('the built not-found page is shown with a route back to the fork documentation', async function () {
  await this.page.getByRole('heading', { name: 'Page Not Found', exact: true }).waitFor();
  await this.page.locator('.navbar__brand').click();
  await this.page.getByRole('heading', { level: 1, name: this.site.heading, exact: true }).waitFor();
});
Given('an isolated copy of the {string} documentation source', async function (name) {
  this.site = sites[name]; assert(this.site);
  this.originalSource = await inventory(this.site.root, new Set(['node_modules', 'build', '.docusaurus']));
  this.originalBuild = await inventory(this.site.build);
  this.scratch = await mkdtemp(join(evidence, name + '-broken-link-'));
  for (const item of ['docs', 'src', 'package.json', 'package-lock.json', 'docusaurus.config.js', 'sidebars.js']) {
    await cp(join(this.site.root, item), join(this.scratch, item), { recursive: true });
  }
  const installed = await command(this.scratch, ['npm', 'ci', '--ignore-scripts', '--no-audit', '--no-fund'], this.id + '-isolated-install');
  assert.equal(installed.code, 0, 'Isolated control dependencies must install before mutation');
  const baseline = await command(this.scratch, ['npm', 'run', 'build'], this.id + '-isolated-baseline', { DOCS_BASE_URL: this.site.prefix });
  assert.equal(baseline.code, 0, 'Unmodified isolated control must build before introducing a broken link');
});
When('an author adds an internal link to a missing page', async function () {
  const intro = join(this.scratch, 'docs/intro.md');
  await writeFile(intro, await readFile(intro, 'utf8') + '\n[Broken control](./missing-documentation-target.md)\n');
});
Then('the same production build fails and identifies the missing route', async function () {
  const result = await command(this.scratch, ['npm', 'run', 'build'], this.id + '-broken-link-control', { DOCS_BASE_URL: this.site.prefix });
  assert.notEqual(result.code, null, 'A killed build is not a valid negative control');
  assert.notEqual(result.code, 0, 'Broken internal link incorrectly accepted');
  assert.match(result.stdout + result.stderr, /missing-documentation-target/);
});
Then('the original source and build remain unchanged', async function () {
  assert.deepEqual(await inventory(this.site.root, new Set(['node_modules', 'build', '.docusaurus'])), this.originalSource);
  assert.deepEqual(await inventory(this.site.build), this.originalBuild);
});

Then('the getting-started page has no horizontal overflow', async function () {
  const dimensions = await this.page.evaluate(() => ({ width: document.documentElement.clientWidth, content: document.documentElement.scrollWidth }));
  assert(dimensions.content <= dimensions.width + 1, JSON.stringify(dimensions));
});
Given('an evidence directory already contains preserved artifact bytes', async function () {
  this.scratch = await mkdtemp(join(evidence, 'retained-artifacts-'));
  // Deliberate fixture bytes, never represented as an actual successful run.
  await writeFile(join(this.scratch, 'messages.ndjson'), '{"acceptanceFixture":"preserve these bytes"}\\n');
  await writeFile(join(this.scratch, 'boundary-receipt.json'), '{"acceptanceFixture":true,"actualRun":false}\\n');
  this.retained = await inventory(this.scratch);
});
When('the documentation boundary is launched with that directory', async function () {
  this.reuseResult = await command(siteRoot, [process.execPath, 'acceptance/run.mjs'], this.id + '-reuse-refusal', { DOCS_EVIDENCE: this.scratch });
});
Then('it refuses before starting another scenario run', function () {
  assert.notEqual(this.reuseResult.code, 0);
  assert.match(this.reuseResult.stdout + this.reuseResult.stderr, /Refusing to overwrite existing evidence/);
});
Then('all preserved artifact bytes remain unchanged', async function () {
  assert.deepEqual(await inventory(this.scratch), this.retained);
});
