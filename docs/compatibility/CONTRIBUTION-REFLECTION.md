# Delivered foundation reflection and draft contribution review

2026-11-18. Owner explicitly requested reflection, preservation, fork-main drafts and upstream proposal issues followed by matching drafts. This supersedes the earlier hold on submissions; it authorizes no merge or registry publication.

## Cucumber outcome

Through45 delivers the version-pinned interoperability foundation: opt-in common step matching, source-faithful AST/Pickles, Messages, lifecycle/attachments, filtering/order/assignment and rerun planning. SDK46 adds the shared Rust compile/rerun/extension interface and installed native Node/TypeScript/Python transports. Foreign callbacks, Behave/pytest-bdd adapters, arbitrary JavaScript support files and universal parity are not delivered.

Evidence is retained at commit598f433: final SDK22/66; through45 root87/348 and affected106/460; parser73/241. Documentation local10/64 and public4/22 passed. No new behavior tests, unit suites, builds, imports, formatting or lint runs were performed for this contribution preparation. New branches retain identical production sources and harnesses; original evidence is historical, not an assertion that extraction was freshly executed.

## Independent review and disposition

Internal /root/cucumber_contribution_review sampled matching, timeout/lifecycle, attachments, assignment, SDK JSON validation, manifests and retained evidence against origin/main d958725. Core/Cargo/codegen spans51 files,+10990/-572 lines; this is not an exhaustive whole-program audit. SDK46 earlier independent reviews resolved the JSON token-kind defect and missing outer Messages evidence. No additional definite behavior defect was established by this bounded sample.

Draft limitations: existing rustfmt/clippy CI was not run locally; compressed source formatting remains a likely review concern. Do not disable upstream workflows or label this merge-ready. The vendored parser provides checkout portability, but registry packaging strips Cargo path dependencies: an appropriate upstream parser release/dependency update is required before publication. SDK artifact-specific license inventory, broader platforms and foreign execution remain separate gates.

## KBD reflection supplement

Phase46 remains CLOSED/PASS. Missing Reflect cannot be registered in an immutable closed phase; existing terminal bookkeeping transitions are permitted, new stage entry is not. A supported run-global DecisionRecorded supplement, sdk46-reflection-supplement, records the authored reflection without pretending to repair the stage. Receipt: evidence/sdk46-closure/reflection-supplement.txt. No canonical state files were edited, phase reopened or signature reused. A new successor requires its own signed start-successor manifest and phase-specific adoption; none was created or signed during this contribution milestone.

## Contribution structure and overlap

The fork-main draft preserves all delivered code, evidence and fork documentation. Upstream preparation excludes GQAdonis Pages/branding, KBD journals/signatures and bulk run output, retaining implementation, acceptance harnesses, fixture provenance and evidence links. Parser contribution precedes its Cucumber consumer. The Cucumber foundation remains a substantial integrated draft: maintainers should agree subdivision and dependency strategy before merge.

Cucumber PR391 remains open at5feb75d (single step-hook slots; our ordered/filterable hooks and reporting differ). PR405 remains open atd1f60a8 (cross-process sharding, absent here; our assignment is in-process). Reference existing Messages issue169, attachments256, Markdown309 and matching-validation378; do not imply independent discovery or duplicate generic feature requests.

No repository-local CONTRIBUTING/PR template or organization default contribution file was found for cucumber-rs; both GitHub community profiles report contributing=null. The Gherkin README links documentation for the separate cucumber/gherkin organization. Its global guide prohibits AI-authored issue/PR prose and requires human review; that is not configured as the cucumber-rs contribution policy. Our submissions must disclose AI assistance and cannot claim human review or upstream endorsement that did not occur.

## Next SDK proposal, not adopted

A next useful bounded phase is serial native foreign execution on the existing Rust runner: Node Promise callbacks, initially synchronous Python callbacks, owned per-attempt host Worlds, explicit matching/hook/attachment outcomes, timeout/late-resolution rejection and source-faithful Messages feeding the existing rerun SDK. Step function-pointer registrations and static World construction need additive owned-dispatch/factory seams. Preserve legacy APIs; no global host registry or second scheduler. Python asyncio, framework adapters, worker processes and publication remain separate proposals. No next-phase implementation or tests occurred.
