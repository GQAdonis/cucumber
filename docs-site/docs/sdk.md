---
id: sdk
title: SDK roadmap
---

# SDK roadmap

The adopted first SDK phase now has **implemented source, awaiting whole-phase BDD verification**: a shared Rust compiler/rerun SDK, Rust-owned extensions, and in-process Node/TypeScript and Python bindings. Native packages have not yet been built or installation-verified. Nothing is registered or published, and no foreign step execution or Python framework adapter is implemented.

| Surface | Current status |
| --- | --- |
| Core source compiler and Messages rerun collector | Verified through45 for the preserved core snapshot |
| `cucumber_sdk::Sdk` compile/rerun/capabilities and JSON request API | Source exists in `sdk/`; new boundary unverified |
| `Extension`, registration and invocation | Source exists; instance-owned Rust operations, no host callbacks |
| Node/TypeScript | NAPI-RS native addon, facade and declarations exist in `bindings/node/`; packaged consumer proof pending |
| Python | PyO3 extension and typed facade exist in `bindings/python/`; wheel consumer proof pending |

The wrappers pass requests into the same Rust implementation. They do not duplicate Gherkin parsing or rerun selection in host languages. The underlying [compiler](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/src/writer/messages/source.rs) and [rerun contract](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/PHASE44-RERUN.md) retain their existing compatibility boundaries.

## Authored Rust API

The following examples describe the current source; they are not claims of completed SDK acceptance. A sibling application uses `cucumber-sdk = { path = "../cucumber/sdk" }` and retains the complete Cucumber checkout.

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

Choose `SourceFormat::Markdown` explicitly for Markdown. Compilation consumes supplied text and preserves URI identity; it does not discover files or guess syntax. `sdk.rerun(original_ndjson, "\n")` derives all attempts, ordered URI groups, formatted selection and independent run success. Counters and source lines are decimal strings. Preserve the original NDJSON text, especially across JavaScript; parsing and reserializing it first can round large integers. Empty rerun entries mean no selected scenarios, not all-source execution.

To extend a Rust application, implement `Extension::name` and `Extension::execute`, then call `register_extension` and `execute_extension`. Names have at least two dot-separated ASCII identifiers, such as `verification.summary`; `core` is reserved and duplicate registration is rejected before mutation. Registrations belong to one SDK instance and cannot replace core operations. Extensions are not Cucumber step definitions or host callbacks. Ordinary unwinding panics map to `INTERNAL_ERROR`; recovery does not cover aborts, process faults, OOM or rollback of application side effects.

## Authored language APIs

These examples assume an eventual local native artifact has been built and installed through the adopted boundary. That prerequisite is still pending. The names shown are private local placeholders, not registry packages offered for installation.

```ts
import { compile, rerun } from 'cucumber-native-local';

const graph = compile({
  source: 'Feature: Inventory\n  Scenario: Empty shelf\n    Given an empty shelf\n',
  uri: 'memory:inventory.feature',
  format: 'gherkin',
  defaultLanguage: 'en',
});
console.log(graph.gherkinDocument, graph.pickles);
// rerun({ ndjson: originalNdjson, separator: '\n' });
```

```python
from cucumber_native_local import compile_source, rerun

compiled = compile_source(
    "Feature: Inventory\n  Scenario: Empty shelf\n    Given an empty shelf\n",
    "memory:inventory.feature",
)
print(compiled["gherkinDocument"], compiled["pickles"])
# rerun(original_ndjson, separator="\n")
```

Both facades also expose `capabilities()` and raw `request(string) -> string`. Raw requests retain versioned success/error envelopes; convenience calls raise `SdkError` for core error responses. Native module load failures remain host errors and have no parser fallback. The protocol owns error codes and optional context; error prose is not a compatibility guarantee. The facade source and full examples are in each binding's README in the current checkout.

## Local artifact boundary

Owner adoption is resolved. All production and acceptance sources must be complete before the orchestrator runs the adopted packet: preparation, eleven behaviors and eleven negative controls. No isolated build, import, install or smoke test is an acceptable substitute.

The authored `sdk/acceptance/prepare.py` will build the N-API library, place `cucumber_sdk.node` beside the Node facade, pack a private npm archive and install it into a fresh outside-checkout consumer. Packing alone does not build a binary. It will also build a wheel with maturin1.12.6/PyO3 0.30.1, install it into a fresh Python environment and prepare an external Rust consumer. The whole packet retains original commands, logs, installed realpaths, archive/native hashes, official-oracle comparisons, negative controls and cleanup receipts.

The initial target is Darwin arm64, Rust1.88.0, Node26.5.0 and CPython3.11.3, with a TypeScript6.0.3 declaration consumer. No platform/runtime is newly verified yet. Host-specific Node archives, other platform wheels and Python source distributions are not a portable release claim. Existing root build/release workflows remain unchanged.

Both distributions currently use `cucumber-native-local` version0.0.0, with Python import name `cucumber_native_local`. Public npm scope/names, Python names, ownership/access, publication scope and supported platforms require confirmation before registration or publication. Artifact dependency/license closure also remains a distribution requirement.

## Remaining work and evidence limits

**Behave1.3.3** and **pytest-bdd9.0.1** remain **unverified adapter tracks**. Their Context/hooks and fixture/plugin contracts differ; shared parsing establishes parity with neither. Cucumber.js13.3.0 remains the JS behavior target, official Gherkin43 the compiler target, and Messages34.2.1/35.0.0 the protocol targets. Foreign step execution, asynchronous host callbacks and framework adapters are not implemented in this phase.

Through45 evidence and the earlier documentation boundary's **10 scenarios /64 steps** apply to their historical source snapshots. Neither proves these new bindings or subsequent documentation edits. The whole-phase SDK result and independent post-implementation audit remain pending. Internal planning review is not external or cross-model certification, and no clean-code claim is made. See [evidence](./evidence.md), [compatibility](./compatibility.md) and [contributing](./contributing.md) for retained limits and upstream contribution gates. Fork Pages delivery is separately authorized and requires its own public behavior boundary.
