# Closure packet — phase-46-native-sdk

Disposition: **CLOSED** (budget-exhausted). This packet is a derived view of
the bound contract (sha256:a48388a624c00318a3afe449bcf7415f6f4a9a516a63b0a43742ee3c75a15dc0) and
`boundary-results.json` (sha256:10ac7bcb79f97d6622d1600f65cad332cf83649da4d062f63116ff28a9751be8); the canonical KBD disposition is authoritative.

## What works, and for whom

- SDK-001 — Rules, outlines, both argument orders and Unicode retain source locations and identities (for Application or verification author)
- SDK-002 — Literal backticks in steps/tables/docstrings remain content; declaration tags remain tags (for Application or verification author)
- SDK-003 — Valid featureless input yields no Pickles (for Application or verification author)
- SDK-004 — Typed SOURCE_ERROR retains the exact original URI; a following valid request succeeds (for Application or verification author)
- SDK-005 — Capabilities identify compiler and rerun operations and do not advertise foreign execution (for Application or verification author)
- SDK-006 — Retain every attempt and original non-PASSED scenario/Examples-row selectors; keep run_success independent, including failed runs with no selected cases (for Application or verification author)
- SDK-007 — Missing references or missing TestRunFinished remain visible errors; a finished run may retain interrupted attempts with completed=false and UNKNOWN (for Application or verification author)
- SDK-008 — No selected cases means None/empty plan and cannot mean run everything (for Application or verification author)
- SDK-009 — Namespaced extension returns its real result without overriding built-ins (for Application or verification author)
- SDK-010 — Local npm archive and Python wheel execute native entry points from fresh directories; a real external TypeScript consumer imports the public declarations, compiles and executes inside this same phase-end BDD scenario (for Application or verification author)
- SDK-011 — Different URIs, parse failures and run IDs cannot leak across requests (for Application or verification author)

## Under which conditions

- environment: Initial behavioral certification target: Darwin arm64, Node26.5.0, CPython3.11.3, Rust1.88.0
- SDK-001 real collaborator: Existing SourceGraph and rerun Collector
- SDK-001 real collaborator: Installed Node native addon and Python extension
- SDK-001 real collaborator: External Rust/TypeScript/Python consumers
- SDK-001 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-002 real collaborator: Existing SourceGraph and rerun Collector
- SDK-002 real collaborator: Installed Node native addon and Python extension
- SDK-002 real collaborator: External Rust/TypeScript/Python consumers
- SDK-002 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-003 real collaborator: Existing SourceGraph and rerun Collector
- SDK-003 real collaborator: Installed Node native addon and Python extension
- SDK-003 real collaborator: External Rust/TypeScript/Python consumers
- SDK-003 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-004 real collaborator: Existing SourceGraph and rerun Collector
- SDK-004 real collaborator: Installed Node native addon and Python extension
- SDK-004 real collaborator: External Rust/TypeScript/Python consumers
- SDK-004 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-005 real collaborator: Existing SourceGraph and rerun Collector
- SDK-005 real collaborator: Installed Node native addon and Python extension
- SDK-005 real collaborator: External Rust/TypeScript/Python consumers
- SDK-005 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-006 real collaborator: Existing SourceGraph and rerun Collector
- SDK-006 real collaborator: Installed Node native addon and Python extension
- SDK-006 real collaborator: External Rust/TypeScript/Python consumers
- SDK-006 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-007 real collaborator: Existing SourceGraph and rerun Collector
- SDK-007 real collaborator: Installed Node native addon and Python extension
- SDK-007 real collaborator: External Rust/TypeScript/Python consumers
- SDK-007 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-008 real collaborator: Existing SourceGraph and rerun Collector
- SDK-008 real collaborator: Installed Node native addon and Python extension
- SDK-008 real collaborator: External Rust/TypeScript/Python consumers
- SDK-008 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-009 real collaborator: Existing SourceGraph and rerun Collector
- SDK-009 real collaborator: Installed Node native addon and Python extension
- SDK-009 real collaborator: External Rust/TypeScript/Python consumers
- SDK-009 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-010 real collaborator: Existing SourceGraph and rerun Collector
- SDK-010 real collaborator: Installed Node native addon and Python extension
- SDK-010 real collaborator: External Rust/TypeScript/Python consumers
- SDK-010 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector
- SDK-011 real collaborator: Existing SourceGraph and rerun Collector
- SDK-011 real collaborator: Installed Node native addon and Python extension
- SDK-011 real collaborator: External Rust/TypeScript/Python consumers
- SDK-011 real collaborator: Retained official Gherkin43 and actual pinned JS13.3 formatter/collector

## Limits

- SDK-001: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-001: No foreign step execution or framework adapters
- SDK-001: No registry publication
- SDK-001: Internal review exact model unknown; no cross-model certification
- SDK-002: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-002: No foreign step execution or framework adapters
- SDK-002: No registry publication
- SDK-002: Internal review exact model unknown; no cross-model certification
- SDK-003: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-003: No foreign step execution or framework adapters
- SDK-003: No registry publication
- SDK-003: Internal review exact model unknown; no cross-model certification
- SDK-004: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-004: No foreign step execution or framework adapters
- SDK-004: No registry publication
- SDK-004: Internal review exact model unknown; no cross-model certification
- SDK-005: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-005: No foreign step execution or framework adapters
- SDK-005: No registry publication
- SDK-005: Internal review exact model unknown; no cross-model certification
- SDK-006: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-006: No foreign step execution or framework adapters
- SDK-006: No registry publication
- SDK-006: Internal review exact model unknown; no cross-model certification
- SDK-007: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-007: No foreign step execution or framework adapters
- SDK-007: No registry publication
- SDK-007: Internal review exact model unknown; no cross-model certification
- SDK-008: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-008: No foreign step execution or framework adapters
- SDK-008: No registry publication
- SDK-008: Internal review exact model unknown; no cross-model certification
- SDK-009: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-009: No foreign step execution or framework adapters
- SDK-009: No registry publication
- SDK-009: Internal review exact model unknown; no cross-model certification
- SDK-010: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-010: No foreign step execution or framework adapters
- SDK-010: No registry publication
- SDK-010: Internal review exact model unknown; no cross-model certification
- SDK-011: Darwin arm64 Node26.5/Python3.11 initial host only
- SDK-011: No foreign step execution or framework adapters
- SDK-011: No registry publication
- SDK-011: Internal review exact model unknown; no cross-model certification
- unknown: Other runtime/platform behavior
- unknown: Public package names and ownership
- unknown: Foreign execution and Behave/pytest-bdd adapter compatibility

## What remains

- nothing: every scenario passed

## Pre-authorization runner artifacts

- no runnerOutputGlobs declared in the contract; scan not possible

This scan is passive evidence (VLBV 04, 10): it reports and never blocks.

## Closure states

| State | Value |
|---|---|
| Implementation complete | true |
| Behavior accepted | true |
| Release eligible | true |
| Release authorized | false (a separate owner decision) |

Method: VLBV.
Executed by: cucumber-rs0.23 harness=false language_sdk with source-aware Messages + installed native Rust/Node/Python consumers phase46 B5repair2; Rust1.88.0 Node26.5.0 CPython3.11.3 TypeScript6.0.3 Darwinarm64 (internal Codex exact deployment unknown).
