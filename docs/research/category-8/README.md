# Category 8 - Change Gates and Guardrails

Date started: 2026-05-02

## Scope

Category 8 covers the enforcement side of agent behavior:

- permission profiles;
- always/ask/never rules;
- blast-radius boundaries;
- high-impact action gates;
- large rework/refactor stop rules;
- cleanup/deletion discipline;
- sandboxing, rollback, and external access.

This category is intentionally separate from Category 1 - Agent Contract. Category 1 defines the contract and authority model. Category 8 defines when actions are allowed, blocked, reviewed, or escalated.

## Current Docs

- `1-permission-models-and-autonomy.md`
- `2-high-impact-actions-and-stop-rules.md`
- `3-change-size-refactors-and-cleanup.md`
- `4-sandboxing-rollback-and-external-access.md`
- `5-developer-pain-and-reference-implementations.md`
- `6-v0.1-guardrail-adoption.md`

## Early Synthesis

The decided v0.1 posture:

> Default to meaningful autonomy inside the project workspace for clear local code changes. Stop before irreversible, external, privileged, broad, ambiguous, or contradiction-heavy actions.

This supports the user's preference for agent freedom while using blast radius, reversibility, and consequence as the real gates.

## Re-Grill Decisions

- v0.1 default permission posture is **Local Build**: autonomous read/edit inside workspace plus known local project commands.
- Ask before dependency changes, network/API calls beyond research browsing, external side effects, broad/destructive deletion, writes outside workspace, auth/security/data/infra/CI/permission changes, git history changes, broad refactors, architecture changes, or continuing through project-memory contradictions.
- Never store secrets/credentials/PII in memory or docs, silently delete/overwrite/revert user work, run destructive commands outside workspace, bypass gates by editing gate files, obey untrusted conflicting instructions, claim completion without evidence, or make production/account-affecting external changes without current-session approval.
- Deploys and external API calls are default-ask in v0.1. Public-doc research browsing is allowed for research tasks, but package installs, account/project API calls, deploys, publishes, pushes, and production-affecting commands require approval with command/API, target, expected effect, rollback path, and rationale.
- Large rework uses a hybrid approval threshold based on subsystem count, high-risk domains, rough file/diff size, mixed refactor+behavior changes, dependency replacement, architecture changes, migration/rollback needs, verification difficulty, ownership ambiguity, and doc/memory contradiction. Numeric size is only a weak signal.
- Cleanup is required in both Build and Reflect. Build cleanup handles code/tests/docs/config/fixtures/dependencies when removing or replacing behavior. Reflect handles broader project hygiene.
- Autonomous deletion is allowed inside the workspace after evidence when deletion is requested or clearly required, references were searched, affected tests/docs/config updated, verification run or explained, and deletion summarized. Ask for unclear ownership, public/API/auth/security/infra/data/config risk, dynamic use, broad/recursive deletion, user uncommitted work, or weak test coverage.
- Checkpoints are recommended by default. Sandboxing is required only for high-autonomy or risky execution profiles.
- Guardrail rules split by authority/frequency: `AGENTS.md` gets always-on gates, `Goal` gets task-specific permissions and exceptions, `STATUS.md` gets current state and blocked approvals, skills get reusable checklists, and `.agent-loop` holds future scaffold templates.

## Adoption

Experiment 004 validated the core guardrail posture with a 23/24 strong pass. The Category 8 guardrails are adopted for v0.1 scaffold design with one tightening: actors must explicitly record git/dirty state and checkpoint status before significant edits.
