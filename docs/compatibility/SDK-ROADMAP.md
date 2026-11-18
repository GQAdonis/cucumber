# Shared native SDK programme — phase46 implementation

The verified Rust foundation through45 is preserved on both origins. Travis has
adopted the eleven-case first SDK contract; owner calibration/adoption is no
longer a blocker. Source for the shared SDK and both native bindings now exists.
The complete phase-end behavioral boundary remains pending: no new native package
has yet been built, installed or behavior-verified. No registry publication or
foreign-language step execution is claimed.

See the [owner adoption](../../.kbd-orchestrator/phases/phase-46-native-sdk/owner-adoption.json),
[bound contract](../../.kbd-orchestrator/phases/phase-46-native-sdk/adopted-contract.json)
and [execution record](../../.kbd-orchestrator/phases/phase-46-native-sdk/execution.md).
Earlier proposal wording is historical; this status does not amend the contract.

## Implemented source and exact boundary

| Surface | Source now present | Verification status |
| --- | --- | --- |
| Shared Rust SDK | [sdk/src/lib.rs](../../sdk/src/lib.rs): `Sdk::compile`, `Sdk::rerun`, `Sdk::capabilities`, versioned JSON `Sdk::request` | New surface unverified; delegates to through45 core operations |
| Rust extension interface | `Extension`, `register_extension`, `execute_extension`; instance-owned namespaced operations | New surface unverified; no built-in replacement or host callbacks |
| Node/TypeScript | [bindings/node](../../bindings/node/README.md): NAPI-RS addon, CommonJS facade and declarations | Source/metadata only; native archive and installed consumer pending |
| Python | [bindings/python](../../bindings/python/README.md): PyO3 extension, typed facade and wheel metadata | Source/metadata only; native wheel and installed consumer pending |

Host facades serialize requests and decode results. Rust owns source compilation,
rerun selection, protocol validation and structured error semantics. The bindings
are in-process native adapters; they do not call a parser subprocess. The SDK
has an independent Cargo workspace, and each binding has its own manifest;
established root build/release workflows remain unchanged.

Targets remain official Gherkin43.0.0, Cucumber.js13.3.0 and Messages34.2.1/35.0.0.
The first adopted host boundary is Darwin arm64, Rust1.88.0, Node26.5.0 and
CPython3.11.3, with the TypeScript6.0.3 declaration consumer. These are targets,
not successful runs or support claims for other environments. Python metadata's
>=3.9 allowance is not proof across those versions.

## Rust usage from the authored API

The examples in this section describe source APIs and have not yet been executed
through the complete SDK acceptance packet. A sibling application can declare
`cucumber-sdk = { path = "../cucumber/sdk" }`, retaining the whole Cucumber checkout
for its core, codegen and vendored parser dependencies.

```rust
use cucumber_sdk::{CompileInput, Sdk, SdkError, SourceFormat};

fn main() -> Result<(), SdkError> {
    let sdk = Sdk::new();
    let graph = sdk.compile(CompileInput {
        source: "Feature: Inventory\n  Scenario: Empty shelf\n    Given an empty shelf\n",
        uri: "memory:inventory.feature",
        format: SourceFormat::Gherkin,
        default_language: "en",
    })?;
    println!("{} pickles", graph.pickles.len());
    Ok(())
}
```

Choose `SourceFormat::Markdown` explicitly for Markdown. Source is supplied text,
not a path to discover or reread; URI identity is retained. Full graph fields,
including actual upstream optional-field absence, come from the existing compiler.
The documented Markdown `Feature.keyword`/Messages-schema conflict remains.

For original Messages text, `sdk.rerun(original_ndjson, "\n")?` returns all
attempts, ordered URI groups, formatted selection and independent run success.
Attempt counters and source lines are decimal strings. Do not parse and
reserialize input Messages in JavaScript before calling it: that could round
large integers. Empty `entries` means no selected scenarios. Selection neither
executes a run nor grants repair authority; keep original attempts and receipts.

An application extension implements the actual Rust trait:

```rust
use cucumber_sdk::{Extension, Sdk, SdkError};
use serde_json::Value;

struct Echo;
impl Extension for Echo {
    fn name(&self) -> &str { "application.echo" }
    fn execute(&self, input: &Value) -> Result<Value, SdkError> {
        Ok(input.clone())
    }
}

fn extension_example() -> Result<Value, SdkError> {
    let mut sdk = Sdk::new();
    sdk.register_extension(Echo)?;
    sdk.execute_extension("application.echo", &Value::String("receipt".into()))
}
```

The example additionally requires the application's own `serde_json` dependency.
Names contain at least two dot-separated ASCII identifiers; `core` is reserved
and duplicates are rejected before registry mutation. The SDK owns the registered
extension per instance. Extensions are Rust application operations, not step
definitions, Python callbacks or JavaScript handlers. Ordinary unwinding panics
are mapped to `INTERNAL_ERROR`; aborts/process faults/OOM and application side
effects are outside recovery. Native library loading occurs before the JSON
error boundary. See [the SDK guide](../../sdk/README.md) for the exact contract.

## Local native artifacts: preparation is still pending

Do not run an isolated build, import or installation during implementation.
After all production and acceptance sources are complete, the orchestrator runs
the adopted whole-phase packet: [preparation](../../sdk/acceptance/prepare.py),
eleven behavior cases and eleven negative controls. Follow the bound contract
rather than replacing it with a package smoke test or unit suite.

At that boundary, preparation is intended to:

1. Resolve independent lockfiles under Rust1.88 and build the actual native addon.
   Copy the host library to `bindings/node/cucumber_sdk.node` before packing;
   `npm pack` alone does not build a binary. Install the local private archive
   into a fresh outside-checkout consumer with scripts disabled.
2. Build a wheel using pinned maturin1.12.6 and PyO3 0.30.1, then install that
   wheel into a fresh outside-checkout Python environment.
3. Build the external Rust consumer and retain original argv, exits, logs,
   archive/native hashes, installed realpaths and dependency identities.
4. Exercise public Rust/TypeScript/Python operations, official pinned oracles and
   negative controls, including visible failure when an installed native binary
   is missing; retain cleanup observations and every attempt.

No resulting artifact or passing installation is claimed yet. The Node archive
will be specific to its build host; cross-platform prebuilts and a standalone
Python source distribution are not certified. See [packaging acceptance](../../sdk/acceptance/README.md)
and the binding READMEs for current layout and provisional identities.

Both local distributions use the placeholder name `cucumber-native-local` at
0.0.0; Python imports use `cucumber_native_local`. Node is marked private, Python
has `Private :: Do Not Upload`, and Rust manifests use `publish = false`.
Names are not registered or reserved. Public npm scope/names, Python name,
ownership/access, publication scope and supported platforms require confirmation.
Resolved artifact dependency/license closure also precedes public distribution.
No credentials belong in the repository.

## Remaining compatibility work

Foreign step execution, captured registrations/World factories and asynchronous
host callbacks are not implemented in this first SDK phase. Both Behave1.3.3 and
pytest-bdd9.0.1 remain separate unverified optional adapter tracks with different
Context/fixture/plugin contracts; see [the dual-target matrix](PYTHON-TARGETS.md).
Shared parsing does not establish parity with either framework or Cucumber.js
support-file execution. Rust extensions are currently exposed to Rust callers
only, not registered through the Node/Python facades.

## Historical evidence and documentation

Through45 core evidence remains valid for its preserved source snapshot; it is
not new SDK proof. Both independent Docusaurus packages passed the earlier
[documentation boundary](DOCS-SITE-ACCEPTANCE.md): 10 scenarios /64 steps,
including isolated broken-link controls. That evidence describes the prior
site source, not subsequent SDK page edits. Hosting is undecided; no site
deployment occurred. mdBook and mature build/release workflows remain intact.

## Review and upstream contribution gates

After the full implementation and phase-end BDD proof, independently audit both
repositories: core/SDK correctness, FFI ownership and panic/exception handling,
callbacks/cancellation where implemented, compatibility/defaults, packaging
closure, documentation and maintainability. Retain finding IDs, severity, source
references, reviewer identity/limitations, dispositions and repair evidence.
Material behavioral repairs require their own complete BDD boundary. No clean
claim before necessary corrections and review are complete.

The retained [internal planning review](../../.kbd-orchestrator/phases/phase-46-native-sdk/review/internal-review.md)
is separate from that final code audit. Exact model deployment is unknown;
no external or cross-model certification is claimed. External project/review
packet dispatch remains prohibited and the denied dispatch will not be retried.

Then inspect current upstream policies and existing issues, separate parser
changes from runner/protocol and SDK contributions, and preserve parser-first
dependency order. Create matching issues/PRs only after completion and review.
No completion issues/PRs are claimed. Recheck these unverified overlap leads:
https://github.com/cucumber-rs/cucumber/pull/391 (step hooks/reporting) and
https://github.com/cucumber-rs/cucumber/pull/405 (scenario sharding).
These leads do not block authorized preservation pushes to the forks.
