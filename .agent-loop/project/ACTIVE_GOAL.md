# Active Goal

Status: completed

Owner approval: requested and accepted in chat on 2026-05-07.

## Parent

- Intent: Improve The Agent Loop public surface.
- System: Public Surface; Project Operations.
- Milestone: post-v0.3 public README alignment.

## Outcome

Rewrite the root README so the public entry point is shorter, clearer, more specific about the value of The Agent Loop, and aligned with the v0.3 install flow.

## Done When

- [x] Root `README.md` explains the project in user-facing value terms instead of internal release-note terms.
- [x] The README keeps the v0.3 install flow concise and warns users to use the uploaded release ZIP asset.
- [x] The README stays clear that this repository is the source workspace, not the framework install to clone directly.
- [x] A better GitHub About text block is proposed to the owner.
- [x] Handoff and log state are updated.

## Scope

In scope:

- `README.md`
- `.agent-loop/START.md`
- `.agent-loop/project/ACTIVE_GOAL.md`
- `.agent-loop/project/logs/2026-05.md`

Out of scope:

- Editing or changing `releases/v0.3/.agent-loop/`.
- Updating the GitHub repository About field directly.
- Committing or pushing without an explicit request.

## Verification

```text
git diff --check
git status -sb
```
