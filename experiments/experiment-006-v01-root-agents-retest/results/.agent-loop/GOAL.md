# Goal

## Objective


## Why


## Scope

In scope:

-

Out of scope:

-

## Acceptance Criteria

-

## Allowed Commands

Known local commands the agent may run under Local Build:

```text

```

## Constraints

- Work inside the project workspace.
- Use markdown project memory by default.
- Do not store secrets, credentials, API keys, tokens, or PII in memory or docs.
- Ask before dependency changes, external side effects, broad/deep refactors, and high-risk actions listed in `.agent-loop/AGENTS.md`.

## Resources And Budgets

- Retrieval attempts before escalation:
- Durable memory candidates per Reflect pass before asking for prioritization:
- Time or scope budget:

## Current Context


## Checklist

1. Read `.agent-loop/AGENTS.md`, `.agent-loop/STATUS.md`, `.agent-loop/GOAL.md`, and `.agent-loop/MEMORY.md`.
2. Create or carefully update root `AGENTS.md` so future prompts load The Agent Loop.
3. Select task-relevant memory from `.agent-loop/MEMORY.md`.
4. Inspect and record git/dirty state before significant edits.
5. Build inside the accepted scope.
6. Log notable work.
7. Check the result with the allowed verification commands.
8. Reflect before finishing.
9. Ask before adopting durable memory or broad scaffold rule changes.

## Stop Conditions

Stop and ask before:

- changing scope beyond this Goal;
- dependency install/upgrade/remove or lockfile changes;
- deploys, pushes, publishes, PRs, issue/comment writes, API calls, or production/account-affecting actions;
- broad deletion, destructive moves, or writes outside the workspace;
- auth/security/data/infra/CI/permission changes;
- broad refactors or architecture changes;
- continuing through contradictions in project memory or docs.

## Escalation Triggers

- Retrieval misses memory that should exist after index lookup and keyword search.
- A candidate memory contains sensitive data.
- A candidate contradicts active memory or may supersede a project decision.
- The agent wants to add non-default storage, automation, multi-agent orchestration, or external side effects.
- More durable memory candidates appear than the Reflect budget allows.

## Verification Criteria

-

## Memory Candidates

Use `.agent-loop/memory/proposed/` for durable candidates. Each candidate needs a source stamp, classification, rationale, risk, and human approval before becoming active durable memory.
