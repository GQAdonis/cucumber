## ADDED Requirements

### Requirement: SDK-001 Compile plaintext source to faithful AST and Pickles in all three installed SDKs
The native SDK SHALL rules, outlines, both argument orders and Unicode retain source locations and identities.

#### Scenario: SDK-001 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Rules, outlines, both argument orders and Unicode retain source locations and identities
- **AND** the negative control is rejected: Mutate an expected cell or location; comparison must fail

### Requirement: SDK-002 Compile Markdown through the same native implementation
The native SDK SHALL literal backticks in steps/tables/docstrings remain content; declaration tags remain tags.

#### Scenario: SDK-002 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Literal backticks in steps/tables/docstrings remain content; declaration tags remain tags
- **AND** the negative control is rejected: Misplaced or repeated argument must return a typed parse error

### Requirement: SDK-003 Compile empty/comment-only input without invented scenarios
The native SDK SHALL valid featureless input yields no Pickles.

#### Scenario: SDK-003 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Valid featureless input yields no Pickles
- **AND** the negative control is rejected: Inject a synthetic Feature/Pickle into expected output and reject

### Requirement: SDK-004 Recover after malformed input in the same host
The native SDK SHALL typed SOURCE_ERROR retains the exact original URI; a following valid request succeeds.

#### Scenario: SDK-004 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Typed SOURCE_ERROR retains the exact original URI; a following valid request succeeds
- **AND** the negative control is rejected: Invalid input cannot produce successful empty output

### Requirement: SDK-005 Discover the versioned implemented operations
The native SDK SHALL capabilities identify compiler and rerun operations and do not advertise foreign execution.

#### Scenario: SDK-005 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Capabilities identify compiler and rerun operations and do not advertise foreign execution
- **AND** the negative control is rejected: Unknown version/operation and premature runtime execution are refused

### Requirement: SDK-006 Derive a lossless rerun plan from real Messages
The native SDK SHALL retain every attempt and original non-PASSED scenario/Examples-row selectors; keep run_success independent, including failed runs with no selected cases.

#### Scenario: SDK-006 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Retain every attempt and original non-PASSED scenario/Examples-row selectors; keep run_success independent, including failed runs with no selected cases
- **AND** the negative control is rejected: Drop a failed attempt or replace original row with a synthetic line and reject

### Requirement: SDK-007 Reject incomplete or inconsistent run evidence
The native SDK SHALL missing references or missing TestRunFinished remain visible errors; a finished run may retain interrupted attempts with completed=false and UNKNOWN.

#### Scenario: SDK-007 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Missing references or missing TestRunFinished remain visible errors; a finished run may retain interrupted attempts with completed=false and UNKNOWN
- **AND** the negative control is rejected: Truncate a genuine stream; no empty passing plan

### Requirement: SDK-008 Represent a completed passing run as no rerun
The native SDK SHALL no selected cases means None/empty plan and cannot mean run everything.

#### Scenario: SDK-008 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** No selected cases means None/empty plan and cannot mean run everything
- **AND** the negative control is rejected: Bogus nonempty/all-source selection is rejected

### Requirement: SDK-009 Extend the safe SDK from an external Rust consumer
The native SDK SHALL namespaced extension returns its real result without overriding built-ins.

#### Scenario: SDK-009 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Namespaced extension returns its real result without overriding built-ins
- **AND** the negative control is rejected: Reserved builtin or duplicate registration is refused

### Requirement: SDK-010 Consume actual native package artifacts outside the checkout
The native SDK SHALL local npm archive and Python wheel execute native entry points from fresh directories; a real external TypeScript consumer imports the public declarations, compiles and executes inside this same phase-end BDD scenario.

#### Scenario: SDK-010 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Local npm archive and Python wheel execute native entry points from fresh directories; a real external TypeScript consumer imports the public declarations, compiles and executes inside this same phase-end BDD scenario
- **AND** the negative control is rejected: Remove native artifact from a disposable install, launch another fresh host process; explicit load failure with no module cache, checkout injection, parser or subprocess fallback

### Requirement: SDK-011 Keep requests isolated in one host process
The native SDK SHALL different URIs, parse failures and run IDs cannot leak across requests.

#### Scenario: SDK-011 installed consumer behavior
- **GIVEN** the actual installed native package and preserved fixture identities
- **WHEN** the application invokes the declared SDK operation
- **THEN** Different URIs, parse failures and run IDs cannot leak across requests
- **AND** the negative control is rejected: Cross-associated IDs must fail or differ from the correct output

