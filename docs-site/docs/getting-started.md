---
id: getting-started
title: Getting started
---

# Getting started

Use a **pinned checkout** of the GQAdonis fork with Rust 1.88 or later. The interoperability changes described here are not a published crates.io release.

Place the full checkout beside your application and preserve its revision:

```sh
git clone https://github.com/GQAdonis/cucumber.git cucumber
git -C cucumber checkout --detach 6e4753fc0783038bb388de1b4d76055edc697b8f
```

For an application in a sibling directory, add:

```toml
[dev-dependencies]
cucumber = { path = "../cucumber", features = ["output-messages"] }

[[test]]
name = "acceptance"
harness = false
```

Keep the full checkout, including `src`, `codegen`, `vendor` and their manifests. The bundled `vendor/gherkin` snapshot removes the need for a sibling parser clone or a machine-specific Cargo patch. Retain your application's lockfile. A relocated consumer is covered by the [existing portability acceptance](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/tests/portability.rs).

Your application supplies its async entry point, World and step callbacks. The [preserved README example](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/README.md#usage) shows the native World/step pattern. Author your behavior scenarios before implementing them; execute only the focused BDD target after its complete phase boundary.

Select compatibility policies independently:

| Need | Explicit choice |
| --- | --- |
| Adopted Gherkin43 syntax and source semantics | `.with_gherkin43()?` |
| Match text across Given/When/Then registrations | `.step_matching(cucumber::step::Matching::KeywordIndependent)` after installing the final step collection |
| JS pending/skipped outcome policy | `.outcome_policy(cucumber::execution::OutcomePolicy::cucumber_js())` |
| Source-backed Messages output | `.with_messages(output)` for the Basic parser |

These choices do not enable every JS behavior. Existing defaults remain available. For hook and attachment reporting, share the actual producer stores with the writer; follow the [complete wiring guide](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/REUSE.md#report-original-sources-and-actual-execution).

Awaiting `.run(...)` does not itself set your application's process exit code. Preserve the original NDJSON, inspect actual completion, and handle missing or unsuccessful completion explicitly. Review [compatibility](./compatibility.md) and [VLBV integration](./vlbv.md) before using a report as acceptance evidence. Historical local-only statements in earlier guides are superseded by the [preservation record](https://github.com/GQAdonis/cucumber/blob/82c86632d63b323d4c3abdce24c404d0029158d0/docs/compatibility/DELIVERY.md#fork-and-distribution-status).
