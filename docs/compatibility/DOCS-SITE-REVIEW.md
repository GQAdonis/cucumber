# Independent internal documentation review

Reviewer: internal Codex subagent /root/docs_review, fork_turns=none. Exact
deployed model identity unknown. Read-only review with no external provider,
tests, builds, installs or imports. This is docs-only, not cross-model
certification or the final core/SDK/FFI review.

## Findings and dispositions

| ID | Severity | Finding | Disposition and retained proof |
| --- | --- | --- | --- |
| DOC-01 | Medium | Launcher accepted existing output directories and could overwrite original artifacts. | Resolved: reject existing run artifacts before outputs, exclusive run claim and owned exclusive BDD log. Real nested launcher refusal and unchanged bytes passed in the tenth scenario. |
| DOC-02 | Low coverage limit | Programmatic focus proved Enter activation but not Tab traversal. | Resolved: actual Tab navigation reaches toggle and active menu link before Enter; both mobile cases pass. |
| DOC-03 | Low coverage limit | Overflow measured Compatibility after leaving Getting started. | Resolved: measure Getting started before navigation and Compatibility afterward; both forks pass. |
| DOC-04 | Documentation clarity | Gherkin README retained a registry0.15 example below fork status. | Resolved: pinned-checkout guidance and path dependency distinguish unpublished fork behavior. |

Reviewer follow-up inspected corrected code and final receipts and found no new
material issue in this scoped change. Root README/status records were updated
from the historical9/56 to latest10/64; earlier evidence is retained unchanged.

## Evidence assessed

Repair4 first completed9 scenarios/56 steps, then the complete review correction
passed10/64 and both global hooks, exit0. Each negative link control had its own
npm-ci installation and successful unmodified production build before the
specific missing-link build failed. The reuse guard rejected before another
scenario run and preserved fixture bytes. Copies/browser/server cleanup recorded.

See [acceptance report](DOCS-SITE-ACCEPTANCE.md) and
[latest original receipts](evidence/docs-sites-20261118-review-repair/boundary-receipt.json).
No existing root Cargo, build/release workflow or mdBook change was introduced.

## Limits

Actual host is Darwin arm64, Node26.5.0 and Chrome157.0.8103.79. No broader browser
matrix or public hosting was exercised. External evidence links were inspected
as destinations, not fetched by the browser scenarios or independently verified
by the reviewer. The ordinary reader-facing pages and specified failure controls
are covered; this is not an exhaustive accessibility/security certification.
The codebases as a whole are not claimed clean: SDK/bindings implementation,
behavioral proof and the requested final independent audit remain outstanding.
