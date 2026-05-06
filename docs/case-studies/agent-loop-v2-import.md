# Agent Loop v0.2 Import Case Study

Date: 2026-05-06
Status: compact applied-evidence note

## Required Context

The owner imported a root `.agent-loop-v2/` folder from another active project and identified it as the practical v0.2 direction. The imported folder mixed reusable framework improvements with live source-project state, so it had to be sanitized before release.

v0.2 is now locked as the finished active scaffold release. Future product changes target v0.3 unless the owner explicitly approves a critical v0.2 packaging correction.

## Reusable Improvements

- `START.md` for startup and handoff.
- `RULES.md` for always-on framework behavior.
- `WORKFLOWS.md` for reusable procedures.
- Explicit modes: Intake, Goal, Read-Only Audit, Change, Exception.
- One executable active goal under `.agent-loop/project/ACTIVE_GOAL.md`.
- Accepted intent, roadmap, system map, observations, logs, and exception notes under `.agent-loop/project/`.
- Stronger safe-deletion and constructive-challenge rules.

## Excluded From Release Source

- Source-project product name, business details, stack choices, local URLs, commands, logs, and legal/compliance notes.
- Source-project handoff text and monthly log history.
- Any live state that would make the release scaffold project-specific.

## Applied Result

`releases/v0.2/.agent-loop/` became the sanitized release source. The release package principle stayed intact: the uploaded asset should contain only `.agent-loop/`, while onboarding creates or carefully updates root `AGENTS.md`.

## Revisit Triggers

- Designing the v0.3 release process.
- Creating a migration path for v0.1 projects.
- Checking whether the layered model reduces context noise or spreads state across too many files.
