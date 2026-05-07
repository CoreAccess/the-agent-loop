# Agent Starting Point

Updated: 2026-05-07

## Framework Bootstrap

Read `Load First`, then apply `Startup Decision`.

## Load First

- `.agent-loop/RULES.md`
- `.agent-loop/project/INTENT.md`
- `.agent-loop/project/ACTIVE_GOAL.md`
- `.agent-loop/project/OBSERVATIONS.md`

## Startup Decision

- Use Read-Only Audit Mode for inspect, review, stress-test, flaw-finding, or audit requests unless Exception Mode applies.
- Use Change Mode when the owner asks to change Agent Loop framework files.
- Use Intake Mode when project intent is uninitialized, no accepted intent exists, or no executable active goal exists.
- Use Goal Mode when accepted project intent and one active executable goal exist.
- Exception Mode takes precedence for unknown large issues, failure loops, conflicts, unsafe ambiguity, or impossible requirements.

## Current Handoff

- This repository now self-applies The Agent Loop v0.3.
- v0.3 is locked as the finished active release source. Do not edit or change `releases/v0.3/.agent-loop/` unless the owner explicitly unlocks it.
- v0.2 and v0.1 remain frozen baselines. Do not change their release source folders except for an explicitly approved critical packaging fix.
- Root `AGENTS.md` is now only the v0.3 adapter and points directly to `.agent-loop/START.md`.
- Workflow procedures are split under `.agent-loop/workflows/`; load only the workflow needed for the selected mode or current task.
- Active project state lives under `.agent-loop/project/`.
- Legacy root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, root `memory/`, and raw `experiments/` were removed after their useful state was distilled.
- Deep research docs now use topic-first folder names: `project-bootstrap-and-onboarding/`, `memory-systems/`, and `change-gates-and-guardrails/`.
- Docs navigation/loading guidance lives in `.agent-loop/project/systems/research-and-evidence.md`; do not recreate docs `README.md` files by default.
- v0.1-era research docs were compressed into compact evidence briefs. Full historical drafts remain available in git history.
- HumanLayer/CodeLayer orientation research was captured in `docs/research/humanlayer-codelayer-agent-workflows.md`; revisit it before selecting planning, reusable skills, validation, context loading, external memory, multi-agent orchestration, or control-plane tooling work.
- Current active goal is completed: root README public-surface refresh and GitHub About copy suggestion.
- Next session should choose the first post-v0.3 improvement goal from `.agent-loop/project/ROADMAP.md`.

## Known Environment

- Check `.agent-loop/project/OBSERVATIONS.md` before commands for active skip rules.
- Record recurring command failures, sandbox notes, or local setup facts in `.agent-loop/project/OBSERVATIONS.md`.

## Load Only If Needed

- Workflow chooser: `.agent-loop/workflows/INDEX.md`.
- Intake workflow: `.agent-loop/workflows/intake.md`.
- Planning workflow: `.agent-loop/workflows/planning.md`.
- Execution workflow: `.agent-loop/workflows/execution.md`.
- Safe deletion workflow: `.agent-loop/workflows/safe-deletion.md`.
- Reflection workflow: `.agent-loop/workflows/reflection.md`.
- Project roadmap: `.agent-loop/project/ROADMAP.md`.
- Project system map: `.agent-loop/project/SYSTEM_MAP.md`.
- System detail files: `.agent-loop/project/systems/`.
- Templates: `.agent-loop/templates/`.
- Project logs: `.agent-loop/project/logs/`.
- Exception notes: `.agent-loop/project/exceptions/`.
