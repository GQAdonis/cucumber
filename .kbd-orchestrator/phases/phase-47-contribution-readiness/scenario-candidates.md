# Proposed contribution readiness outcomes

Actor: downstream Rust/SDK users and maintainers. Basis: actual CI failures and explicit preservation requirements. Reason now: blocked safe contribution completion. Likelihood: observed for failures, otherwise UNKNOWN. Mandatory: no bypass, no zero/skipped false pass, preserved source/evidence identity, no local unit suites. Decision: whether exact delivered scope can be ready and fork-main safely merged. All ten are proposed, not adopted.

1. Legacy parser rejects its historically invalid escape; explicit43 mode preserves the official literal value. Negative control switches mode and must differ.
2. Error messages/location remain intact across private error-storage changes; malformed sources still fail, no swallowed error.
3. Fork and vendored parser agree on legacy/43 documents and official corpus inputs; intentionally mismatched snapshot is rejected.
4. External consumer builds/runs meaningful scenarios under supported public feature combinations without warnings introduced by unused Messages internals; undefined steps still fail.
5. Derived generic/custom-init Worlds execute the intended definition options and attachment/completion contexts; legacy APIs remain usable.
6. Dry-run lifecycle oracle is actually installed/invoked through its documented package boundary; missing oracle fails explicitly rather than passing/skipping.
7. A fresh Rust1.88 consumer resolves the supported dependency graph and executes the affected feature path; incompatible graph is not presented as MSRV proof.
8. Existing book consumer examples build/link/execute through their supported production entry point; no changed or disabled workflow masks missing crates.
9. Each BDD entry point discovers only its supported acceptance scope, rejects skipped/zero-selected cases where required and retains original Messages/results.
10. Complete affected parser/core/SDK packet retains existing matching, Messages, rerun and installed native behavior after fixes; source/fixture identities and negative controls remain intact.

Counts, exact commands, budgets and repair limits must be bound in the assessed contract before implementation; these are proposals, not invented owner calibration. The new successor signature authorizes entry, not automatic adoption of these ten cases.

