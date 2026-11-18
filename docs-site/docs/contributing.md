---
id: contributing
title: Contributing
---

# Contributing

This is the GQAdonis fork. Keep contributions bounded, source-pinned and reviewable; preserve existing consumer defaults unless an explicit compatibility policy changes them.

Author the finite behavior scenarios first, implement the complete phase, then run only its focused BDD acceptance. Do not introduce unit suites, unqualified Cargo test runs or early build/check/lint/import probes. Retain exact commands, failed attempts, nonzero scenario counts and final results. Existing Rust build/release workflows and mdBook remain intact; the documentation package is additive.

The complete programme requires an independent audit after implementation and behavioral proof, covering both parser and runner, Rust extensions, FFI ownership/errors, language callbacks, compatibility, packaging and documentation. Record reviewer identity, limitations, findings and dispositions. Material behavioral fixes need their own completed BDD boundary. Internal review is not external or cross-model certification; do not call the codebases clean before the gate is satisfied.

Matching upstream issues and pull requests are authorized at completion, after that review. Read current contribution policies and existing issues first, separate coherent contributions, and preserve parser-before-consumer dependency order. Recheck these possible overlaps rather than assuming their status or equivalence:

- [cucumber-rs/cucumber#391](https://github.com/cucumber-rs/cucumber/pull/391): step hooks/reporting lead.
- [cucumber-rs/cucumber#405](https://github.com/cucumber-rs/cucumber/pull/405): scenario sharding lead.

Their current status and actual overlap are unverified here. No completion issues or pull requests are claimed. Repository preservation commits/pushes are distinct from registry publication; package naming/ownership and publication scope still require confirmation.

This site is fork documentation, not endorsed by upstream. It uses text identity rather than assuming logo trademark permission. Original code remains under its [MIT](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/LICENSE-MIT) or [Apache-2.0](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/LICENSE-APACHE) terms. Hosting remains undecided and no deployment is authorized by these instructions. Read the [SDK roadmap](./sdk.md) and [evidence](./evidence.md) before expanding scope.
