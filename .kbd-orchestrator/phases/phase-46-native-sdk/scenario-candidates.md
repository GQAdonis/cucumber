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

- Useful outcome: Typed SOURCE_ERROR retains the exact original URI; a following valid request succeeds.
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

- Useful outcome: Retain every attempt and original non-PASSED scenario/Examples-row selectors; keep run_success independent, including failed runs with no selected cases.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Actual pinned Cucumber.js13.3 rerun formatter for selection; original Messages and pinned EventDataCollector for full attempt history.
- False-positive control: Drop a failed attempt or replace original row with a synthetic line and reject.
- Alternative: selected for proposal; host-side semantics and mocked FFI rejected because they do not establish shared-core behavior.
- Next decision: accept boundary only if this case and control pass at complete phase end.

## SDK-007: Reject incomplete or inconsistent run evidence

- Useful outcome: Missing references or missing TestRunFinished remain visible errors; a finished run may retain interrupted attempts with completed=false and UNKNOWN.
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

- Useful outcome: Local npm archive and Python wheel execute native entry points from fresh directories; a real external TypeScript consumer imports the public declarations, compiles and executes inside this same phase-end BDD scenario.
- Observation: installed SDK entry point (external Rust consumer for SDK-009), captured results and artifact hashes.
- Truth source: Archive/binary hashes, fresh-process isolated installs, resolved facade/native paths and real results; Rust consumer records dependency provenance.
- False-positive control: Remove native artifact from a disposable install, launch another fresh host process; explicit load failure with no module cache, checkout injection, parser or subprocess fallback.
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

## Required before SDK contract adoption

Freeze a versioned shared request/result/error schema, including URI, dialect,
media type, IDs, attempt completion and independent run success. Define malformed
request and unsupported-version results across both native wrappers. Bind exact
retained fixture hashes and generator versions. Use deterministic IDs or a
bijective ID mapping, preserving all graph references; never normalize away URI,
source location, argument order or AST/Pickle relationships. Mutate captured
relationships as controls, not only deliberately wrong expected strings.
These acceptance-critical details remain prerequisites, not implementation.

## Review follow-up cases within the same frontier

SDK-006 also carries an original NDJSON attempt number 9007199254740993 through
both wrappers as the exact decimal string. Compare against the original literal,
not JavaScript JSON.parse or the formatter's precision-limited number. This is a
protocol-preservation boundary, not fabricated agreement with a rounded oracle.
SDK-010 records public declaration resolution and actual compiled TypeScript
consumer execution at phase end; plain JavaScript alone cannot prove TS usability.
SDK-005 follows the concrete validation-precedence examples in the contract
proposal; returning any error is insufficient. SDK-004 requires SOURCE_ERROR.uri.
