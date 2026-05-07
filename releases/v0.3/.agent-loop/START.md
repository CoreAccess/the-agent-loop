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

- Project state is not initialized yet.
- Root `AGENTS.md` points to `.agent-loop/START.md`.
- Workflow procedures are split under `.agent-loop/workflows/`; load only the workflow needed for the selected mode or current task.
- If onboarding resumes, load `.agent-loop/workflows/intake.md` and ask `Question 1`.

## Known Environment

- Check `.agent-loop/project/OBSERVATIONS.md` before commands for active skip rules.

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
