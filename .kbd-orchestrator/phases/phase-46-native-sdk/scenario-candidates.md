# Phase46 scenario candidates — proposal

No case is adopted. All likelihoods are UNKNOWN. Actor: application or verification author. Basis: Travis's shared Rust/TypeScript/Python SDK request and existing Gherkin43/Messages contracts. Reason now: expose proven native behavior without duplicating semantics. All eleven cases are mandatory within this proposed boundary. See calibration-proposal.json; no owner verdicts are recorded.

## SDK-001: Compile plaintext source to faithful AST and Pickles in all three installed SDKs

- Useful outcome: Rules, outlines, both argument orders and Unicode retain source locations and identities.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Pinned Gherkin43 complete AST/Pickle fixture output.
- False-positive control: Mutate an expected cell or location; comparison must fail.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-002: Compile Markdown through the same native implementation

- Useful outcome: Literal backticks in steps/tables/docstrings remain content; declaration tags remain tags.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Pinned Gherkin43 Markdown corpus and retained phase45 cases.
- False-positive control: Misplaced or repeated argument must return a typed parse error.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-003: Compile empty/comment-only input without invented scenarios

- Useful outcome: Valid featureless input yields no Pickles.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Pinned Gherkin43 featureless fixtures.
- False-positive control: Inject a synthetic Feature/Pickle into expected output and reject.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-004: Recover after malformed input in the same host

- Useful outcome: Typed error and URI are visible; a following valid request succeeds.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Invalid official fixtures paired with a valid fixture.
- False-positive control: Invalid input cannot produce successful empty output.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-005: Discover the versioned implemented operations

- Useful outcome: Capabilities identify compiler and rerun operations and do not advertise foreign execution.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Adopted operation schema and actual exported entry points.
- False-positive control: Unknown version/operation and premature runtime execution are refused.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-006: Derive a lossless rerun plan from real Messages

- Useful outcome: Retain every attempt and original failed scenario/Examples-row selectors.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Actual pinned Cucumber.js13.3 rerun formatter plus original source graph.
- False-positive control: Drop a failed attempt or replace original row with a synthetic line and reject.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-007: Reject incomplete or inconsistent run evidence

- Useful outcome: Missing references and unfinished streams remain visible errors.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Native Collector state contract and retained phase44 fixtures.
- False-positive control: Truncate a genuine stream; no empty passing plan.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-008: Represent a completed passing run as no rerun

- Useful outcome: No selected cases means None/empty plan and cannot mean run everything.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Native LocalSelection contract.
- False-positive control: Bogus nonempty/all-source selection is rejected.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-009: Extend the safe SDK from an external Rust consumer

- Useful outcome: Namespaced extension returns its real result without overriding built-ins.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Consumer-owned extension behavior and reserved-name contract.
- False-positive control: Reserved builtin or duplicate registration is refused.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-010: Consume actual native package artifacts outside the checkout

- Useful outcome: Local npm archive and Python wheel execute their native entry points from fresh directories.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Captured archive identities, install commands and real native results.
- False-positive control: Remove native artifact from a disposable install; explicit load failure, no parser/subprocess fallback.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-011: Keep requests isolated in one host process

- Useful outcome: Different URIs, parse failures and run IDs cannot leak across requests.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Independent fixture identities and paired request sequence.
- False-positive control: Cross-associated IDs must fail or differ from the correct output.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## Boundaries and restoration

Real native core, actual extension loading, local artifact installation, original Messages and official fixtures. Registry publication, multi-platform certification and foreign callbacks/framework adapters remain later programme work. No simulated host parser. Disposable package installs and mutated controls are isolated under phase evidence and cleaned with retained receipts; originals remain unchanged. Stop at this finite frontier.
