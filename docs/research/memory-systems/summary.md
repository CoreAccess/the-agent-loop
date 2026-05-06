# Category 6 - Memory Systems

Date: 2026-04-28
Status: deep research complete; v0.2 decisions applied

## Required Context

Category 6 defines what project memory should store, when it should be loaded, and how it stays useful without bloating context.

The durable model has four useful axes:

- Type: semantic, episodic, procedural, reference.
- Tier: core, recall, archival.
- Scope: project in v1; personal and team are future or project-local approximations.
- File role: startup/index, active state, log, system detail, source-backed evidence, template.

The main principle is just-in-time loading. Always-loaded files should stay small. Everything else should be loaded only when the current task needs it.

## Applied Implications

- `.agent-loop/AGENTS.md`, `.agent-loop/START.md`, and `Load First` files form the core tier.
- `.agent-loop/project/ROADMAP.md`, `SYSTEM_MAP.md`, system details, logs, templates, and docs are loaded on demand.
- Durable memory is project-local in v0.2. Cross-project personal memory and team memory are future scope.
- Save less, but save better: handoff/log updates may be automatic, while durable lessons should be distilled and source-stamped.
- Reflection should consolidate stale docs, dead questions, obsolete memory, temp files, contradictions, and experiment artifacts.
- Markdown remains the default backend because it is inspectable, portable, versionable, and sufficient for the current project scale.

## Source Basis

- Karpathy LLM-maintained wiki pattern: index, source pages, append-only log, and lint.
- Anthropic memory tool docs: memory is archival by default and should be loaded on demand.
- Databricks memory research: episodic versus semantic memory and personal versus organizational scope.
- Letta/MemGPT: core, recall, and archival tier model.
- mem0: atomic memories, ADD/UPDATE/DELETE/NOOP consolidation vocabulary, source-stamped memory operations.
- LangGraph/LangMem: long-term memory separated from short-term thread state.
- Cloudflare Agent Memory: constrained memory API and layered storage roles.
- pgvector/Postgres/SQLite research: graduate storage only when retrieval failure or product requirements justify it.

## Revisit Triggers

- Context loading becomes unreliable with the current file-based approach.
- `.agent-loop/project/` grows enough that startup cost or retrieval misses become visible.
- v0.3 adds a formal memory schema, lint workflow, or local MCP memory bridge.
- A public guide needs migration advice from markdown into SQLite/Postgres/managed memory.
