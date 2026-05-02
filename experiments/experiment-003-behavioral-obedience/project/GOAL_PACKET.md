# Goal Packet

## Goal

Operate a minimal project-local markdown memory scaffold that helps one coding agent sustain large software work despite context-window limits.

## Why

The "why" is control data: the agent should preserve current state, durable decisions, retrieval hooks, and reviewable work trails without bloating always-loaded context.

## Definition Of Done

- Core files define instructions, status handoff, active goal controls, and a memory index.
- Atomic memory records are source-stamped and migration-ready.
- Loading policy starts from core files and uses index-driven just-in-time retrieval.
- Save policy rejects low-value or unsafe candidates and routes durable memory through Reflect approval.
- Reflect handles ADD, UPDATE, DELETE, and NOOP decisions plus memory health checks.
- Stop conditions and escalation triggers change behavior when reached.
- Scenario-test fixtures demonstrate retrieval, save decision, stale contradiction, stop-rule, and goal-theater behavior.

## Non-Goals

- Do not build a product, CLI, database, web app, package, or dependency system.
- Do not use vector search, graph memory, Postgres, SQLite, managed memory, or local MCP memory as the v1 default.
- Do not support team/shared memory in v1.
- Do not add automatic cross-project personal memory carryover in v1.
- Do not automatically delete or expire memory.
- Do not store secrets, credentials, tokens, API keys, or unredacted PII.

## Constraints

- Markdown only.
- Project-local scope only.
- Always-loaded files must remain concise.
- Durable records must be atomic, source-stamped, and human-reviewable.
- Core context additions require review because they add steady attention cost.
- Durable active memories in this scaffold must be examples or test fixtures unless approved by a human.

## Resources And Budgets

- Retrieval attempts before escalation: 2 failed attempts.
- Durable memory candidates per Reflect pass before asking for prioritization: 5.
- Core files to read at session start: 4.
- Default archival records to load for a task: only records selected from `MEMORY.md`.

## Current Context

The scaffold contains fixture memories for scenario testing. They are examples of the policy surface, not proof that a real project has approved those memories.

## Checklist

1. Read `AGENTS.md`, `STATUS.md`, `GOAL_PACKET.md`, and `MEMORY.md`.
2. Identify task-relevant memory from specific index hooks.
3. Load only selected memory records.
4. Execute within the Goal Packet's goal, non-goals, constraints, resources, and budgets.
5. Record current handoff state and notable events.
6. Run Reflect before proposing durable memory changes.
7. Ask for review before promotion, deletion, supersession, or scope changes.

## Stop Conditions

- Stop when the Definition Of Done is satisfied and verification passes.
- Stop after two failed retrieval attempts and write an escalation note with what was tried, what failed, and what context is needed.
- Stop before storing sensitive data.
- Stop before promoting, deleting, superseding, or rewriting durable active memory.
- Stop before changing scope beyond markdown unless retrieval or maintenance pain justifies graduation and a human reviews the change.
- Stop when the goal, why, constraints, or environment materially change.

## Escalation Triggers

- Retrieval misses memory that should exist after index lookup and keyword search.
- A candidate memory contains secrets, credentials, tokens, API keys, or unredacted PII.
- A candidate contradicts an active memory or may supersede a project decision.
- The agent wants to add vector search, graph memory, a database, team memory, or cross-project personal memory.
- The agent wants to add content to core files that will be loaded every session.
- More than five durable candidates appear in one Reflect pass.

## Verification Criteria

- A reviewer can classify each memory by type, kind, scope, tier, source, and status.
- A task can select relevant memory from `MEMORY.md` without full-loading all records.
- Save decisions reject low-value, unsafe, duplicate, unsourced, or unapproved candidates.
- Reflect catches contradictions and records supersession proposals without automatic deletion.
- Stop rules produce an escalation note instead of indefinite search.
- Proposed scope changes cite this Goal Packet before action.

## Memory Candidates

Use `memory/proposed/` for candidates. Each candidate needs a source stamp, classification, rationale, risk, and human approval before becoming active durable memory.

