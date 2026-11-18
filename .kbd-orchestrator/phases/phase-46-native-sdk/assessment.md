# Assessment: native source and evidence SDK

2026-11-18. Source inspection and existing evidence only; no new runtime proof.

## Preserved baseline

Cucumber0.23 and maintained Gherkin0.16 have through45 focused BDD against pinned
Cucumber.js13.3.0, Gherkin43.0.0 and Messages34.2.1/35. Latest Rust1.88 runs:
87/348 primary,106/460 affected,73/241 sibling. Both origins now retain
foundation/rust-bdd-sdk: Cucumber6e4753fc0783038bb388de1b4d76055edc697b8f,
Gherkin efb91e8bb5a7d59a717f88c05d1c06ec5d06a819.
No main/release-tag trigger ran. Historical BDD is not retroactive KBD closure.

## Existing seams and actual gaps

SourceGraph owns source compilation and Collector owns rerun semantics. SDKs must
call those implementations, preserving original source and every attempt.
No public SDK or native TS/Python extension exists. Core lib forbids unsafe;
ABI machinery belongs in separate adapter crates.

Runtime steps are function pointers returning LocalBoxFuture. World construction
is static. Foreign closures need captured registration and per-run factory seams;
a catch-all handler/process-global session would falsify ambiguity or isolation.
Rust future cancellation cannot terminate arbitrary host work; late completion
and cleanup need a contract. Existing process-global panic-hook replacement also
requires independent-run coordination. These are later real integration work.

Root workspace/codegen and vendored parser must stay intact. Separate nested
SDK/adapter workspaces are feasible. No Docusaurus exists; Cucumber already has
mdBook and a gh-pages deployer that must not be overwritten.

## Proposed first boundary

Shared safe Rust SDK + NAPI-RS/PyO3 wrappers expose compiler/AST/Pickle and rerun,
proved through packages installed outside checkout. This scope does not depend
on which Python framework is selected. Dynamic registration/factory and actual
foreign callbacks follow, retaining the complete requested programme.
This ordering is proposed for calibration, not adopted or a parity claim.

## Decisions and limitations

Python baseline remains Behave1.3.3 vs pytest-bdd9.0.1 vs named alternative.
Public names/scopes/owners/publication scope and docs hosting remain unresolved.
Observed host: Darwin arm64, Node26.5.0, Python3.11.3; no other platform is certified.
Rust1.88 remains core minimum. Candidate dependencies are source-verified only.
No newly requested SDK, bindings, sites or packages exist or are published yet.

## Recalled lessons

"Boundary gates must launch the packaged artifact": install actual npm tarball
and Python wheel outside checkout and call their native production entry points.
"Preserve production evidence in dated review folders": retain every original
boundary and failure receipt separately.
"Discover test environment state instead of encoding checkout assumptions":
record actual interpreter/ABI/platform and refuse incompatible artifacts.
"Ask once at phase boundary for operator-only actions": reuse push authorization;
only new calibration and unresolved publication decisions need new decisions.
Prior-context Knowledge gaps: none recorded. New task-specific questions above
are not resolved by recalled agent lessons.

Planning-artifact review is pending. Final independent code audit occurs after
implementation/behavior proof and before upstream issues/PRs. Neither codebase
is claimed clean or fully parity-certified.
