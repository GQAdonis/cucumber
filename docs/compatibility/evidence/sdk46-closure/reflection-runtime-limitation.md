# Reflection metadata limitation

Canonical stage transition: `stage reflect was not found`. Stage entry: `phase phase-46-native-sdk is already closed ... a closed phase is immutable`. Subsequent transition remained rejected. SDK canonical closure is CLOSED/PASS. No reopen, unsafe state-file edits, credential changes or new execution were attempted.

The command shell continued to the best-effort hook and handoff writer after the rejection. The hook persisted five reflection records and printed a completion-shaped line; neither is proof of canonical stage completion. The generated handoff is retained here as unaccepted and removed from active handoffs. Authored reflection explicitly records this limitation. A runtime-supported post-close Reflect stage path is needed to close this metadata gap.
