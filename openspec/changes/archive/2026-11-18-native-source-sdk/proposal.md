# Shared native SDK

## Why
Applications in Rust, TypeScript and Python need the same proven source compiler
and lossless rerun plans without duplicating Rust behavior or invoking subprocess
adapters. Travis explicitly adopted this first phase and its reviewed boundary.

## What Changes
Add independent sdk, bindings/node and bindings/python workspaces, strict version1
requests and safe Rust-owned extensions. Build actual local npm/wheel artifacts.
Preserve the existing core APIs, dependency snapshot, workflows and defaults.

## Capabilities
### New Capabilities
- native-sdk: source compilation, rerun, safe extensions and installed native adapters.

## Impact
Scope: sdk/**, bindings/**, phase46 artifacts and compatibility documentation.
No registry publication, external reviewer transmission, site deployment or
foreign step execution in this boundary. Both Python framework adapters follow.
