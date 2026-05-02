# Sub-Category 6.6 - Storage Backends and Graduation

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 6 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

The first five Category 6 docs answer what memory is, what to save, what to load, how to maintain it, and where boundaries sit. This doc answers the implementation question:

**What should memory physically live in, and when should the framework graduate from one storage pattern to another?**

The research does not support a single universal backend. Real systems are converging on a layered answer:

- Files are best for small, human-readable project memory.
- SQLite is best for local-first searchable state and conversation history.
- Postgres is best for product-grade memory that needs transactions, filters, joins, auth, and operational maturity.
- Vector stores are best for large semantic search over prose.
- Graph stores are best only when relationships are first-class.
- Managed memory APIs are best when the user wants the memory pipeline, not just storage.

The framework's v1 audience is experienced solo developers and small projects, so the default should not be "install a vector database." It should be a low-friction path that starts with markdown and graduates only when the pain is real.

---

## Storage is not one thing

Several sources treat "memory backend" as if it means one database. That framing breaks down quickly. Production memory systems usually have multiple storage roles:

| Role | What it stores | Common backend |
|------|----------------|----------------|
| **Session state** | Current thread, tool calls, checkpoints, branch history | SQLite, Postgres, framework checkpointer |
| **Durable memory records** | Distilled facts, preferences, decisions, instructions | Markdown, JSON docs, SQLite, Postgres |
| **Search index** | Lexical or semantic index over records | FTS5, Postgres FTS, pgvector, Qdrant, Vectorize |
| **Graph layer** | Entity relationships and temporal links | Neo4j, Memgraph, Neptune, Kuzu, Apache AGE |
| **Artifact store** | Long documents, exports, snapshots, old logs | Files, object storage, repo docs |
| **Audit/version layer** | History of memory changes | Git, event table, supersession chain |

Cloudflare's Agent Memory is the clearest production example: raw messages and classified memories live in SQLite-backed Durable Objects, vectors live in Vectorize, and future snapshots/exports go to R2. That is a stack, not a single store.

For the framework, this means the storage recommendation should name the role first. "Use Postgres" is too vague. Better: "Use repo markdown for project decisions; use SQLite/FTS for local conversation history; use Postgres + pgvector if you are building a product memory layer."

---

## Backend pattern 1 - Markdown files in the repo

**How it works:** Memory is plain markdown with light frontmatter. A small index (`MEMORY.md`) is always loaded or easy to inspect. Individual memory files are loaded on demand.

**Used by:** Karpathy's wiki pattern, this project, many `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` setups, repo-local tools such as Squad-style `.squad/` memory.

**Best for:**
- Project decisions
- Agent instructions
- Architecture notes
- Handoff state
- Human-readable memory that should travel with the repo

**Pros:**
- Zero infrastructure.
- Works across Claude, Gemini, Codex, Cursor, and any agent that can read files.
- Human-reviewable in normal editor workflows.
- Versioned by git when the project is a git repo.
- Easy to diff, copy, delete, and migrate later.

**Cons:**
- Search is weak unless the agent uses `rg`/index discipline.
- No concurrent write protection.
- No real access control if committed to repo.
- Index hygiene is load-bearing.
- Retrieval quality depends on filename and one-line hook quality.

**Verdict for this framework:** default v1 project memory backend.

Markdown is not "less serious" than a database for this use case. It is the right first backend because the framework is a template and agent behavior contract, not an enterprise SaaS memory service.

---

## Backend pattern 2 - Local SQLite / embedded search

**How it works:** Memory records live in a local embedded database. Search is usually FTS5, sqlite-vec, or a small local embedding index. The agent talks to it through a CLI, MCP server, or app-specific tools.

**Used by:** Cloudflare Durable Object SQLite for session history and FTS, local-first MCP memory servers, many desktop coding-agent memory tools.

**Best for:**
- Local conversation history
- Fast full-text search
- Cross-session recall without cloud
- A local dashboard or inspector
- More records than markdown can comfortably index

**Pros:**
- Still local-first.
- Fast search without a service dependency.
- Better structured metadata than loose markdown.
- Can expose a stable MCP tool surface to multiple agents.

**Cons:**
- Less transparent than markdown.
- Requires a server, CLI, or tool bridge.
- Backup/export has to be designed.
- Human review is worse unless a UI exists.

**Practical signal from Cloudflare:** their Session API defaults conversation history to SQLite and uses SQLite FTS5 for built-in searchable context. That is strong evidence that embedded lexical search is enough for many agent-memory workloads before vectors enter the picture.

**Verdict for this framework:** optional v1 extension, not default. Useful for "I have many sessions and want recall" but too much machinery for a new repo template.

---

## Backend pattern 3 - Postgres, usually with pgvector

**How it works:** Memory records are rows. Metadata, scope, source stamps, versions, and access control live as normal columns. Semantic search is added through `pgvector`; lexical search uses Postgres full-text search or extensions; exact lookup uses indexes.

**Used by:** LangGraph `PostgresStore`, Databricks Lakebase for agent state/memory, many production RAG systems, pgvector-based application stacks.

**Best for:**
- Product-grade memory
- Multi-user memory
- Team or organization scope
- Strong metadata filtering
- Transactional writes
- Joins with application data
- Row-level security and audit needs

**Pros:**
- Mature operational story.
- ACID transactions, backups, point-in-time recovery, joins, and normal app auth.
- One database can hold facts, sessions, versions, source refs, access policies, and vectors.
- pgvector supports exact and approximate nearest-neighbor search while keeping vectors with relational data.

**Cons:**
- More setup than files or SQLite.
- Approximate vector indexes introduce recall/speed tuning.
- Query quality still depends on chunking, embeddings, metadata, and reranking.
- Can become "database as junk drawer" without memory health rules.

**Important distinction:** Postgres is not just "a vector DB alternative." For agent memory, its value is that memory records are structured operational data. Vectors are one index over that data, not the whole backend.

**Verdict for this framework:** recommended graduation target for serious app/product memory. Not the starter default.

---

## Backend pattern 4 - Dedicated vector database

**How it works:** Memory chunks are embedded and stored in a purpose-built vector database such as Qdrant, Chroma, Pinecone, Weaviate, Milvus, or Vectorize. Retrieval is semantic similarity, often combined with metadata filters, sparse search, or reranking.

**Used by:** Letta archival memory, mem0 default vector store choices, managed RAG stacks, Cloudflare Vectorize as one layer of Agent Memory.

**Best for:**
- Large unstructured prose
- Documentation repositories
- Research corpora
- Support history
- Cases where users ask semantically similar questions with different wording

**Pros:**
- Strong semantic retrieval over large text.
- Scales beyond what file indexes can handle.
- Rich vector DBs have filtering, payload metadata, hybrid search, and managed hosting.

**Cons:**
- Wrong default for small memory stores.
- Exact string recall can be worse than lexical search.
- Embedding dimension/model choices become operational concerns.
- Raw append-only vector memory degrades without consolidation, contradiction handling, and decay.
- Adds network/service dependency unless local.

**Practitioner pain:** Reddit and developer threads repeatedly surface two complaints: vector DBs feel like overkill for structured preferences/facts, and append-only vector stores degrade as duplicates, contradictions, and stale entries accumulate.

**Verdict for this framework:** use when the corpus is too large or fuzzy for index-driven markdown / SQLite / Postgres FTS. Do not make vector DB setup part of v1 onboarding.

---

## Backend pattern 5 - Graph memory

**How it works:** Memory entries also become entities and relationships. Graph traversal helps answer "who did what with whom," "what caused what," "which decision superseded this one," or "how are these project facts connected?"

**Used by:** mem0 Graph Memory, mcp-memory-service typed knowledge graph, MemLayer-style memory graphs, academic memory systems.

**Best for:**
- Multi-hop relationship questions
- Team/org memory
- Causal histories
- Compliance/audit questions
- Multi-agent shared context

**Pros:**
- Captures relationships vectors blur together.
- Useful for temporal and causal reasoning.
- Supports explicit contradiction/supersession edges.

**Cons:**
- Dynamic graph growth is hard to control.
- Entity extraction errors become structural errors.
- Relationship pruning becomes a maintenance burden.
- Graph context can balloon at retrieval time.
- Many use cases work fine with source-stamped rows and tags.

Mem0's own docs are conservative here: routine conversations can stay vector-only to save latency, and graph users need pruning policies for stale relationships. That is the right posture.

**Verdict for this framework:** v2 / advanced. Add the `supersedes` hook now so replacement/invalidation is possible later, but do not add broad manual relationship fields or ship graph memory as the default.

---

## Backend pattern 6 - Managed memory API / MCP memory service

**How it works:** The agent does not talk to files or raw databases. It gets a constrained API: remember, recall, forget, list, ingest. The service handles extraction, deduplication, indexing, reranking, consolidation, exports, and sometimes team sharing.

**Used by:** Cloudflare Agent Memory, Letta archival memory, mem0 platform, mcp-memory-service, Memorix-style MCP memory bridges.

**Best for:**
- Teams
- Multiple coding agents sharing memory
- Users who want memory as a product capability
- Workflows where the memory pipeline matters more than storage choice

**Pros:**
- Constrained tools keep the model focused on the task instead of database strategy.
- Can centralize memory across Claude, Gemini, Codex, Cursor, and CI agents.
- Can implement extraction, verification, supersession, and export in one place.
- Better UX when paired with dashboard / inspector.

**Cons:**
- Another service to trust and operate.
- Possible vendor lock-in if export is weak.
- Harder to audit than markdown unless transparent.
- More moving parts than a repo template should require.

Cloudflare's blog makes the key architectural point: the primary agent should not burn context deciding how storage works. A purpose-built memory API can be better than raw database/filesystem access for production workloads.

**Verdict for this framework:** design-compatible, not required. The framework should preserve a portable markdown schema so users can later migrate into an MCP/managed memory layer without losing meaning.

---

## Graduation ladder

The framework should recommend a ladder, not a binary choice.

| Stage | Use when | Backend | Search |
|-------|----------|---------|--------|
| **0 - No durable memory** | Disposable task | None beyond chat/context | None |
| **1 - Repo markdown** | Normal v1 project | `MEMORY.md`, `memory/*.md`, `STATUS.md`, `DECISIONS.md` | Index + filenames + `rg` |
| **2 - Local searchable memory** | Many sessions, repeated recall, local-first | SQLite / MCP local server | FTS5, optional local vectors |
| **3 - App-grade memory** | Building memory into a product or multi-user tool | Postgres + metadata + optional pgvector | SQL filters + FTS + vectors |
| **4 - Large semantic corpus** | Large docs/logs/research/support history | Dedicated vector DB or Vectorize/Qdrant/etc. | Vector + metadata + rerank |
| **5 - Relational/team memory** | Multi-agent/team, causal/temporal graph questions | Postgres + graph extension, Neo4j, Memgraph, Neptune, Kuzu | Hybrid + graph traversal |
| **6 - Managed memory service** | Team wants memory pipeline as infrastructure | Cloudflare/mem0/Letta/MCP service | Service-defined |

Proposed v1 default:

1. Start every project at Stage 1.
2. Add Stage 2 only if the user repeatedly asks "what did we decide last time?" and markdown lookup becomes annoying.
3. Use Stage 3+ only when the project itself is building agent memory or the memory store becomes product data.

---

## Graduation triggers

Thresholds should be rough, not magic numbers.

| Signal | Stay in markdown | Graduate |
|--------|------------------|----------|
| Number of durable memory entries | <50 comfortable; 50-200 with good index | >200 or index skimming becomes unreliable |
| Retrieval complaints | Agent finds the right file quickly | Agent often misses memories that exist |
| Write frequency | A few writes per session | Multiple agents/users writing concurrently |
| Scope | One project, one user | Cross-project, team, or app users |
| Query type | "Open the decision file" | "Find similar past incidents" / "What pattern keeps recurring?" |
| Privacy/security | Repo-appropriate memory | Personal/private/team data with access rules |
| Audit | Git history is enough | Need row-level audit, export, or compliance |

The important trigger is not store size alone. It is **retrieval failure plus maintenance burden**. A 300-entry markdown memory with excellent filenames may work. A 40-entry vector store full of duplicates and contradictions may fail.

---

## Recommended v1 file schema

Even if v1 uses markdown, it should store enough metadata to migrate later.

Proposed frontmatter:

```yaml
---
name: Human-readable title
description: One-line retrieval hook
type: semantic # semantic | episodic | procedural | reference
scope: project # project in v1; team reserved; personal deferred to future cross-project memory
kind: decision # decision | personalization | instruction | reference | research | log
tier: archival # core | recall | archival
source: session:2026-04-28 # or commit:<sha>, file:<path>, user-confirmed
created: 2026-04-28
updated: 2026-04-28
status: active # active | superseded | deprecated
---
```

Optional fields for later:

```yaml
supersedes:
confidence:
expires:
tags:
```

This is enough to migrate into Postgres, SQLite, or an MCP memory service without reclassifying every file from scratch.

---

## Token and context cost

Storage backend choice affects tokens indirectly through retrieval behavior.

| Backend | Steady context cost | Retrieval cost | Hidden cost |
|---------|---------------------|----------------|-------------|
| Markdown full-load | High if loaded wholesale | None | Lost-in-the-middle; steady token tax |
| Markdown JIT | Index only | Selected files | Index quality burden |
| SQLite/FTS | Summary/count only | Search results | Tool/server bridge |
| Postgres/pgvector | None unless queried | Query results + optional embedding | Query design, metadata discipline |
| Vector DB | None unless queried | Embedding + top-k chunks + rerank | Chunking/model/index ops |
| Graph | None unless queried | Nodes/edges plus explanation | Graph expansion; noisy relationships |
| Managed API | Tool listing only | Service response | Vendor/API latency and opacity |

The token mistake is assuming vector search automatically saves context. It only saves context if:

- the memory records are well-shaped,
- retrieval returns few high-signal results,
- the service does not dump noisy chunks,
- and maintenance prevents duplicates/stale memories.

For this framework, markdown JIT has the best cost/complexity ratio at launch. It keeps the core token cost tiny: index and current status only. The individual memories remain archival.

---

## Security and portability

Backend choice is also a trust boundary.

| Backend | Privacy posture | Portability |
|---------|-----------------|-------------|
| Repo markdown | High transparency; risky if personal/private data is committed | Excellent |
| User-space markdown | Personal and local; not shared by repo | Good but agent-specific unless standardized |
| SQLite local | Local-first; backup/export needed | Good if export exists |
| Postgres | Strong auth/RLS possible; operational burden | Good if schema documented |
| Vector DB cloud | Depends on provider; embeddings leave local boundary unless self-hosted | Variable |
| Graph DB | Same as DB; may expose sensitive relationships | Variable |
| Managed API | Depends on vendor/export guarantees | Risk if no export |

Framework rule that should survive every backend:

**Memory must be exportable to plain markdown/JSON.**

That preserves human control and avoids the trap where the most valuable artifact in the project becomes trapped inside one vendor or one agent harness.

---

## Patterns to borrow for our framework

1. **Default to repo markdown for project memory.** It is portable, inspectable, versionable, and enough for v1.

2. **Treat storage as a ladder.** Do not ask new users to choose files vs Postgres vs vector DB. Start simple, graduate on clear pain.

3. **Design the markdown schema for migration.** Add `type`, `scope`, `tier`, `source`, timestamps, and status now. These are cheap in files and valuable later.

4. **Separate memory records from search infrastructure.** The durable record is the source of truth. Vector/FTS/graph indexes are rebuildable derivatives.

5. **Prefer constrained memory tools over raw DB access in production.** Cloudflare's pattern is right: agent sees remember/recall/forget/list, not arbitrary database design.

6. **Postgres is the serious default once memory becomes app data.** Use it for auth, audit, filters, joins, and transactional updates; add pgvector only as one retrieval index.

7. **Vector DBs are for semantic scale, not every memory.** Small structured memories do not need embeddings.

8. **Graph memory is advanced.** Useful for team/multi-agent causality, but it needs pruning and relationship hygiene. Defer to v2 while keeping only the immediately useful `supersedes` hook.

9. **Local-first MCP memory is the likely bridge.** For cross-agent coding workflows, a local MCP server over SQLite/Postgres gives shared recall without forcing cloud storage.

10. **Export is non-negotiable.** Any backend we recommend must have a plain export path.

---

## Re-grill decisions applied

1. V1 project memory starts as repo markdown under the project-local framework area.
2. The markdown schema is strict enough for migration: `name`, `description`, `type`, `kind`, `scope`, `tier`, `source`, `created`, `updated`, and `status`.
3. Project-local personalization uses `scope: project` plus `kind: personalization`; do not use `scope: personal` in v1.
4. `scope: team` is reserved as a future value, but team/shared memory is unsupported in v1.
5. Graduation guidance should include rough thresholds, but retrieval failure and maintenance burden are the real triggers.
6. Local MCP memory servers are an optional advanced v1 graduation path, not an onboarding default.
7. When memory becomes product data, recommend Postgres first, with `pgvector` as an optional retrieval index.
8. Strongly warn against starting with vector databases unless there is large unstructured prose or proven semantic-search pain.
9. Add only `supersedes` as a v1 graph-style hook; defer broad `related` fields.
10. Every recommended backend must export to plain Markdown or JSON.
11. Strongly recommend git for memory auditability, but do not hard-block quick/local experiments.
12. For this project, keep current `memory/` authoritative during research and add only a bridge note that future Agent Loop memory is expected under `.agent-loop/memory/`.

---

## Sources

Direct reads:
- [Cloudflare - Agents that remember: introducing Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/) - managed memory API, constrained operations, SQLite-backed Durable Objects, Vectorize, supersession, RRF retrieval
- [Cloudflare Agents docs - Memory](https://developers.cloudflare.com/agents/concepts/memory/) - conversation history in SQLite, searchable context, FTS5 default, loadable context/skills
- [Databricks docs - Agent state and memory](https://docs.databricks.com/aws/en/oltp/projects/state-management) - managed Postgres/Lakebase backend for agent state and memory
- [LangChain/LangGraph docs - Long-term memory](https://docs.langchain.com/oss/python/langchain/long-term-memory) - JSON documents by namespace/key, InMemoryStore vs PostgresStore
- [Letta docs - Archival memory](https://docs.letta.com/guides/core-concepts/memory/archival-memory) - archival memory as query-on-demand vector DB, use/don't-use boundaries
- [mem0 docs - Vector databases overview](https://docs.mem0.ai/components/vectordbs/overview) - supported vector backends and config model
- [mem0 docs - Graph Memory](https://docs.mem0.ai/open-source/features/graph-memory) - vector + graph architecture, graph-store choices, pruning guidance
- [pgvector README](https://github.com/pgvector/pgvector) - vectors inside Postgres, exact/approximate search, ACID/PITR/joins
- [mcp-memory-service README](https://github.com/doobidoo/mcp-memory-service) - local/shared MCP memory, REST API, knowledge graph, local embeddings, autonomous consolidation

Search-surfaced / practitioner signals:
- [Reddit - How AI agent memory what are you using?](https://www.reddit.com/r/AI_Agents/comments/1qx495b/how_ai_agent_memory_what_are_you_using/) - graph expansion pain, vector latency/overkill concerns
- [Reddit - Agent memory degrades at 5k+ stored items](https://www.reddit.com/r/AI_Agents/comments/1slgft3/agent_memory_degrades_at_5k_stored_items_because/) - duplicate/contradiction/decay failure modes in append-only vector memory
- [Memorix DEV post](https://dev.to/_2340687267e5cacfe32da1/memorix-give-your-ai-coding-agents-shared-persistent-project-memory-1pk2) - cross-agent project memory via MCP and git-aware memory
- [Karpathy LLM wiki commentary](https://gamgee.ai/blogs/karpathy-llm-wiki-memory-pattern/) - file/wiki pattern as alternative to raw query-time RAG
