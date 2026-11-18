# Internal SDK planning review

Reviewer: /root/internal_sdk_review, internal Codex subagent. Exact deployed model
identity unavailable. Isolated fork_turns=none; read-only supplied artifact review.
No external provider dispatch, builds, tests, imports, installations or edits.
This is not owner adoption, cross-model certification or the final code audit.

| ID | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| IR-01 | High | JS rerun formatter only proves selection, not all attempt history or run success. | Scenario proposal now separates formatter projection from original Messages/pinned EventDataCollector; independent run_success required. |
| IR-02 | High | Versioned DTO/error/capability contract is not yet concrete. | Draft shared schema and malformed/versioned behavior now authored in SDK-CONTRACT-PROPOSAL.md and sdk-contract.schema.json; reviewer follow-up and owner adoption pending. |
| IR-03 | High | Archive acceptance could pass through checkout imports or cached native modules. | Plan requires fresh processes, isolated Python environment, scrubbed module paths, resolved native paths/hashes, fresh missing-binary process and external Rust provenance. |
| IR-04 | Medium | Fixture identity and normalization could hide source graph errors. | Draft oracle-identities.json binds retained artifacts; proposal requires bijective IDs without URI/location/reference normalization. Reviewer follow-up and owner adoption pending. |
| IR-05 | Medium | Broad unfinished-stream rejection conflicts with retained completed=false interrupted attempts. | Proposal now distinguishes missing run boundary from finished runs retaining interrupted attempts. |
| IR-06 | Medium | Exclusive Python target decision is superseded. | Both frameworks are separate optional research tracks; no selection blocker on shared core. |

Scope: assessment, analysis, library candidates, plan, scenarios, calibration,
goals and programme plus constraints. No production implementation review occurred.
Changes above are planning dispositions; they are not new behavioral proof.

## Internal follow-up review

Same isolated internal reviewer, exact deployment unknown; no execution. The
review found IR-01/03/04/05/06 substantially addressed at planning level and
identified three remaining medium concerns in the concrete boundary:

- IR-07: JS-only package consumption could miss broken TypeScript declarations.
  Disposition: SDK-010 now requires actual external TS compile-and-execute inside
  phase-end BDD, with declaration-resolution evidence.
- IR-08: promised integer preservation had no >2^53 case. Disposition: SDK-006
  now requires exact 9007199254740993 decimal-string preservation against original
  NDJSON, never the JS JSON.parse oracle for that field.
- IR-09: error schema made source URI optional. Disposition: schema conditionally
  requires URI for SOURCE_ERROR; SDK-004 requires exact equality. Concrete
  request-validation precedence is documented for SDK-005.

These dispositions are authored corrections, not executed schema/behavior proof.
Oracle hash inventory was not independently recomputed by the reviewer. Owner
calibration and contract adoption remain pending before SDK implementation.


## Completed phase46 post-implementation follow-up

The scoped internal review and static QA completed after repair2 BDD22/66. SDK46-IR-01 and SQA-01 are resolved; original findings remain in docs/compatibility/SDK46-INTERNAL-REVIEW.md and SDK46-STATIC-QA.md. This does not certify the broader programme or claim an external/cross-model review.
