---
name: stale-contradiction-handling-fixture
description: Test fixture for handling contradictions, supersession, and backend default conflicts.
type: procedural
kind: decision
scope: project
tier: archival
source: input/experiment-001-goal-packet.md > Stop Conditions and Escalation Triggers; AM-013, AM-014, AM-015, AM-018, AM-019
created: 2026-05-02
updated: 2026-05-02
status: active
confidence: high
tags: [test-fixture, contradiction, supersession, backend, health-check]
supersedes:
fixture: true
---

# Fixture: Stale Contradiction Handling

## Statement

Repo markdown is the default v1 backend for project memory. A new candidate that says to use Postgres as the default backend for all projects contradicts this active memory and must not be blindly added.

## Rules

- Classify a contradictory candidate as `UPDATE`, `DELETE`, or `NOOP`; do not silently add it as another active truth.
- Record the contradiction in Reflect and ask for human review.
- If the new candidate is accepted, mark the older memory as `superseded` and set `supersedes` on the newer record.
- Do not automatically delete the older memory.
- Treat Postgres, vector, graph, or managed memory as graduation paths only when retrieval failure, maintenance burden, team scope, security, audit, or concurrency pain justifies the complexity.

## Why It Matters

Contradictory active memories make retrieval less trustworthy. Supersession preserves audit history without allowing two incompatible defaults to remain active.

## Source Anchor

- `input/experiment-001-goal-packet.md` > Non-Goals, Stop Conditions, and Escalation Triggers
- AM-013: classify proposals as ADD, UPDATE, DELETE, or NOOP.
- AM-014: health checks scan for contradictions and stale entries.
- AM-015: do not automatically delete or expire memory in v1.
- AM-018: repo markdown is the default v1 backend.
- AM-019: storage graduates when real pain justifies complexity.

## Scenario Use

For a candidate saying "Use Postgres as the default backend for all projects," record the conflict, cite this fixture and the active Goal Packet, and ask for review before any supersession.

## Review Notes

This is a test fixture, not a real approved project memory.

