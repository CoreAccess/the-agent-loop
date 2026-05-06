# Agent Starting Point

Updated:

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

- Project state is not initialized yet.
- Use Intake Mode to create or update root `AGENTS.md`, inspect the repository, ask a short one-question-at-a-time intake, and propose project intent plus one active goal before implementation.

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
