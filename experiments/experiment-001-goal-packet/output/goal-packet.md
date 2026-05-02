# Goal Packet

## Goal

Design a minimal project-local memory and context system for The Agent Loop that lets a single coding agent sustain work on large software projects despite context-window limits. The design should use source-stamped atomic memory records, a small always-loaded index/status layer, just-in-time loading of archival records, Reflect-gated memory distillation, finite work loops, and reviewable work trails.

Inference from:
- `source/02-kinds-of-memory.md` > The three axes
- `source/03-what-to-save-and-when.md` > Patterns to borrow for our framework
- `source/04-what-to-load-and-when.md` > Just-in-time retrieval
- `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
- `source/07-storage-backends.md` > Backend pattern 1 - Markdown files in the repo
- `source/08-goal-systems-and-decision-loops.md` > Add a Goal Packet

## Why

Large software goals outlive a single context window, and agents can lose progress unless the system preserves current state, durable decisions, and retrieval hooks. Reflect closes the development loop into memory; just-in-time retrieval keeps active context focused on what is relevant; finite Goal Packets keep the agent from continuing without a bounded endpoint.

Inference from:
- `source/01-development-lifecycle.md` > Key Findings
- `source/04-what-to-load-and-when.md` > Just-in-time retrieval
- `source/08-goal-systems-and-decision-loops.md` > Why This Matters

## Definition Of Done

- A v1 memory schema is defined for markdown records with `name`, `description`, `type`, `kind`, `scope`, `tier`, `source`, `created`, `updated`, and `status`, plus optional `supersedes`, `confidence`, `expires`, and `tags`.
  Source: `source/07-storage-backends.md` > Recommended v1 file schema
- A project memory layout is defined with core scaffolding, an index, archival atomic records, recall logs, and current status handoff state.
  Inference from:
  - `source/02-kinds-of-memory.md` > How real systems map onto the axes
  - `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
  - `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
- A save policy is defined that uses bounded automatic status/log updates, event-triggered candidates, and Reflect-phase human approval for durable memory writes.
  Source: `source/03-what-to-save-and-when.md` > Re-grill decisions applied
- A loading policy is defined that starts from index/status, loads only task-relevant memory, and broadens only when retrieval fails or the task requires more context.
  Source: `source/04-what-to-load-and-when.md` > Re-grill decisions applied
- A Reflect routine is defined for distillation, ADD/UPDATE/DELETE/NOOP classification, health checks, and goal review.
  Inference from:
  - `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
  - `source/08-goal-systems-and-decision-loops.md` > Add Goal Review To Reflect
- Stop conditions, escalation triggers, resource budgets, and verification criteria are part of the design, not left to agent improvisation.
  Source: `source/08-goal-systems-and-decision-loops.md` > Make Loops Finite

## Non-Goals

- Do not implement the memory system in this experiment.
  Source: `TASK.md` > Constraints
- Do not make vector search, graph memory, Postgres, managed memory APIs, or local MCP memory the v1 default.
  Source: `source/07-storage-backends.md` > Graduation ladder
- Do not support team/shared memory in v1.
  Source: `source/06-memory-boundaries.md` > Re-grill decisions applied
- Do not add automatic cross-project personal memory carryover in v1.
  Source: `source/06-memory-boundaries.md` > Re-grill decisions applied
- Do not automatically delete or expire memory.
  Source: `source/05-keeping-memory-healthy.md` > Re-grill decisions applied
- Do not store secrets, credentials, tokens, API keys, or unredacted PII in memory.
  Source: `source/06-memory-boundaries.md` > Privacy, security, and PII

## Constraints

- The design must be source anchored and bounded to the local corpus used for this experiment.
  Source: `source/source-manifest.md` > Corpus Rule
- Core context must stay small because always-loaded memory creates steady token cost and attention loss risk.
  Source: `source/04-what-to-load-and-when.md` > The lost-in-the-middle problem
- Durable records must be atomic, source-stamped, and human-reviewable.
  Inference from:
  - `source/03-what-to-save-and-when.md` > What shape does the saved item take?
  - `source/03-what-to-save-and-when.md` > Re-grill decisions applied
- V1 memory scope is project-local, with project-local personalization represented as `scope: project` plus `kind: personalization`.
  Source: `source/07-storage-backends.md` > Re-grill decisions applied
- Storage must remain exportable to plain markdown or JSON.
  Source: `source/07-storage-backends.md` > Security and portability

## Source Evidence

- The development lifecycle source says Reflect closes the loop into memory and that phase handoffs prevent work from falling through cracks.
  Source: `source/01-development-lifecycle.md` > Key Findings
- The memory taxonomy source says useful memory guidance needs type, tier, scope, and file-role distinctions.
  Source: `source/02-kinds-of-memory.md` > The three axes
- The save source says memory should be biased toward not-saving, source-stamped, atomic, and Reflect-gated for durable writes.
  Source: `source/03-what-to-save-and-when.md` > Patterns to borrow for our framework
- The loading source says the framework should default to just-in-time retrieval and keep full-load behavior to scaffolding.
  Source: `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
- The health source says memory maintenance needs distillation, consolidation, decay, and lint.
  Source: `source/05-keeping-memory-healthy.md` > Four maintenance operations
- The boundary source says v1 should be project-local, avoid secrets and PII, and reserve team memory for future work.
  Source: `source/06-memory-boundaries.md` > Patterns to borrow for our framework
- The storage source says repo markdown is the default v1 backend and graduation should follow real retrieval or maintenance pain.
  Source: `source/07-storage-backends.md` > Backend pattern 1 - Markdown files in the repo
- The goal-system source says meaningful work should be captured in a Goal Packet with objective, why, constraints, budgets, stop conditions, escalation triggers, and memory candidates.
  Source: `source/08-goal-systems-and-decision-loops.md` > Add a Goal Packet

## Proposed Memory Model

- `AGENTS.md`: core procedural rules for the project. Keep small and mandatory.
  Source: `source/02-kinds-of-memory.md` > Re-grill decisions applied
- `STATUS.md`: core current-state handoff with phase, completed work, next step, and open decisions.
  Source: `source/01-development-lifecycle.md` > Re-Grill Decisions
- `MEMORY.md`: core index with one row per durable memory and a high-quality one-line retrieval hook.
  Source: `source/02-kinds-of-memory.md` > Patterns to borrow for our framework
- `memory/*.md`: archival atomic memory records, one durable idea per file, with migration-ready frontmatter.
  Inference from:
  - `source/03-what-to-save-and-when.md` > What shape does the saved item take?
  - `source/07-storage-backends.md` > Recommended v1 file schema
- `memory/log.md`: recall layer for append-only notable session events, not full transcripts.
  Source: `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
- `memory/decisions.md` or decision records: project-scope durable decisions, versioned by git when available.
  Inference from:
  - `source/06-memory-boundaries.md` > Where memories should live
  - `source/05-keeping-memory-healthy.md` > Versioning and audit trails

Memory fields:

- `type`: semantic, episodic, procedural, or reference.
  Source: `source/07-storage-backends.md` > Recommended v1 file schema
- `scope`: project in v1; team reserved; personal deferred.
  Source: `source/07-storage-backends.md` > Re-grill decisions applied
- `tier`: core, recall, or archival, defaulting durable records to archival.
  Source: `source/02-kinds-of-memory.md` > Patterns to borrow for our framework
- `source`: session, commit, file, issue, URL, or user-confirmed source stamp.
  Source: `source/03-what-to-save-and-when.md` > Re-grill decisions applied
- `status`: active, superseded, deprecated, or equivalent lifecycle state.
  Source: `source/07-storage-backends.md` > Recommended v1 file schema
- `supersedes`: the only graph-style v1 hook.
  Source: `source/07-storage-backends.md` > Re-grill decisions applied

## Context-Loading Strategy

- Start each session from core scaffolding: project instructions, current status, the Goal Packet if active, and the memory index.
  Inference from:
  - `source/01-development-lifecycle.md` > Re-Grill Decisions
  - `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
- Use the memory index and descriptive filenames to select only task-relevant archival records.
  Source: `source/04-what-to-load-and-when.md` > Strategy B - Index-driven
- Use keyword search for exact terms, identifiers, decisions, file names, and error strings.
  Inference from:
  - `source/04-what-to-load-and-when.md` > Strategy C - Keyword / BM25 search
  - `source/07-storage-backends.md` > Graduation ladder
- Broaden context only when the index does not surface relevant memory, the task explicitly needs more history, or verification shows retrieval missed an existing record.
  Source: `source/04-what-to-load-and-when.md` > Re-grill decisions applied
- Keep core memory additions rare because core context costs tokens every turn and can suffer lost-in-the-middle attention loss.
  Source: `source/04-what-to-load-and-when.md` > The lost-in-the-middle problem
- Graduate to SQLite, Postgres, vector, graph, or managed memory only when retrieval failure, write concurrency, team scope, security, audit, or maintenance burden makes markdown insufficient.
  Source: `source/07-storage-backends.md` > Graduation triggers

## Checklist

1. Write a task-level Goal Packet with goal, why, done criteria, constraints, resources, loop rules, stop conditions, escalation triggers, and memory candidates.
   Source: `source/08-goal-systems-and-decision-loops.md` > Add a Goal Packet
2. Classify required memory files by role: core instructions, current status, index, archival atomic records, recall log, and decisions.
   Source: `source/02-kinds-of-memory.md` > How real systems map onto the axes
3. Define the markdown frontmatter schema and make every durable record migration-ready.
   Source: `source/07-storage-backends.md` > Recommended v1 file schema
4. Define save triggers: bounded status/log updates, explicit user signals, task completion, corrections, and Reflect candidates.
   Source: `source/03-what-to-save-and-when.md` > The trigger problem
5. Add a save quality gate that rejects small talk, transient reasoning, general definitions, duplicate facts, quickly expiring facts, secrets, and unsourced claims.
   Source: `source/03-what-to-save-and-when.md` > Re-grill decisions applied
6. Define the Reflect workflow for memory proposals, ADD/UPDATE/DELETE/NOOP classification, human approval, and goal review.
   Inference from:
   - `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
   - `source/08-goal-systems-and-decision-loops.md` > Add Goal Review To Reflect
7. Define the index standard: each row has a title, link, and specific one-line retrieval hook.
   Source: `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
8. Define a health check for contradictions, orphan memories, broken links, stale entries, and schema violations.
   Source: `source/05-keeping-memory-healthy.md` > Operation 4 - Lint / health check
9. Define storage graduation signals and keep vector or graph memory out of onboarding.
   Source: `source/07-storage-backends.md` > Graduation triggers
10. Verify the design with policy-focused scenarios, not only artifact completion.
    Source: `source/08-goal-systems-and-decision-loops.md` > Test Policy, Not Just Outcome

## Stop Conditions

- Stop when the Goal Packet's definition of done is satisfied and verification criteria pass.
  Source: `source/08-goal-systems-and-decision-loops.md` > Add a Goal Packet
- Stop and escalate when repeated retrieval attempts fail to find memory that should exist.
  Inference from:
  - `source/04-what-to-load-and-when.md` > Strategy B - Index-driven
  - `source/07-storage-backends.md` > Graduation triggers
- Stop and ask for review before writing, deleting, superseding, or promoting durable memory.
  Inference from:
  - `source/03-what-to-save-and-when.md` > Re-grill decisions applied
  - `source/05-keeping-memory-healthy.md` > Re-grill decisions applied
- Stop and ask the user when a memory candidate is ambiguous between reusable preference and project-only fact.
  Source: `source/06-memory-boundaries.md` > Cross-project user memory - practical structure
- Stop work on the current plan when evidence shows the goal, why, constraints, or environment changed materially.
  Source: `source/08-goal-systems-and-decision-loops.md` > Loops Are How Goals Survive Reality
- Stop a retry loop after the configured max attempts, cost/time budget, or failure threshold is reached.
  Source: `source/08-goal-systems-and-decision-loops.md` > Make Loops Finite

## Escalation Triggers

- A candidate memory contains sensitive data, credentials, PII, or project-private details whose storage location is unclear.
  Source: `source/06-memory-boundaries.md` > Privacy, security, and PII
- A new memory contradicts an active memory or may supersede a prior project decision.
  Source: `source/05-keeping-memory-healthy.md` > Operation 2 - Consolidation
- The agent wants to add content to core files such as `AGENTS.md` or `MEMORY.md`.
  Source: `source/04-what-to-load-and-when.md` > The lost-in-the-middle problem
- The memory store is producing retrieval misses, duplicate results, stale results, or index maintenance pain.
  Source: `source/07-storage-backends.md` > Graduation triggers
- The task starts to require team/shared memory, concurrent writes, row-level access control, or product-grade audit.
  Source: `source/07-storage-backends.md` > Backend pattern 3 - Postgres, usually with pgvector
- The agent cannot tell whether adaptation is signal-driven or a reaction to noise.
  Source: `source/08-goal-systems-and-decision-loops.md` > Gamble Lab Lessons

## Verification Criteria

- A reviewer can inspect the memory schema and classify each record by type, tier, scope, and file role.
  Source: `source/02-kinds-of-memory.md` > The three axes
- Given a sample task, the agent can identify which memory files to load from the index without full-loading the store.
  Source: `source/04-what-to-load-and-when.md` > Strategy B - Index-driven
- Given a candidate memory, the agent can reject, ADD, UPDATE, DELETE, or NOOP it with a source-stamped rationale.
  Inference from:
  - `source/03-what-to-save-and-when.md` > Patterns to borrow for our framework
  - `source/05-keeping-memory-healthy.md` > Operation 2 - Consolidation
- A Reflect pass produces memory candidates, a health-check result, and a goal-review note without writing durable memory before approval.
  Inference from:
  - `source/01-development-lifecycle.md` > Proposed Phase-by-Phase Framework Structure
  - `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
  - `source/08-goal-systems-and-decision-loops.md` > Add Goal Review To Reflect
- A failure scenario verifies that the agent stops after configured attempts or escalates when retrieval, verification, or security rules fail.
  Source: `source/08-goal-systems-and-decision-loops.md` > Make Loops Finite
- The design can export project memory to plain markdown or JSON.
  Source: `source/07-storage-backends.md` > Security and portability

## Risks

- Context bloat can make the agent less effective if too much memory is kept in core.
  Mitigation: default durable records to archival and keep only scaffolding in core.
  Source: `source/04-what-to-load-and-when.md` > The lost-in-the-middle problem
- Memory bloat can make retrieval worse if the system saves too many low-value items.
  Mitigation: reject by default and surface only high-confidence Reflect candidates.
  Source: `source/03-what-to-save-and-when.md` > Failure modes
- Hallucinated saves can become false ground truth.
  Mitigation: source-stamp every memory and require human approval for durable writes.
  Source: `source/03-what-to-save-and-when.md` > F2 - Hallucinated saves
- Stale or contradictory memories can mislead future sessions.
  Mitigation: classify proposals with ADD/UPDATE/DELETE/NOOP and use health checks for contradictions and staleness.
  Source: `source/05-keeping-memory-healthy.md` > Four maintenance operations
- Vague index hooks can hide existing memory from the agent.
  Mitigation: require specific one-line retrieval hooks and descriptive filenames.
  Source: `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
- Starting with vector or graph storage can add complexity before the project has retrieval pain.
  Mitigation: start with repo markdown and graduate only on clear signals.
  Source: `source/07-storage-backends.md` > Graduation triggers
- Project memory can leak sensitive data if secrets or PII are stored in retrievable files.
  Mitigation: refuse sensitive memory and review private/sensitive candidates during Reflect.
  Source: `source/06-memory-boundaries.md` > Privacy, security, and PII
- Open-loop work can continue after the goal has changed or failed.
  Mitigation: use finite loops, stop conditions, escalation triggers, and Reflect goal review.
  Inference from:
  - `source/01-development-lifecycle.md` > Key Findings
  - `source/08-goal-systems-and-decision-loops.md` > Make Loops Finite

## Research Gaps

- The corpus does not define the smallest useful Goal Packet for quick bug fixes.
  Source: `source/08-goal-systems-and-decision-loops.md` > Open Questions
- The corpus does not fully solve how to prevent "goal theater," where the agent writes a Goal Packet but ignores it.
  Source: `source/08-goal-systems-and-decision-loops.md` > Open Questions
- The corpus does not solve high-relevance staleness detection without human invalidation.
  Source: `source/05-keeping-memory-healthy.md` > Operation 3 - Decay / forgetting
- The corpus gives rough storage graduation signals but not validated thresholds for a large software project.
  Source: `source/07-storage-backends.md` > Graduation triggers
- The corpus defers multi-agent shared memory and write-conflict handling.
  Source: `source/06-memory-boundaries.md` > Multi-agent shared memory

## Memory Candidates To Preserve

- AM-001 through AM-004: memory taxonomy, file roles, archival default, and core procedural placement.
- AM-005 through AM-008: save policy, human approval, source stamps, and atomic record shape.
- AM-009 through AM-011: just-in-time retrieval, index hygiene, and core-context risk.
- AM-012 through AM-015: Reflect distillation, consolidation vocabulary, lint, and no automatic deletion.
- AM-016 through AM-020: project-local scope, security, markdown default, graduation triggers, and migration-ready schema.
- AM-021 through AM-023: Goal Packet, why as control data, and finite loops.

Each listed memory candidate carries its own source anchor in `output/atomic-memory.md`.
