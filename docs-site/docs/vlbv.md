---
id: vlbv
title: VLBV integration
---

# VLBV integration

Use original Cucumber Messages together with explicit application receipts to produce programmatic boundary results. The existing adapter is read-only: it does not run a packet, create authorization, close a canonical phase or authorize a release.

The [adapter](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/scripts/messages-to-boundary-results.mjs) uses Node's standard library with no npm dependencies. The native Rust compiler/runner itself does not require Node.

1. Capture assertions at the actual application callback, using a fresh shared attachment store. Resolve attachments through exact attempt, TestCase and TestStep IDs; do not pick the first case or infer identity from a title.
2. Preserve original Messages bytes, process status, timing, candidate/contract identity and all attempts. Bind the exact same Messages artifact reference in both `run.messages` and the process receipt's `messages` field.
3. Supply independently exercised oracle, negative-control and cleanup receipts with the existing authorization and frozen candidate records. A green formatter or exit status does not prove the business assertion executed.
4. Pass the bound receipt bundle to the adapter and retain its derived output separately from originals.

From the pinned Cucumber checkout, the invocation shape is:

```sh
node scripts/messages-to-boundary-results.mjs \
  --root /path/to/evidence-root \
  --bundle receipts/bundle.json
```

The bundle must satisfy the [receipt schema](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/phase39-receipts.schema.json); this is not a command for generating missing evidence. Follow the [producer recipe](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/VLBV-PRODUCER.md) and [full adapter contract](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/PHASE39-VLBV-ADAPTER.md).

The implemented scope is deterministic adopted-contract v2. Unsupported stochastic profiles are blocked. Exit0 means projected PASS, exit3 product FAIL, and exit2 BLOCKED/NOT_EXERCISED or invalid input; canonical consumers still apply their own gates. Hashes bind bytes, not the truth of producer observations.

For a follow-up run, the [native rerun plan](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/PHASE44-RERUN.md) resolves original scenarios or Examples rows. Apply both returned SourcePaths and LineSelectors. `None` means no execution; inspect run success separately. Selection is not B5 authorization, and later success does not erase prior failures or reduce the original denominator.

See [evidence](./evidence.md) for retained behavioral results. These tools do not grant canonical KBD certification.
