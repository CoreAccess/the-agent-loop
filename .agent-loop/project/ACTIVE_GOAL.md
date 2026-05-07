# Active Goal

Status: completed

Owner approval: requested and accepted in chat on 2026-05-07.

## Parent

- Intent: Self-apply The Agent Loop v0.3.
- System: Release Packages; Public Surface; Project Operations.
- Milestone: v0.3 release alignment.

## Outcome

Adopt the locked v0.3 release candidate as the active project operating model, update the root public README for the simpler v0.3 install flow, and publish the aligned repository state to GitHub.

## Done When

- [x] `releases/v0.3/.agent-loop/` is treated as locked and remains unmodified.
- [x] Root `AGENTS.md` points future sessions directly to `.agent-loop/START.md`.
- [x] Root `.agent-loop/` uses v0.3-style workflow files under `.agent-loop/workflows/`.
- [x] Root `README.md` describes v0.3 as the active install target and uses the simpler starter prompt.
- [x] Project state, handoff, and logs reflect v0.3 as the active self-application version.
- [x] Repository changes are committed and pushed to GitHub.
- [x] A one-line human-readable GitHub Releases description is provided to the owner.

## Scope

In scope:

- `README.md`
- `AGENTS.md`
- `.agent-loop/`
- `docs/research/humanlayer-codelayer-agent-workflows.md`
- `releases/v0.3/`
- `.gitignore`

Out of scope:

- Editing or changing `releases/v0.3/.agent-loop/`.
- Uploading the v0.3 ZIP asset to GitHub Releases.

## Verification

```text
git diff --check
rg -n "\\.agent-loop/AGENTS\\.md|\\.agent-loop/WORKFLOWS\\.md" AGENTS.md README.md .agent-loop --hidden --glob "!**/ACTIVE_GOAL.md"
git status -sb
```
