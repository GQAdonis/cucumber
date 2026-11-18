# Shared native SDK programme — proposed phase46

The verified Rust foundation through45 is preserved on both origins. Active KBD
phase: phase-46-native-sdk. Assessment and eleven scenario candidates are
proposals; no adoption or new SDK verification is claimed.

Proposed first value: safe Rust SDK compilation and Messages rerun operations
delegate to existing native implementations, with thin in-process NAPI-RS/PyO3
bindings, TypeScript/Python facades and actual local package artifacts. A safe
namespaced Rust extension interface cannot replace built-ins. No host parser or
subprocess is represented as FFI.

See [programme](../../.kbd-orchestrator/phases/phase-46-native-sdk/programme.md),
[scenario proposal](../../.kbd-orchestrator/phases/phase-46-native-sdk/scenario-candidates.md),
[calibration examples](../../.kbd-orchestrator/phases/phase-46-native-sdk/calibration-proposal.json)
and [implementation proposal](../../.kbd-orchestrator/phases/phase-46-native-sdk/plan.md).

Later work: captured registration and World factories, real Promise/Python
callback execution, framework compatibility, both additive Docusaurus sites,
package preparation and independent review. Python target is unresolved:
Behave1.3.3 and pytest-bdd9.0.1 have different Context/fixture/plugin contracts.
Neither is already supported by a new SDK.

## Documentation and distribution

Neither repository currently has Docusaurus. Plan independent private docs-site
packages using pinned Docusaurus3.10.2; retain mdBook and mature build/release
workflows. Clearly label GQAdonis forks and use the researched official green
palette; logo trademark permission is not assumed. Hosting is undecided.

Public npm scope/names, Python name, ownership, publication scope and supported
platforms require confirmation. No wrapper artifacts exist or are published.

## Review and upstream contribution gates

After implementation and complete phase-end BDD proof, independently audit both
repositories: core/SDK correctness, FFI ownership and panic/exception handling,
callbacks/cancellation, compatibility/defaults, packaging dependency closure,
documentation and maintainability. Review actual frozen source and evidence.
Retain finding IDs, severity, source references, dispositions and repair evidence.
Material behavioral repairs require their own complete BDD boundary. No clean
claim before necessary corrections and review are complete.

Then inspect upstream policies/existing issues; separate parser changes from
runner/protocol and SDK contributions, parser dependencies first. Create matching
issues/PRs only after completion. Fork branding/distribution must not be presented
as upstream endorsed. No issues/PRs have been opened for this work.

Recheck these overlap leads at contribution time; status and actual overlap are
not yet verified: https://github.com/cucumber-rs/cucumber/pull/391 (step hooks/
reporting), https://github.com/cucumber-rs/cucumber/pull/405 (scenario sharding).
Record actual comparison and coordinate to avoid duplicate contributions.
These leads do not block preservation pushes.

## Current blockers

Owner calibration/adoption is pending for the new finite scenario frontier.
Isolated assessment review was denied before sending: external disclosure of
nonpublic packet content lacks explicit authorization. Prepared packet and exact
denied command are retained in the phase review directory; no findings exist.
This planning review is separate from the final code audit.
