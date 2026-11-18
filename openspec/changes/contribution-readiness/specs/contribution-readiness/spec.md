## ADDED Requirements

Status: proposed requirements only. Canonical adoption was denied before execution; these clauses describe the requested future contract, not an adopted or implemented capability. See docs/compatibility/readiness/ADOPTION-BLOCKER.md.

### Requirement: CR47-001 Preserve legacy table escape policy and explicit Gherkin43 behavior
The contribution SHALL satisfy this observable result: Legacy Default/new/new_latest reject the historical invalid Examples and step-table escape; explicit43 preserves official literal values, recognized escapes and following-step identity.

#### Scenario: CR47-001 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Legacy Default/new/new_latest reject the historical invalid Examples and step-table escape; explicit43 preserves official literal values, recognized escapes and following-step identity.

#### Scenario: CR47-001 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Switch only policy and require the expected semantic difference; corrupt one cell/step observation and reject.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-002 Preserve public parse errors across private storage repair
The contribution SHALL satisfy this observable result: Classic and Markdown malformed sources retain public variants, path, structured position and promised diagnostics; following valid input succeeds.

#### Scenario: CR47-002 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Classic and Markdown malformed sources retain public variants, path, structured position and promised diagnostics; following valid input succeeds.

#### Scenario: CR47-002 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Mutate path/location or suppress error; comparator rejects and valid recovery remains required.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-003 Keep parser fork and vendor production identity and behavior aligned
The contribution SHALL satisfy this observable result: Recorded production source/manifest correspondence and same-policy featureless/malformed/valid results agree between independently built fork/vendor consumers.

#### Scenario: CR47-003 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Recorded production source/manifest correspondence and same-policy featureless/malformed/valid results agree between independently built fork/vendor consumers.

#### Scenario: CR47-003 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Corrupt one byte in disposable comparison copy or one output observation; reject without mutating production source.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-004 Execute public feature-profile consumers without new warnings
The contribution SHALL satisfy this observable result: Eight explicit profiles compile and execute matched behavior under Rust1.88 with -Dwarnings; undefined-step control remains nonpassing.

#### Scenario: CR47-004 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Eight explicit profiles compile and execute matched behavior under Rust1.88 with -Dwarnings; undefined-step control remains nonpassing.

#### Scenario: CR47-004 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Undefined step produces no handler side effect and a visible nonpassing outcome; all-feature builds cannot substitute for no-Messages profiles.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-005 Execute derived generic and custom-init Worlds with intended options
The contribution SHALL satisfy this observable result: Generic/custom-init/legacy Worlds execute with intended DefinitionOptions and attachment/completion contexts.

#### Scenario: CR47-005 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Generic/custom-init/legacy Worlds execute with intended DefinitionOptions and attachment/completion contexts.

#### Scenario: CR47-005 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Remove expected metadata or misassociate attachment scope in copied observation and require rejection.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-006 Invoke locked dry-run lifecycle oracles from a fresh package boundary
The contribution SHALL satisfy this observable result: Actual dry_run acceptance invokes pinned Query/Messages collaborators without ambient node_modules dependency.

#### Scenario: CR47-006 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Actual dry_run acceptance invokes pinned Query/Messages collaborators without ambient node_modules dependency.

#### Scenario: CR47-006 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Remove oracle from disposable install and launch fresh process; explicit failure with no skip/canned response/fallback.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-007 Resolve and execute the actual minimal dependency graph on Rust1.88
The contribution SHALL satisfy this observable result: Pinned nightly minimal-resolution graph and actual root/dev-dependent affected path build and execute with Rust1.88; corrected constraints derive from source/diagnostic evidence.

#### Scenario: CR47-007 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Pinned nightly minimal-resolution graph and actual root/dev-dependent affected path build and execute with Rust1.88; corrected constraints derive from source/diagnostic evidence.

#### Scenario: CR47-007 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** The original incompatible graph is rejected; normal compatible-latest resolution cannot count as minimum proof.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-008 Establish book example linkage and attribute the existing failure
The contribution SHALL satisfy this observable result: Actual agreed book example links and executes through a fresh consumer; immutable-base comparison/tool/artifact evidence distinguishes contribution regression from existing tool behavior.

#### Scenario: CR47-008 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** Actual agreed book example links and executes through a fresh consumer; immutable-base comparison/tool/artifact evidence distinguishes contribution regression from existing tool behavior.

#### Scenario: CR47-008 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Remove required dependency in disposable consumer and require failure; existence of rlib alone is rejected as proof.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-009 Guard dedicated BDD discovery and reject missing selections
The contribution SHALL satisfy this observable result: New boundary runs exact adopted scenario identities/counts; existing parser compatibility uses dedicated entry point without changing intentional legacy skips.

#### Scenario: CR47-009 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** New boundary runs exact adopted scenario identities/counts; existing parser compatibility uses dedicated entry point without changing intentional legacy skips.

#### Scenario: CR47-009 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Wrong tag/empty feature selection fails the new guard; original tests/cucumber.rs intentional skipped behavior is not changed.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

### Requirement: CR47-010 Retain complete affected parser core and installed SDK behavior
The contribution SHALL satisfy this observable result: All49 named root BDD targets, parser packet and fresh installed-native functional/control packet retain adopted matching/source/Messages/rerun and package behavior.

#### Scenario: CR47-010 accepted behavior
- **GIVEN** the actual source, fixture and collaborator identities bound by the phase47 contract
- **WHEN** the documented production consumer executes at the complete phase boundary
- **THEN** All49 named root BDD targets, parser packet and fresh installed-native functional/control packet retain adopted matching/source/Messages/rerun and package behavior.

#### Scenario: CR47-010 rejection control
- **GIVEN** a disposable control preserving original production source and evidence
- **WHEN** Existing controls execute; corrupt identity/drop attempt/remove native library where specified and prove rejection.
- **THEN** the false result is visibly rejected without silent skip, fallback or lost original evidence

