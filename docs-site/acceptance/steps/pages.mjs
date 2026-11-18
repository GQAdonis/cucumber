import { BeforeAll, AfterAll, Before, After, Given, When, Then, setDefaultTimeout } from '@cucumber/cucumber';
import { chromium } from 'playwright-core';
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

setDefaultTimeout(120_000);
assert(process.env.PAGES_EVIDENCE, 'PAGES_EVIDENCE must identify a fresh evidence directory');
const evidence = resolve(process.env.PAGES_EVIDENCE);
const exec = promisify(execFile);
const api = async (path) => JSON.parse((await exec('gh', ['api', path], { maxBuffer: 8 * 1024 * 1024 })).stdout);
let browser;
let sequence = 0;
BeforeAll(async () => {
  browser = await chromium.launch({ channel: process.env.DOCS_BROWSER_CHANNEL || 'chrome', headless: true });
  await writeFile(resolve(evidence, 'environment.json'), JSON.stringify({ node: process.version, browser: browser.version(), observedAt: new Date().toISOString() }, null, 2));
});
Before(async function () {
  this.id = String(++sequence).padStart(2, '0');
  this.context = await browser.newContext();
  this.page = await this.context.newPage();
  this.errors = [];
  this.pages = [];
  this.assets = [];
  this.page.on('pageerror', error => this.errors.push(String(error)));
  this.page.on('requestfailed', request => this.errors.push(request.url() + ': ' + request.failure()?.errorText));
  this.page.on('response', response => {
    if (response.url().startsWith(this.url || 'https://gqadonis.github.io/')) {
      if (response.status() >= 400) this.errors.push(response.status() + ' ' + response.url());
      if (/\.(?:js|css)(?:\?|$)/.test(response.url())) this.assets.push(response.url());
    }
  });
});
After(async function ({ result }) {
  await writeFile(resolve(evidence, this.id + '-observation.json'), JSON.stringify({ status: result?.status, project: this.project, pages: this.pages, assets: this.assets, errors: this.errors }, null, 2));
  await this.page?.screenshot({ path: resolve(evidence, this.id + '-page.png'), fullPage: true });
  await this.context?.close();
});
AfterAll(async () => browser?.close());
Given('the successful Pages deployment for {string} is available', async function (project) {
  assert(['cucumber', 'gherkin'].includes(project));
  this.project = project;
  this.url = `https://gqadonis.github.io/${project}/`;
  const root = `repos/GQAdonis/${project}`;
  const pages = await api(root + '/pages');
  const branch = await api(root + '/branches/foundation%2Frust-bdd-sdk');
  const runs = await api(root + '/actions/workflows/docs-pages.yml/runs?branch=foundation%2Frust-bdd-sdk&per_page=10');
  const run = runs.workflow_runs.find(run => run.conclusion === 'success');
  assert(run, 'The foundation branch must have a successful documentation workflow');
  const comparison = await api(root + `/compare/${run.head_sha}...${branch.commit.sha}`);
  await writeFile(resolve(evidence, this.id + '-deployment-comparison.json'), JSON.stringify({ deployedSha: run.head_sha, branchSha: branch.commit.sha, comparison }, null, 2));
  assert(['identical', 'ahead'].includes(comparison.status), 'Deployed documentation must be an ancestor of the current branch');
  assert.equal(comparison.behind_by, 0, 'Current branch must contain the deployed source');
  assert(Array.isArray(comparison.files), 'GitHub must report changed files');
  assert(comparison.files.length < 300, 'GitHub comparison may truncate at 300 files; documentation freshness cannot be proven');
  const isDocumentation = path => path?.startsWith('docs-site/') || path === '.github/workflows/docs-pages.yml';
  assert(!comparison.files.some(file => isDocumentation(file.filename) || isDocumentation(file.previous_filename)), 'Documentation or its deployment workflow changed after the latest successful deployment');
  const jobs = await api(root + `/actions/runs/${run.id}/jobs`);
  assert(jobs.jobs.some(job => job.name === 'build' && job.conclusion === 'success'));
  assert(jobs.jobs.some(job => job.name === 'deploy' && job.conclusion === 'success'));
  assert.equal(pages.build_type, 'workflow');
  assert.equal(pages.html_url.toLowerCase(), this.url);
  this.repository = await api(root);
  await writeFile(resolve(evidence, this.id + '-github.json'), JSON.stringify({ pages, branch, run, jobs, repository: { full_name: this.repository.full_name, homepage: this.repository.homepage } }, null, 2));
});
async function visit(world, url) {
  const response = await world.page.goto(url, { waitUntil: 'networkidle' });
  assert.equal(response.status(), 200, url);
  assert(world.page.url().startsWith(world.url));
  const text = await world.page.locator('body').innerText();
  assert.match(text, /GQAdonis fork/);
  assert.match(await world.page.getByRole('contentinfo').innerText(), /Not endorsed by the upstream/);
  world.pages.push({ url: world.page.url(), status: response.status(), heading: await world.page.getByRole('heading', { level: 1 }).innerText() });
}
When('a reader opens its public home and getting-started deep link', async function () {
  await visit(this, this.url);
  await visit(this, this.url + 'getting-started/');
});
Then('both pages identify the independent GQAdonis fork', function () {
  assert.equal(this.pages.length, 2);
  assert.equal(this.pages[0].heading, this.project === 'cucumber' ? 'Cucumber for Rust' : 'Gherkin for Rust');
  assert.equal(this.pages[1].heading, 'Getting started');
});
Then('the public pages load their local assets without browser errors', function () {
  assert(this.assets.some(url => url.endsWith('.js')), 'Expected actual public JavaScript');
  assert(this.assets.some(url => url.endsWith('.css')), 'Expected actual public stylesheet');
  assert.deepEqual(this.errors, []);
});
When('a reader follows the repository About website', async function () {
  assert.equal(this.repository.homepage?.toLowerCase(), this.url);
  await visit(this, this.repository.homepage);
});
Then('it points to the same HTTPS Pages site and serves the fork documentation', function () {
  assert.equal(this.pages.length, 1);
  assert.equal(this.pages[0].url.toLowerCase(), this.url);
  assert.deepEqual(this.errors, []);
});
