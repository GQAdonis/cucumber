# Proposed implementation order — not an adopted contract

Prerequisite: owner review of calibration and finite frontier. Python framework
selection blocks its adapter, not framework-neutral compiler/rerun APIs. Public
names/ownership block publication, not private local packaging. Hosting blocks
deployment, not documentation authoring.

1. Author adopted business scenarios and focused harness without running it.
2. Add independent safe sdk crate with versioned owned DTOs, source compilation
   and rerun delegated to existing Rust code, and namespaced extensions.
3. Add thin Node/Python native adapters in independent nested workspaces.
   NAPI-RS/PyO3 candidates are source-researched, not resolution/MSRV certified.
4. Add TypeScript/Python facades and private artifact metadata including native
   libraries/licenses. No registration, import downloads or subprocess fallback.
5. Finish artifact-based BDD and controls, freeze source, then run the adopted
   packet at phase end. No intermediate build/import/lint/typecheck/test.
6. Retain original logs, child commands/exits and artifact identities; bounded
   behavioral repairs; documentation claims only as far as evidence supports.

Proposed commands (not authorized before complete adopted phase boundary):

    env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --manifest-path sdk/Cargo.toml --test language_sdk -- --tags @sdk46
    env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --manifest-path sdk/Cargo.toml --test language_sdk -- --tags @sdk46_negative

The target must be harness=false and exercise real package consumers. Build,
packaging and installation occur as user actions at that boundary. Initial
dependency resolution must be an explicit packet action before --locked commands;
do not assume lockfiles already exist. Final adopted commands are fixed before
generation, not adjusted after results to conceal failures.

Proposed budget: 240 minutes, 200 tool calls, at most two owner-authorized repairs,
stop after three no-progress cycles; tokens UNKNOWN. These limits are proposed.
All eleven cases/controls, cleanup and artifact identities are required.

Remaining programme: native dynamic registration/World factory, foreign callback
and framework parity, both docs sites, package preparation, final independent
audit/corrections, then matching upstream issues/PRs. This first SDK boundary does
not complete the user's entire request.
