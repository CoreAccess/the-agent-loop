# Atomic Memory Records

### AM-001

Type: claim
Statement: Every durable memory item should declare its type, tier, and scope.
Source: `source/02-kinds-of-memory.md` > The three axes
Why it matters: The future system needs these fields to avoid mixing what a memory contains, how expensive it is to load, and who it belongs to.
Confidence: high
Status: active
Tags: taxonomy, schema, memory-model

### AM-002

Type: claim
Statement: File role is a separate memory axis from cognitive memory type.
Source: `source/02-kinds-of-memory.md` > How real systems map onto the axes
Why it matters: The system should distinguish source, index, log, schema, and synthesized memory roles even when the content type is semantic or episodic.
Confidence: high
Status: active
Tags: file-roles, taxonomy, schema

### AM-003

Type: workflow-rule
Statement: Durable memory should default to archival tier unless per-turn relevance justifies core loading.
Source: `source/02-kinds-of-memory.md` > Patterns to borrow for our framework
Why it matters: This limits steady token cost and prevents always-loaded memory from crowding the active task context.
Confidence: high
Status: active
Tags: archival-default, context-budget, retrieval

### AM-004

Type: workflow-rule
Statement: Always-loaded project rules belong in `AGENTS.md`, while task-specific procedural playbooks belong in skills.
Source: `source/02-kinds-of-memory.md` > Re-grill decisions applied
Why it matters: This keeps mandatory behavior close to the project while avoiding a bloated core prompt.
Confidence: high
Status: active
Tags: procedural-memory, core-tier, file-role

### AM-005

Type: workflow-rule
Statement: The save policy should reject by default unless a memory candidate passes a durable-value test.
Source: `source/03-what-to-save-and-when.md` > Patterns to borrow for our framework
Why it matters: The source warns that indiscriminate saving creates noisy stores that reduce retrieval precision.
Confidence: high
Status: active
Tags: save-policy, bloat, quality-gate

### AM-006

Type: workflow-rule
Statement: Durable memories should be drafted during Reflect and written only after human approval.
Source: `source/03-what-to-save-and-when.md` > Re-grill decisions applied
Why it matters: Human approval is the trust gate that prevents low-quality or hallucinated durable memory from becoming project truth.
Confidence: high
Status: active
Tags: reflect, human-approval, durable-memory

### AM-007

Type: constraint
Statement: Every memory record needs a source stamp that identifies the session, commit, file, issue, or user confirmation behind it.
Source: `source/03-what-to-save-and-when.md` > Re-grill decisions applied
Why it matters: Source stamps make memories auditable and support later consolidation or supersession.
Confidence: high
Status: active
Tags: source-stamp, audit, trust

### AM-008

Type: claim
Statement: Atomic records are the dominant shape for queryable durable memory.
Source: `source/03-what-to-save-and-when.md` > What shape does the saved item take?
Why it matters: One durable idea per record is easier to search, update, source-stamp, and retrieve without extra context bloat.
Confidence: high
Status: active
Tags: atomic-records, retrieval, schema

### AM-009

Type: workflow-rule
Statement: Just-in-time retrieval should be the default context-loading strategy.
Source: `source/04-what-to-load-and-when.md` > Just-in-time retrieval
Why it matters: The future agent should load relevant memory on demand instead of preloading the whole store into the context window.
Confidence: high
Status: active
Tags: jit, retrieval, context-loading

### AM-010

Type: risk
Statement: Index-driven retrieval fails when memory index hooks or filenames are vague.
Source: `source/04-what-to-load-and-when.md` > Patterns to borrow for our framework
Why it matters: The planned v1 retrieval mechanism depends on the agent choosing the right file from short hooks and descriptive names.
Confidence: high
Status: active
Tags: index-hygiene, retrieval-risk, filenames

### AM-011

Type: risk
Statement: Core context is scarce because long prompts can suffer lost-in-the-middle attention loss.
Source: `source/04-what-to-load-and-when.md` > The lost-in-the-middle problem
Why it matters: Adding more always-loaded memory can reduce, rather than improve, the agent's effective attention.
Confidence: high
Status: active
Tags: context-bloat, attention, core-tier

### AM-012

Type: workflow-rule
Statement: Reflect is the primary moment for distilling episodic session evidence into durable semantic memory.
Source: `source/05-keeping-memory-healthy.md` > Patterns to borrow for our framework
Why it matters: The future system needs a repeatable place where raw work trails become concise memories.
Confidence: high
Status: active
Tags: reflect, distillation, episodic-to-semantic

### AM-013

Type: workflow-rule
Statement: Memory proposals should be classified as ADD, UPDATE, DELETE, or NOOP.
Source: `source/05-keeping-memory-healthy.md` > Operation 2 - Consolidation
Why it matters: This vocabulary forces the agent to handle duplicates, contradictions, and irrelevant candidates before writing memory.
Confidence: high
Status: active
Tags: consolidation, duplicate-control, reflect

### AM-014

Type: workflow-rule
Statement: Memory health checks should scan for contradictions, orphan entries, broken links, stale entries, and format violations.
Source: `source/05-keeping-memory-healthy.md` > Operation 4 - Lint / health check
Why it matters: A small human-readable memory store still needs maintenance to stay trustworthy.
Confidence: high
Status: active
Tags: lint, health-check, maintenance

### AM-015

Type: constraint
Statement: The system should not automatically delete or expire memory in v1.
Source: `source/05-keeping-memory-healthy.md` > Re-grill decisions applied
Why it matters: User review preserves trust when cleanup touches project knowledge that may still matter.
Confidence: high
Status: active
Tags: deletion, human-review, trust

### AM-016

Type: constraint
Statement: V1 memory should be project-local rather than cross-project personal or team memory.
Source: `source/06-memory-boundaries.md` > Re-grill decisions applied
Why it matters: Project-local scope reduces leakage risk and matches the minimal single-agent design target.
Confidence: high
Status: active
Tags: scope, project-local, v1

### AM-017

Type: constraint
Statement: Memory files must not contain credentials, API keys, tokens, secrets, or unredacted PII.
Source: `source/06-memory-boundaries.md` > Privacy, security, and PII
Why it matters: Memory is retrievable by design, so sensitive data would create a persistent exposure risk.
Confidence: high
Status: active
Tags: security, privacy, pii

### AM-018

Type: storage-guidance
Statement: Repo markdown is the default v1 backend for project memory.
Source: `source/07-storage-backends.md` > Backend pattern 1 - Markdown files in the repo
Why it matters: Markdown is portable, inspectable, versionable, and sufficient for a minimal project memory system.
Confidence: high
Status: active
Tags: markdown, backend, v1

### AM-019

Type: storage-guidance
Statement: Storage should graduate when retrieval failure and maintenance burden become real, not merely when a rough size threshold is crossed.
Source: `source/07-storage-backends.md` > Graduation triggers
Why it matters: The future system should not introduce SQLite, Postgres, vectors, or graph storage before the pain justifies the complexity.
Confidence: high
Status: active
Tags: graduation, storage-ladder, yagni

### AM-020

Type: storage-guidance
Statement: Markdown memory schema should include migration-ready metadata such as type, kind, scope, tier, source, timestamps, and status.
Source: `source/07-storage-backends.md` > Recommended v1 file schema
Why it matters: Cheap metadata in files makes later migration to SQLite, Postgres, or a memory service less lossy.
Confidence: high
Status: active
Tags: schema, migration, metadata

### AM-021

Type: workflow-rule
Statement: Every meaningful task should start from a lightweight Goal Packet.
Source: `source/08-goal-systems-and-decision-loops.md` > Add a Goal Packet
Why it matters: The agent needs objective, why, success criteria, constraints, resources, stop conditions, and memory candidates before acting on large goals.
Confidence: high
Status: active
Tags: goal-packet, planning, bounded-agency

### AM-022

Type: workflow-rule
Statement: The Goal Packet's "why" should be treated as control data, not motivational prose.
Source: `source/08-goal-systems-and-decision-loops.md` > Treat "Why" As Control Data
Why it matters: The reason for the goal changes technical choices, tradeoffs, verification, and scope.
Confidence: high
Status: active
Tags: why, control-data, decision-making

### AM-023

Type: constraint
Statement: Agent loops must be finite and include attempt limits, budgets, failure thresholds, escalation triggers, and stop conditions.
Source: `source/08-goal-systems-and-decision-loops.md` > Make Loops Finite
Why it matters: Finite loops prevent endless activity from replacing measurable progress.
Confidence: high
Status: active
Tags: loops, stop-conditions, resource-budget
