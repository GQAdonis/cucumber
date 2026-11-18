# Shared SDK contract proposal 1

Owner adopted the phase and reviewed boundary. Implementation and behavioral proof remain pending.
sdk-contract.schema.json defines the JSON boundary; it is not an executable test.
Native Rust owns all behavior. Both native adapters expose request(json: string)
returning a response JSON string; typed facades construct the same request.
Native library load failure occurs before this boundary and must be visible.

## Operations and errors

Each request has version=1, operation and input. Fields are strict. Capabilities
takes an empty input object. Compile requires original source, URI, explicit
gherkin/markdown format and defaultLanguage; no path reads or syntax guessing.
Use SourceGraph::parse_gherkin43 or the existing Markdown graph constructor.
Return full graph objects unchanged, preserving absent optional fields.
The protocol metadata records target baselines, not universal schema conformity.

Rerun accepts original NDJSON text, parsed only in Rust, and explicit separator.
No host JSON round-trip may round large input integers. Return all attempts,
ordered URI groups and formatted projection, retaining runSuccess independently.
Counters/lines use decimal strings across JSON so JavaScript cannot silently
round Rust u64 values. Missing run ID is null, not an invented identity.
An empty entries array means no rerun; never map it to all-source execution.

Invalid JSON/shape produces INVALID_REQUEST; recognizable unsupported version
produces UNSUPPORTED_VERSION before operation dispatch; an unknown operation
produces UNKNOWN_OPERATION. Source errors use SOURCE_ERROR with original URI.
The underlying core currently exposes some source errors as text: do not invent
structured location fields by scraping prose. Rerun errors retain incomplete run,
already-finished, invalid relevant envelope or missing reference distinctions.
NDJSON physical error line is optional decimal-string context, not a source line.
Unexpected caught adapter/core panics produce INTERNAL_ERROR; process faults/OOM
cannot be promised recoverable. A following valid request must still work after
ordinary input errors.

## Safe native Rust extensions

Proposed Rust-owned Extension interface supplies a qualified unique name and
execute(input) -> Result<Value, SdkError>. Sdk registration reserves core names
and rejects duplicates before mutation. Names use namespace.operation; core is
reserved. Extensions are invoked only through explicit extension dispatch in
Rust, not through core request.operation. Host binding capabilities therefore
do not advertise host callback registration or foreign step execution.

Each SDK instance owns its registry; no global mutable session. The basic
compiler/rerun boundary remains synchronous and independently instantiated.
Extension arbitrary payload semantics belong to the application; Rust extensions
do not become Cucumber step definitions, Python fixtures or JS support files.

## Oracle and isolation requirements

See oracle-identities.json for exact current retained oracle/source hashes.
Official AST/Pickle generators can choose different IDs: establish a bijection
by full corresponding structure, reject duplicate IDs, require every reference
to map, then compare complete objects/array order. Do not normalize URI, source
location, argument order or reference relationships. Supply the fixture's own
URI to both sides. Mutate captured AST/Pickle relationships as a negative control.

Use the pinned actual RerunFormatter only for selection/grouping. Compare full
attempts with original Messages and actual pinned EventDataCollector. Preserve
recovering/exhausted retries, every non-PASSED status and global/parser failure
with empty selection. A missing TestRunFinished errors; interrupted attempts
inside a finished run retain completed=false and UNKNOWN as core currently does.

Package proof uses fresh processes, clean Python environments, scrubbed module
search overrides and installed module/native-library realpaths outside checkout.
Record archive and native binary hashes. Removing a native binary is tested in
a separate fresh process, with no previously loaded module available. Rust's
external consumer records actual resolved dependency source/revision.

## Concrete validation precedence

1. Non-JSON text or a non-object top level: INVALID_REQUEST.
2. Missing/noninteger version: INVALID_REQUEST. An integer version other than 1:
   UNSUPPORTED_VERSION, even if operation is unknown or input malformed.
3. Version1 with missing/nonstring operation: INVALID_REQUEST. An unrecognized
   string operation: UNKNOWN_OPERATION, before operation-input validation.
4. Known operation with missing, wrong-type, additional or absent required input
   fields: INVALID_REQUEST. All version1 request objects reject unknown fields.
5. A valid compile shape with unsupported defaultLanguage or invalid Gherkin:
   SOURCE_ERROR, always carrying the original exact URI, even when empty.

Examples: version2/operation=unknown/input=null gives UNSUPPORTED_VERSION;
version1/operation=unknown/input=null gives UNKNOWN_OPERATION; version1/compile
with source=17 gives INVALID_REQUEST. No error prose equality is required.

SDK-006 includes attempt=9007199254740993 in original NDJSON and expects that
exact decimal string; do not use JS JSON.parse as its precision oracle. SDK-010
compiles and executes an external TypeScript consumer of the installed public
API within phase-end BDD, recording declaration resolution. No early typecheck.
Validate request and response against their respective schema $defs; the root
oneOf is an artifact convenience, not permission to send responses as requests.
