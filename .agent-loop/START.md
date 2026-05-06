# Agent Starting Point

Updated: 2026-05-06

## Load First

- `.agent-loop/RULES.md`
- `.agent-loop/project/INTENT.md`
- `.agent-loop/project/ACTIVE_GOAL.md`
- `.agent-loop/project/OBSERVATIONS.md`

## Startup Decision

- Use Read-Only Audit Mode for inspect, review, stress-test, flaw-finding, or audit requests unless Exception Mode applies.
- Use Intake Mode when project intent is uninitialized, no accepted intent exists, or no executable active goal exists.
- Use Goal Mode when accepted project intent and one active executable goal exist.
- Use Change Mode when the owner asks to change Agent Loop framework files.
- Exception Mode takes precedence for unknown large issues, failure loops, conflicts, unsafe ambiguity, or impossible requirements.

## Current Handoff

- This repository now self-applies The Agent Loop v0.2 to build v0.3.
- v0.2 is locked as the finished active release baseline. Do not change `releases/v0.2/.agent-loop/` except for an explicitly approved critical release packaging fix.
- Root `AGENTS.md` is now only the v0.2 adapter. Active project state lives under `.agent-loop/project/`.
- Legacy root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, root `memory/`, and raw `experiments/` were removed after their useful state was distilled.
- Current active goal is completed. Next session should choose the first v0.3 improvement goal from `.agent-loop/project/ROADMAP.md`.

## Known Environment

- Check `.agent-loop/project/OBSERVATIONS.md` before commands for active skip rules.
- Record recurring command failures, sandbox notes, or local setup facts in `.agent-loop/project/OBSERVATIONS.md`.

## Load Only If Needed

- Project roadmap: `.agent-loop/project/ROADMAP.md`.
- Project system map: `.agent-loop/project/SYSTEM_MAP.md`.
- System detail files: `.agent-loop/project/systems/`.
- Framework workflow definitions: `.agent-loop/WORKFLOWS.md`.
- Templates: `.agent-loop/templates/`.
- Project logs: `.agent-loop/project/logs/`.
- Exception notes: `.agent-loop/project/exceptions/`.
