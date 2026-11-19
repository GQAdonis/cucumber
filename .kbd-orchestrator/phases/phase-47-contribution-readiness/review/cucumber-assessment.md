# Cucumber contribution-readiness assessment review

Date: 2026-11-18. Reviewer: `/root/cucumber_contribution_review`, an independent internal Codex agent; exact model/deployment identity is unavailable. Source/document and retained-CI-log review only. No build, test, import, linter, executable validation probe, source modification or external review transmission was performed. This report is not the post-implementation audit and does not certify readiness to merge.

## Disposition

**PASS for assessment-to-specification preparation, with the binding requirements below.** The assessment correctly distinguishes the signed successor/assessment authorization from phase-specific contract adoption. It retains actual failures, marks the minimal-graph correction and book causality unknown, preserves mature workflows and recognizes local BDD-only verification. None of the ten proposed outcomes is falsely represented as adopted or proved. No production generation, behavioral execution, ready transition or merge is authorized by this review.

## Requirements to resolve before adoption/implementation

| ID | Material question or limitation | Required specification decision |
| --- | --- | --- |
| CR47-A01 | Outcome7 currently says a fresh Rust1.88 consumer resolves the supported graph. A normal latest-compatible graph can pass while the observed minimal-versions graph still fails. | Explicitly retain the existing minimal-resolution boundary (`cargo +nightly update -Z minimal-versions`) and Rust1.88 affected-path execution inside the accepted phase-end BDD scenario. Record resolver/toolchain identity, actual resolved graph, exact fixture/command and independent success/failure criteria. Determine corrected minimum constraints by source analysis before selecting them; do not guess a version or remove the mature job. |
| CR47-A02 | Outcome8 is appropriately a proposed outcome, but the book error is not yet attributed to this patch. Logs show a successful build, then mdBook0.5.4/Rust1.100.0 cannot locate several crates. | Establish the source/configuration cause and supported consumer entry point. Preserve the unknown until supported evidence resolves it. The acceptance must prove actual example linkage/execution; merely checking that `.rlib` files exist or changing documentation text is insufficient. Any existing upstream/tool defect must be distinguished from our regression. Do not silently rewrite the Makefile/workflow to avoid the failing path. |
| CR47-A03 | “Existing remote check policy” and local BDD-only constraints can conflict if the specification quietly introduces local replicas of unit/lint suites. | State separately: local whole-phase BDD commands and their real consumer/build operations; permitted source-formatting edits; existing automatically triggered remote required checks. No local generic/unit suite or early lint/typecheck/build. Remote check success is a distinct readiness gate, not a substitute for BDD proof. Push only after the completed local boundary as proposed; do not weaken or disable mature checks. |
| CR47-A04 | Outcome6 covers missing `@cucumber/query`, the first observed failure, but other new acceptance targets also use locked JavaScript oracle packages. | Inventory all external collaborators actually required by the selected existing entry points. Bind package directories, locks, executable versions, installation/cache/network behavior and missing-collaborator failure semantics. A developer's pre-existing `node_modules` directory cannot satisfy fresh CI proof. Do not skip missing oracles or equate an availability preflight with accepted behavior. |
| CR47-A05 | Outcome4's “supported public feature combinations” and outcome10's “complete affected packet” do not yet bound cost or coverage. | Enumerate the feature matrix, exact commands/scenario identities, counts/nonzero guards, source/native artifact identities and negative controls. Include the no-Messages configurations that failed with `-D warnings`. Native SDK proof must remain installed-artifact proof on the adopted host, not silently broaden into every platform implied by metadata. Set finite cumulative budgets and repair limits before implementation. |
| CR47-A06 | Three existing codegen token expectations are stale because intended generated registrations gained DefinitionOptions. Updating them alone is implementation-shaped evidence. | Preserve and reconcile existing assertions without deleting or weakening them, while the local accepted BDD exercises generic/custom-init Worlds and actual options/context behavior. Do not add a unit suite or run the existing one locally under another label. Remote mature codegen checks remain distinct. |

The formatting and initial17 codegen clippy diagnostics are observed, but later core lint findings may be masked by that first failure. The proposed whole-delivered-scope audit must remain an actual independent post-proof gate with material corrections inside authorized repair bounds; this assessment review is not that gate.

## Scope and provenance observations

The ten candidates remain traceable to real parser/core/CI readiness failures and preservation requirements. Keeping foreign execution, framework adapters, public registry operations, upstream merging and unrelated release changes out of this repair phase is appropriate. Safe fork-main merging still requires actual green checks, exact head/base identity, the owner's merge authority and preserved Pages deployment branches.

The original `docs/compatibility/readiness/PROPOSAL.md` contains historical unsigned/not-activated wording. The parent is adding a superseding current-state note linking the exact successor authorization; preserve that history without presenting it as the current gate. No individual calibration answer should be inferred from signing the successor.

Retained failure evidence reviewed previously: Cucumber CI44298276111, including five no-Messages dead-code errors;14 dry-run failures from absent Query package;three codegen expectation mismatches;17 initial codegen lint diagnostics; formatting diffs;74 ICU/Yoke minimum-graph errors; and the book linker/search-path failure. No new execution was used to create this review.

## Reviewed source identities

- `assessment.md`: `ccb5b6cb27569d87386f536c48e63b9febeb3ad09d6ce6079795dec2c12c880b`
- `scenario-candidates.md`: `842e34ae1ce142e0c8c0d5c069f62bec9295510b90a103da17f32ed81bd11af1`
