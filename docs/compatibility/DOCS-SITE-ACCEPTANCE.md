# Additive documentation acceptance boundary

Authority: Travis requested Docusaurus sites for both forks and README/docs
updates, with existing build/release processes preserved. The follow-up directs
continuing this unaffected documentation work while SDK adoption is unresolved.
This is a separately scoped documentation change; it does not adopt the SDK
contract or claim canonical KBD/VLBV certification.

Acceptance scenarios were authored before site implementation in
docs-site/acceptance/features/documentation.feature. Scope: both docs-only sites,
curated current-status/integration/evidence pages, fork branding and local
production artifacts. Real boundaries: Docusaurus production build, loopback HTTP,
installed Chrome, browser navigation and isolated broken-link negative controls.
Hosting, public domains, package publication, browser matrices and SDK behavioral
claims are excluded. No application runner or existing release workflow changes.

Candidate versions: Docusaurus3.10.2, React19.2.0, Cucumber.js13.3.0,
playwright-core1.56.1. The acceptance harness is independent from Rust build/test
workflows. It runs only after both sites and this finite nine-case boundary are
complete. Initial lock generation/install is part of that final packet; generated
lockfiles are retained. Exact commands, original outputs, screenshots, build
identities and cleanup receipts will be retained under compatibility evidence.

Positive observations: reader sees fork identity, accurate source-pinned
integration, bounded evidence, limits, SDK plans and working deep links.
Negative controls: deliberately broken internal links in disposable copies must
fail the same production builder; originals remain byte-identical. No simulated
server-side content or mock browser. Passing pages cannot establish SDK parity.

Known independent gate: phase46 SDK owner calibration/contract adoption remains
unresolved. Internal planning review does not meet external/cross-model
certification and is not the final post-implementation audit.

## Frozen first boundary command

From each docs-site directory, install its pinned direct packages and generate
its first retained package-lock.json with npm install --ignore-scripts --no-audit
--no-fund. Then from cucumber/docs-site run npm run acceptance with DOCS_EVIDENCE
set to a fresh absolute evidence directory. The focused BDD BeforeAll builds both
real sites under /preview/cucumber/ and /preview/gherkin/. Nine selected scenarios
exercise browser use and two deliberately broken-link builds. No broader suite.
Node26.5.0 and installed Google Chrome are the observed local runtime; no other
platform/browser is claimed. Lock and environment identities are retained.

## First fully exercised result — historical repair4

The repair4 boundary passed **9 scenarios / 56 steps**, plus both global
hooks, exit0. See [original BDD output](evidence/docs-sites-20261118-repair4/bdd.log)
and [finite-boundary receipt](evidence/docs-sites-20261118-repair4/boundary-receipt.json).
Both production builds succeeded under non-root paths. Seven real Chrome browser
scenarios passed; each of two independent control copies installed from its lock,
built successfully unmodified, then failed specifically on the injected broken
link. Original source/build identities remained unchanged; copies, browser and
server were cleaned. [Commands](evidence/docs-sites-20261118-repair4/commands.json),
[screenshots and environment](evidence/docs-sites-20261118-repair4/environment.json)
and [cleanup](evidence/docs-sites-20261118-repair4/cleanup.json) are retained.

Initial attempts remain unaltered: first selected zero scenarios; repair1 failed
SSR with forced ESM package mode; repair2 failed with forced CommonJS mode;
repair3 built both sites and exercised all nine but exposed footer/inert-menu
locator defects and invalid shared-dependency negative controls. None is passing
proof. Repair4 corrected all observed harness defects and passed the same full
finite boundary. No unit suite or unrelated Rust target ran.

Both sites use Docusaurus3.10.2 and React19.2.0 with committed lockfiles. Actual
acceptance host: Darwin arm64, Node26.5.0 and the Chrome version in environment.json.
This evidence establishes the local documentation boundary, not cross-browser,
public-hosting, SDK, package publication or canonical KBD/VLBV certification.
Established workflow hashes are retained unchanged in workflow-preservation.json.

## Latest result after independent review

Internal docs-only review found an evidence-overwrite defect and two coverage
limits. A new refusal scenario was authored first, followed by the guarded
launcher and actual Tab-navigation/Getting-started overflow correction. The
complete expanded boundary passed **10 scenarios / 64 steps**, both global hooks,
exit0, on the same documented runtime. See [original final BDD output](evidence/docs-sites-20261118-review-repair/bdd.log),
[finite receipt](evidence/docs-sites-20261118-review-repair/boundary-receipt.json),
[commands](evidence/docs-sites-20261118-review-repair/commands.json) and
[cleanup](evidence/docs-sites-20261118-review-repair/cleanup.json).

Seven scenarios use real browser behavior; two prove broken-link rejection after
healthy isolated builds; the tenth launches the actual boundary against existing
artifact fixtures and proves refusal without modification. The launcher owns its
log and claims evidence directories exclusively. Do not shell-redirect over a
prior run's files. Use a new DOCS_EVIDENCE directory for each authorized boundary.

The independent [review report](DOCS-SITE-REVIEW.md) records resolved findings and
scope limits. This documentation review does not complete the pending final
Rust/core/SDK/FFI audit or imply canonical KBD certification.
