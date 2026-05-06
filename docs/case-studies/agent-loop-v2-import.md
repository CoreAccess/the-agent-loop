# Agent Loop v0.2 Import Case Study

Date: 2026-05-06

## Source

The owner imported a root `.agent-loop-v2/` folder from another active project and identified it as the practical v0.2 direction for The Agent Loop.

The imported folder was not a clean release scaffold. It mixed reusable framework improvements with live project state from the source project.

## Reusable Improvements

- A compact startup file: `.agent-loop/START.md`.
- A framework rule file separate from the boot instructions: `.agent-loop/RULES.md`.
- Reusable workflows in `.agent-loop/WORKFLOWS.md`.
- Explicit operating modes: Intake, Goal, Read-Only Audit, Change, and Exception.
- One executable active goal under `.agent-loop/project/ACTIVE_GOAL.md`.
- Accepted project direction under `.agent-loop/project/INTENT.md`.
- Roadmap and parking lot separated from active execution scope.
- System maps and optional system detail files for scalable project structure.
- Observations for recurring environment facts and command skip rules.
- Exception notes for durable evidence from failure loops or unsafe ambiguity.
- Stronger safe-deletion workflow and constructive challenge loop.

## Excluded From Release Source

- Live source-project handoff text.
- Source-project product name, business details, stack choices, local database notes, URLs, commands, logs, and legal/compliance notes.
- Monthly log history from the source project.

## Merge Result

Created `releases/v0.2/.agent-loop/` as a sanitized v0.2 draft source.

The draft keeps v0.1's package principle: the release asset should still contain only `.agent-loop/`, with root `AGENTS.md` created or carefully updated during onboarding.

v0.2 replaces v0.1's `GOAL.md`, `STATUS.md`, and `MEMORY.md` scaffold shape with a layered state model:

- `START.md` for startup and handoff
- `RULES.md` for always-on behavior
- `WORKFLOWS.md` for reusable procedures
- `project/INTENT.md` for accepted direction
- `project/ACTIVE_GOAL.md` for executable scope
- `project/ROADMAP.md` for future goals and parking lot
- `project/SYSTEM_MAP.md` plus `project/systems/` for scalable structure
- `project/OBSERVATIONS.md`, logs, and exception notes for durable operational evidence

## Validation Needed

- Blank-project onboarding should still create root `AGENTS.md` and ask one question at a time.
- Existing-project onboarding should merge only the marked root adapter block.
- A second prompt after root adapter creation should load the right v0.2 context without requiring the user to repeat the starter prompt.
- The layered model should reduce context noise rather than spreading state across too many files.
- Legacy v0.1 projects should receive a proposed migration path instead of silent deletion or overwrite of `GOAL.md`, `STATUS.md`, or `MEMORY.md`.
