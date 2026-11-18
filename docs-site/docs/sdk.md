---
id: sdk
title: SDK roadmap
---

# SDK roadmap

The adopted first SDK phase has **bounded installed-package BDD evidence** for the shared Rust compiler/rerun SDK, Rust-owned extensions, and in-process Node/TypeScript and Python bindings. The completed repair2 packet built and installed real local artifacts, passed **11 functional scenarios /33 steps** and **11 negative controls /33 steps**, and retained outer Messages proof for **22 scenarios /66 steps** plus cleanup. Scoped internal review and static QA resolved their material findings. No registry package is published, and no foreign step execution or Python framework adapter is implemented. See [phase46 evidence and limits](https://github.com/GQAdonis/cucumber/blob/foundation/rust-bdd-sdk/docs/compatibility/PHASE46-SDK.md).

| Surface | Current status |
| --- | --- |
| Core source compiler and Messages rerun collector | Verified through45 for the preserved core snapshot |
| `cucumber_sdk::Sdk` compile/rerun/capabilities and JSON request API | Installed Rust consumer covered by repair2 |
| `Extension`, registration and invocation | Rust extension contract covered by repair2; no host callbacks |
| Node/TypeScript | Actual local NAPI-RS archive installed outside checkout; TypeScript consumer covered by repair2 |
| Python | Actual local PyO3 wheel installed outside checkout; Python consumer covered by repair2 |

The wrappers pass requests into the same Rust implementation. They do not duplicate Gherkin parsing or rerun selection in host languages. The underlying [compiler](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/src/writer/messages/source.rs) and [rerun contract](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/PHASE44-RERUN.md) retain their existing compatibility boundaries.

## Authored Rust API

These examples illustrate the APIs exercised by the installed-consumer boundary; they are not additional acceptance runs. A sibling application uses `cucumber-sdk = { path = "../cucumber/sdk" }` and retains the complete Cucumber checkout.

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

These examples require a compatible local native artifact. The adopted repair2 boundary built and installed those artifacts in fresh external consumers. The names shown remain private local placeholders, not registry packages offered for installation.

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

Owner adoption is resolved and the repair2 packet completed: preparation, eleven behaviors and eleven negative controls. Future behavioral changes retain the complete phase-end BDD rule; an isolated build, import, install or smoke test is not an acceptance substitute.

The `sdk/acceptance/prepare.py` packet built the N-API library, placed `cucumber_sdk.node` beside the Node facade, packed a private npm archive and installed it into a fresh outside-checkout consumer. Packing alone does not build a binary. It also built a wheel with maturin1.12.6/PyO3 0.30.1, installed it into a fresh Python environment and prepared an external Rust consumer. Original commands, logs, installed realpaths, archive/native hashes, official-oracle comparisons, negative controls, outer Messages and cleanup receipts are retained. Local artifacts remain under `docs/compatibility/evidence/sdk46-repair2/artifacts/`, ignored by Git; their identity receipts are retained.

The verified repair2 environment is Darwin arm64, Rust1.88.0, Node26.5.0 and CPython3.11.3, with a TypeScript6.0.3 declaration consumer. Other runtime/platform combinations remain unverified. Host-specific Node archives, other platform wheels and Python source distributions are not a portable release claim. Existing root build/release workflows remain unchanged.

The initial Node24 mismatch remains recorded. Repair1 passed its cases, but review found JSON map/type confusion and missing outer Messages evidence. Repair2 fixed those issues and passed the full packet without replacing prior evidence. The [phase report](https://github.com/GQAdonis/cucumber/blob/foundation/rust-bdd-sdk/docs/compatibility/PHASE46-SDK.md) distinguishes these attempts.

Both distributions currently use `cucumber-native-local` version0.0.0, with Python import name `cucumber_native_local`. Public npm scope/names, Python names, ownership/access, publication scope and supported platforms require confirmation before registration or publication. Artifact dependency/license closure also remains a distribution requirement.

## Remaining work and evidence limits

**Behave1.3.3** and **pytest-bdd9.0.1** remain **unverified adapter tracks**. Their Context/hooks and fixture/plugin contracts differ; shared parsing establishes parity with neither. Cucumber.js13.3.0 remains the JS behavior target, official Gherkin43 the compiler target, and Messages34.2.1/35.0.0 the protocol targets. Foreign step execution, asynchronous host callbacks and framework adapters are not implemented in this phase.

Through45 evidence and the earlier documentation boundary's **10 scenarios /64 steps** apply to their historical source snapshots. SDK proof comes from the separate repair2 packet. Scoped internal review and static QA resolved their material findings; no full-program clean, full-parity or external/cross-model certification claim is made. See [evidence](./evidence.md), [compatibility](./compatibility.md) and [contributing](./contributing.md) for retained limits and upstream contribution gates.

[Cucumber](https://gqadonis.github.io/cucumber/) and [Gherkin](https://gqadonis.github.io/gherkin/) fork Pages sites are live. Their public boundary passed **4 scenarios /22 steps** and both repository About links were updated. Those observations precede these latest page edits, whose documentation acceptance and delivery remain separate.
