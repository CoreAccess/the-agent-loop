# Active Goal

Status: completed

Owner approval: accepted in chat on 2026-05-06.

## Parent

- Intent: Self-apply The Agent Loop v0.2 to build v0.3.
- System: Project operations.
- Milestone: v0.2 self-application cleanup.

## Outcome

Prepare this repository to use the v0.2 `.agent-loop/project/` model as its active operating system for v0.3 work.

## Done When

- [x] Root `.agent-loop/` exists and is initialized from the finished v0.2 scaffold.
- [x] Root `AGENTS.md` is only the v0.2 adapter.
- [x] Current intent, roadmap, active goal, system map, observations, and handoff live under `.agent-loop/project/`.
- [x] Useful experiment lessons are preserved in `docs/case-studies/`.
- [x] Raw `experiments/`, root `memory/`, root `STATUS.md`, root `BACKLOG.md`, and root `DECISIONS.md` are removed.
- [x] Root `README.md` describes the cleaned repository shape and v0.2/v0.3 status.
- [x] Git diff is reviewed, validation checks passed, and workspace cleanliness will be verified after commit.

## Scope

In scope:

- Root `.agent-loop/` project state.
- Root `AGENTS.md`.
- Root `README.md`.
- `docs/case-studies/`.
- Removal of legacy root state and raw experiment capsules after distillation.

Out of scope:

- Editing frozen release source in `releases/v0.1/` or `releases/v0.2/`.
- Designing v0.3 feature changes beyond capturing likely next goals.
- Publishing a new release.

## Stop Conditions

- A file targeted for deletion contains unique, undistilled decisions or evidence.
- Git shows unrelated user changes.
- The cleanup would remove release artifacts or public docs needed for install/use.

## Verification

```text
git status -sb
git diff --stat
git diff --check
tar -tf releases/v0.2/v0.2.zip
```
