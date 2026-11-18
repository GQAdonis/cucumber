# Cucumber/Gherkin project constraints

Authority: Travis's explicit delegation,2026-11-17/18; current instructions take precedence over generic skill examples.

- Author finite acceptance scenarios before implementation. No generated-code execution until the complete value-phase boundary: no unit suites, generic cargo test, early build/check/lint/typecheck/import/probe. Only focused BDD, including actual packaged consumers, at the adopted boundary.
- Preserve all through45 source, evidence and unrelated edits. Existing build/release workflows, Cargo settings and mdBook remain intact. Add wrappers and Docusaurus sites with independent manifests only.
- SDKs reuse native Rust parser, matching, scheduling, lifecycle and Messages semantics. Do not duplicate them in host languages or call a subprocess and label it FFI.
- Track selected compatibility versions, native API boundaries and actual evidence. Investigate Behave and pytest-bdd as separate optional compatibility targets; a common parser is not framework parity.
- Registry names, ownership, credentials/access and publication scope require confirmation before registration/publication. Never store credentials. Documentation hosting is undecided; no deployment.
- Repository preservation commits/pushes are explicitly authorized. Origins are GQAdonis/cucumber and GQAdonis/gherkin. Use non-release branches; no force push, main overwrite or v-tag release trigger.
- After the complete implementation and BDD boundary, independently audit correctness, safety, maintainability, compatibility, documentation and packaging. Record findings/dispositions; apply necessary corrections under the same boundary rules. Do not call the codebases clean before this gate.
- Upstream matching issues/PRs are explicitly authorized only at completion and after review. Read contribution policies/existing issues, split reviewable contributions and preserve parser-before-consumer dependency order. No premature issues/PRs.
- Canonical state is the append-only KBD runtime; never hand-edit generated progress, waypoint, disposition or journal. Prior phase evidence is historical, not retroactive canonical certification.
- Do not transmit project code, specifications or review packets to external review providers; the denied dispatch must not be retried. Internal independent review must identify its reviewer and limits without claiming cross-model certification.
