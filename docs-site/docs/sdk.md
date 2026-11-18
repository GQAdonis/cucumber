---
id: sdk
title: SDK roadmap
---

# SDK roadmap

The extensible Rust SDK and in-process TypeScript/Python native bindings are **proposed and unverified**. No new npm or Python wrapper package is available or published. The existing Rust foundation already offers useful compiler and rerun operations.

| Surface | Current status |
| --- | --- |
| `SourceGraph::parse_gherkin43` and Markdown/source snapshot variants | Existing native compiler graph in the `output-messages` feature |
| Messages rerun `Collector` and `Plan::local_selection` | Verified native operations retaining all attempts and original source locations |
| Safe namespaced Rust extension interface | Proposed; must preserve built-in behavior |
| TypeScript native wrapper | Proposed shared-core binding; no JS support-file execution claim |
| Python native wrapper | Proposed shared-core binding; no framework parity claim |

See the [existing compiler implementation](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/src/writer/messages/source.rs) and [verified rerun API](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/PHASE44-RERUN.md). Native parsing and rerun collection require no JavaScript runtime.

The staged direction is to expose those shared operations and the safe Rust extension surface first, then implement foreign step execution. Host wrappers must call the Rust implementation rather than duplicate parser, runner or reporting semantics. A subprocess bridge is not in-process FFI.

Both **Behave 1.3.3** and **pytest-bdd 9.0.1** are **unverified adapter tracks** to investigate. Behave Context/hooks and pytest-bdd fixtures/plugins have different lifecycle contracts; a common parser alone establishes parity with neither. Cucumber.js 13.3.0 remains the pinned JS behavior target. Version pins describe the investigation targets, not tested package compatibility.

The [preserved programme proposal](https://github.com/GQAdonis/cucumber/blob/82c86632d63b323d4c3abdce24c404d0029158d0/docs/compatibility/SDK-ROADMAP.md) records the initial scope. Current direction investigates both Python tracks while continuing shared-core and documentation work. SDK owner calibration and contract adoption remain unresolved. Internal planning review cannot be represented as external or cross-model certification, and is separate from the final code audit.

Before registration or publication, confirm intended npm scope/package names, Python package names, ownership/access, publication scope and supported platforms. Package preparation must be additive and preserve established build/release workflows. See [contributing](./contributing.md) for the review and upstream gates.
