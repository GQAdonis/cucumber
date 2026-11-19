# Fork GitHub Pages delivery

Published 2026-11-18 with Travis's explicit authorization for documentation-only
CI/CD and repository About website updates. This supersedes the earlier local-
only hosting restriction for these two documentation sites. Registry publishing
and unrelated build/release changes remain outside this authorization.

- Cucumber: https://gqadonis.github.io/cucumber/
- Gherkin: https://gqadonis.github.io/gherkin/

Both repository About website fields now contain their corresponding verified
HTTPS Pages address. GitHub creates/deploys each site through the dedicated
.github/workflows/docs-pages.yml. The first successful runs are
[Cucumber44292845914](https://github.com/GQAdonis/cucumber/actions/runs/44292845914)
and [Gherkin44292845898](https://github.com/GQAdonis/gherkin/actions/runs/44292845898).

Before changes, both Pages APIs returned404 and neither repository had an
environment. Actions was already enabled; it was not modified. Creating Pages
in workflow mode created the github-pages environment and its main branch rule.
Only the foundation/rust-bdd-sdk branch was additionally allowed for documentation
deployment; the existing main rule was preserved. No other security, branch-
protection, Rust CI, release or mdBook setting was changed.

The workflows trigger documentation-path pushes to foundation/rust-bdd-sdk,
install locked documentation dependencies, build Docusaurus3.10.2 with Node22.20.0
and upload/deploy the successful artifact with immutable official action pins.
The deploy job needs the build job. Broken links fail the build. Each site has
its correct repository path prefix. About was updated once through the authorized
repository API; no administrator credential was added to the workflow.

## Behavioral evidence

The complete local documentation boundary passed10 scenarios/64 steps plus both
global hooks, exit0. It covers both sites, mobile navigation/deep links, explicit
SDK/package limitations, isolated healthy-build/broken-link controls and refusal
to overwrite prior evidence. See
[evidence/docs-pages-20261118-local](evidence/docs-pages-20261118-local/).

After successful CI deployment and About updates, public browser acceptance
passed4 scenarios/22 steps, exit0: both home/deep-link routes, actual JS/CSS asset
loading without browser errors, fork/non-endorsement identity and both About
links. It retained deployment/API identity, screenshots, Messages and a nonzero
scenario receipt in
[evidence/docs-pages-20261118-public](evidence/docs-pages-20261118-public/).
The configuration/API receipts are in
[evidence/docs-pages-20261118-settings](evidence/docs-pages-20261118-settings/).

The public harness compares the deployed commit to the current branch. It permits
unrelated later SDK commits only when the comparison proves no documentation or
workflow changes; divergent history or a potentially truncated file comparison
fails closed. This is site delivery evidence, not SDK or whole-program parity.

The finite public boundary is authored in
../../docs-site/acceptance/features/pages.feature. From docs-site, supply a fresh
absolute PAGES_EVIDENCE directory and run node acceptance/pages-run.mjs after
both deployments and About links are ready. Do not overwrite earlier evidence.

## SDK documentation refresh

After final SDK46 proof and resolved scoped reviews, the completed documentation boundary ran again and passed10 scenarios/64 steps plus2 hooks, exit0. The retained fresh packet is [docs-pages-20261118-sdk-final-local](evidence/docs-pages-20261118-sdk-final-local/). The refresh deployed successfully in [run44295540606](https://github.com/GQAdonis/cucumber/actions/runs/44295540606) at commit d18c1520c7a18c661c848d896bc9247363f210e1. Final public-browser acceptance then passed4 scenarios/22 steps plus2 hooks, exit0, against both sites and About links. See [docs-pages-20261118-sdk-final-public](evidence/docs-pages-20261118-sdk-final-public/). Gherkin remained at its already-successful deployment24ab35f; no unnecessary redeployment was introduced.
