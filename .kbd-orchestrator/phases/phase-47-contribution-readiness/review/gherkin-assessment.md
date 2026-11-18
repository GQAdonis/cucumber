# Phase47 independent Gherkin assessment review

Reviewer: `/root/gherkin_contribution_review`, internal Codex agent; exact model/deployment UNKNOWN. Date:2026-11-18. Read-only assessment of the proposed parser repair boundary and retained CI diagnosis; no external review transmission. This review writes only this report. No production edits, builds, tests, imports, linting or canonical state changes.

## Reviewed inputs

- `assessment.md`: SHA256 `ccb5b6cb27569d87386f536c48e63b9febeb3ad09d6ce6079795dec2c12c880b`
- `scenario-candidates.md`: SHA256 `842e34ae1ce142e0c8c0d5c069f62bec9295510b90a103da17f32ed81bd11af1`

Also inspected Gherkin source, its dedicated BDD scenarios/harness and existing discovery harness, the original production diff, and previously retrieved failed CI44298273420 logs. The report does not convert historical passing73/241 evidence into current merge readiness.

## Verdict

The proposal identifies the observed parser regression accurately and is suitable to continue specification/calibration. It is **not yet an executable accepted contract**: exact cases/entry points, packet counts, provenance and budgets are expressly unbound. No implementation or verification authority is inferred from successor signing; no individual owner adoption is asserted. No new definite parser correctness defect was established in this assessment-only pass.

## Required precision before adoption/generation

1. **CR47-G01 — Preserve independent policy selection (outcome1).** Define both `Default`/`GherkinEnv::new` and `new_latest` with legacy table semantics: latest vocabulary alone must not silently opt into43 tables. Contrast explicit `TableSemantics::Gherkin43`. Include the actual failing `Examples` escape (`| \     |`) and a step table; preserve recognized escaped newline/pipe/backslash and adjacent following-step identity. The existing six literal-escape BDD cases currently call the default parser, so their policy selection must be reconciled with the intended legacy repair rather than simply changing assertions. Dual argument-order acceptance is a separate delivered behavior and should not be removed to repair escapes.
2. **CR47-G02 — Keep error changes private (outcome2).** Do not change public `ParseFileError` variants/signatures to silence `result_large_err`. Bind exact classic diagnostic text and structured position/path for a malformed supplied-source case, plus the additive Markdown diagnostic and a following valid parse. Compare before/after retained observations where formatting equivalence is promised; an assertion that merely sees `Err` is insufficient. No blanket lint suppression or swallowed diagnostics.
3. **CR47-G03 — Vendor correspondence is source plus behavior (outcome3).** Name the production file set and manifest/hash identity, then exercise both parsers under the same policy/source inputs, including featureless input and a malformed case. The negative control should corrupt a disposable comparison copy only and prove detection; never alter the actual vendor to manufacture a passing check. Synchronize production source without rewriting unrelated Cargo/release configuration.
4. **CR47-G04 — Separate observed CI cause from discovery concern (outcome9).** CI stopped at the legacy lib assertion; recursive discovery is a separate static concern. Existing `tests/cucumber.rs` intentionally has no registered steps and no fail-on-skipped, so do not impose new failure semantics on that mature harness to satisfy a new test. Isolate the dedicated compatibility feature/harness scope additively; preserve packaged fixture inclusion if paths move. Bind nonzero expected case/step totals to the focused acceptance entry point, and prove absent/wrong selection cannot be counted as success. Preserve original failed CI evidence.
5. **CR47-G05 — Bound the affected packet (outcome10).** Name the existing parser73/241 baseline and the specific consumer corpus, lexical/document/Markdown, Messages/rerun and SDK packets actually affected. The historical Gherkin-only harness does not contain standalone Document/Markdown/lexical acceptance, so the consumer-side evidence must remain explicit. No claim that one parser harness certifies all new APIs, all feature combinations or universal Gherkin43 conformance.

These are specification requirements, not authorization to add new feature scope or execute checks. The exact command/count decisions belong in the reviewed contract before production work.

## Maintainability and process

Formatting and removal of the two old Step Display borrows are mechanical corrections; preserve existing CI policy. Compact private error storage without public API churn. The unchanged CI runs unit suites automatically when a PR update is pushed; the assessment correctly distinguishes those remote runs from locally authorized phase-end BDD. That distinction must be explicit in the final contract and evidence rather than relabeling unit output as BDD.

Pre-register the existing terminal lifecycle stages before closure in the supported runtime; this avoids repeating phase46's immutable missing-Reflect gap. Do not reopen phase46 or edit generated state. Source commits should remain local through unfinished implementation; published contribution status must not become ready or merged until the adopted proof and actual required checks succeed.

## Limits and disposition

No certification of Cucumber codegen, dependency minimums, book toolchain causality or foreign execution is provided by this Gherkin-focused review. Those outcomes require the other assigned source analysis and concrete contract entries. The finite contribution repair is appropriate; foreign execution, framework adapters and registry publication remain outside it. All five items above remain specification actions for the parent; none has been represented as implemented or verified.
