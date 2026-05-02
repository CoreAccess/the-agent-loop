# Sub-Category 6.3 — What to Load and When

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 3 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

Sub-category 1 said memories should default to **archival** — not in context until needed. Sub-category 2 said the bias is toward saving less, not more. This sub-category answers: when an agent needs a memory, **how does it get there**, and what does that cost?

This is where the framework's stated principle (token & context efficiency first) lands hardest. Get retrieval wrong and either the agent loads everything (context bloat, "lost in the middle") or it loads nothing useful (the memory exists but the agent never finds it).

---

## The five retrieval strategies

The same five families show up across mem0, Letta, Anthropic's memory tool, Karpathy's wiki, and academic frameworks. They are not mutually exclusive — most production systems layer them.

### Strategy A — Full-load (no retrieval)

**How it works:** Every memory file is in core context every turn. No selection step.

**Used by:** Naive `MEMORY.md` setups, `CLAUDE.md`-style monolithic configs.

**Trade-off:** Zero retrieval cost, maximum token cost. Practitioners report "memory files eating 15% of your window before you've typed anything" with this pattern. Also exposes the **lost-in-the-middle** problem: long prompts have measurably worse attention to tokens in the middle, so loading more memory doesn't mean using more memory.

**When it's right:** Tiny memory stores (under ~5KB total). Prototype phase only.

### Strategy B — Index-driven (Karpathy pattern)

**How it works:** A small `index.md` file is in core context. Each entry is one line — title, hook, file pointer. The agent reads the index, picks the relevant memory file, loads only that file.

**Used by:** Karpathy's wiki pattern, this project's current `MEMORY.md` + memory files.

**Trade-off:** Low context cost (only the index is steady-loaded). Retrieval depends entirely on **the agent picking the right file from one-line hooks**. Misses if the hook is too vague or the agent's reasoning skips it.

**When it's right:** Moderate scale (under ~hundreds of memory entries) with disciplined index hygiene. Karpathy specifically calls out this works well "at moderate scale and avoids the need for embedding-based RAG infrastructure."

### Strategy C — Keyword / BM25 search

**How it works:** Memory is stored as discrete records. Agent queries with keywords; BM25 (or similar lexical scoring) ranks results.

**Used by:** Postgres full-text search, Elasticsearch-backed memory, many internal tool implementations.

**Trade-off:** Excellent for exact-term matches ("Error code TS-999"). Poor for semantic recall ("the bug we hit last sprint with the auth thing"). Works without LLM at retrieval time — fast and cheap.

**When it's right:** Memory dominated by named entities, codes, identifiers, exact strings.

### Strategy D — Vector / semantic search

**How it works:** Each memory has an embedding. Agent's query is embedded; nearest-neighbor search returns top-k similar memories.

**Used by:** mem0, Letta archival, LangGraph long-term memory, every RAG-backed system.

**Trade-off:** Catches paraphrases and conceptual similarity. Misses exact-string recall (BM25 wins there). Embeddings have to be generated at write time and search time. Quality depends heavily on chunk boundaries and embedding model.

**When it's right:** Memory dominated by free-form prose where the user won't query with the exact phrasing they originally said.

### Strategy E — Hybrid (BM25 + vector + reranker, often + recency)

**How it works:** Run B/C/D in parallel, combine scores. Often add a recency decay weight — recent memories scored higher than old ones with the same similarity.

**Used by:** Anthropic Contextual Retrieval, mem0g (graph variant), production pgvector setups, Weaviate.

**Trade-off:** Best accuracy. Highest implementation complexity. More moving parts.

**Anthropic's Contextual Retrieval results:**
- Contextual Embeddings alone → 35% reduction in retrieval failures
- + Contextual BM25 → 49% reduction
- + reranking → 67% reduction

**When it's right:** Memory store >200k tokens or chunks lack standalone context. Anthropic explicitly says: if your knowledge base fits the context window, **don't bother with retrieval** — use prompt caching instead.

### Comparing the five

| Strategy | Steady token cost | Per-query cost | Recall quality | Complexity |
|----------|-------------------|----------------|----------------|------------|
| Full-load | Very high (linear with store) | None | High but plagued by lost-in-the-middle | Trivial |
| Index-driven | Low (index only) | One file read | Moderate — depends on hook quality | Low |
| Keyword/BM25 | None | Fast lookup | Strong on exact terms, weak on paraphrase | Low |
| Vector | None | Embedding + ANN | Strong on paraphrase, weak on exact terms | Medium |
| Hybrid | None | Multiple lookups + reranker | Highest | High |

---

## Just-in-time retrieval (the meta-principle)

A pattern named explicitly in the 2026 research literature: **JIT context retrieval**. Borrowed from compiler terminology — instead of pre-loading everything, store cues + raw archive, "compile" tailored context on the fly when a request arrives.

This is the pattern Anthropic's memory tool docs explicitly endorse: "rather than loading all relevant information upfront, agents store what they learn in memory and pull it back on demand. This keeps the active context focused on what's currently relevant."

JIT is not a single retrieval strategy — it's a **commitment** to one. The framework's commitment should be JIT by default. Full-load is allowed only for the index/scaffolding tier.

---

## The lost-in-the-middle problem

Confirmed across multiple sources. Tokens at the very start and very end of a long prompt get high attention. Tokens in the middle get measurably less. This means:

- Loading 50KB of memory doesn't equal "the agent has 50KB of memory available." It equals "the agent has roughly the start and end available, with diminishing attention through the middle."
- Counter-intuitively, **less can be more**. Loading 5KB of well-targeted memory often beats 50KB of dump.
- Anthropic's "Contextual Retrieval" recommends retrieving 20 chunks rather than 5 or 10 — but only because they pair it with reranking that pushes the most relevant to the start/end positions.

For the framework: **steady core context is precious real estate**. Anything in `MEMORY.md` or `AGENTS.md` is loaded every turn and competes for attention. Discipline about what goes there is more important than discipline about what goes in archival.

---

## When retrieval is overkill

A specific finding from Anthropic Contextual Retrieval that landed cleanly: **if your knowledge base fits the context window, don't retrieve. Use prompt caching instead.**

For the framework's audience (solo devs working on one project at a time), the *project-scope* memory store likely fits in context for many projects. The bias should be:

1. Tiny store → full-load with index (current `MEMORY.md` pattern). Cache the whole thing.
2. Moderate store → index-driven JIT load (graduated current pattern). Index in cache; files loaded as needed.
3. Large store → hybrid retrieval (Postgres + pgvector + recency, or dedicated vector DB).

Most users never reach (3). Designing the framework as if everyone needs vector search is YAGNI.

---

## Token cost

| Strategy | Tokens loaded per turn | LLM calls per query | Hidden costs |
|----------|------------------------|---------------------|--------------|
| Full-load | Entire store | 0 | Lost-in-the-middle attention loss |
| Index-driven | Index size + selected file | 0 (agent picks via reasoning) | Index hygiene burden |
| BM25 | Query results only | 0 | Index maintenance |
| Vector | Query results only | 1 (embedding) | Embedding pipeline |
| Hybrid | Query results only | 1-2 (embedding + rerank) | Multiple systems |

The Anthropic memory tool's design implicitly endorses index-driven JIT. The agent's first move is `view /memories` (sees the directory listing, like an index). It reads only the file it picks. No vector search. No embedding pipeline. Works because:

- The directory listing is ~1 line per file (cheap)
- Filenames are descriptive (work as hooks)
- Agent picks via reasoning, not nearest-neighbor

For a single-project memory of <100 entries with descriptive filenames, this is enough. We don't need to build retrieval infrastructure.

---

## Patterns to borrow for our framework

1. **JIT by default. Full-load only for the scaffolding tier.** `AGENTS.md`, `STATUS.md`, and the memory index are full-load (always in context). Everything else is loaded on demand. This is the existing pattern; codify it.

2. **Index hygiene is load-bearing.** If the framework's primary retrieval mechanism is "agent reads index, picks file," index entries must be informative one-liners. Vague hooks ("Notes on memory") fail; specific hooks ("AI Framework Project — Core Decisions") work. Plain language principle reinforces this.

3. **Filename as second-order index.** Anthropic's memory tool relies on `view` returning filenames. Filenames should be descriptive, kebab-case, and topical. Not `notes_2026_04_27.md`; yes `framework_research_decisions.md`.

4. **Defer vector search.** Most users never need it. The framework should ship a file-based retrieval pattern that scales to ~hundreds of entries. Sub-category 6 (storage) covers when/how to graduate.

5. **Reranking by recency is a cheap win.** Even without vector search, when multiple memory files match a hook, prefer recent. Sub-category 4 (health) covers timestamping.

6. **Document the lost-in-the-middle constraint explicitly.** Framework docs should state: "Adding to AGENTS.md or MEMORY.md is not free — it costs steady tokens AND attention. Push memories to archival files unless they need to be in core every turn."

7. **Borrow Anthropic's "if it fits in context, cache it" rule.** For small projects, the framework should not encourage building retrieval pipelines. Cache the whole thing.

---

## Re-grill decisions applied

1. V1 uses index-driven just-in-time retrieval, supported by keyword search for exact terms.
2. Memory index entries stay minimal: title, link, and a high-quality one-line retrieval hook. Full metadata stays in file frontmatter.
3. Memory filenames should be stable, descriptive, human-readable, and lowercase kebab-case or snake_case. Do not require type/scope prefixes.
4. Always-loaded files use soft size budgets with warnings, not hard caps.
5. Retrieval graduation uses rough numeric thresholds for orientation, but retrieval failure and maintenance burden are the real triggers.
6. Recency is a tie-breaker after status/authority, relevance, and source quality.
7. Anthropic Contextual Retrieval is an advanced Anthropic-specific option, not The Agent Loop's portable v1 default.
8. Root agent instructions should explicitly say to start from index/status, load only task-relevant memory, and broaden only when retrieval fails or the task needs more context.

---

## Sources

Direct reads:
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — 35/49/67% retrieval failure reduction; "if it fits in context, don't retrieve"
- [Anthropic memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — JIT principle; `view` directory pattern

Search-surfaced:
- [Karpathy gist (re-read for retrieval)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — index-driven retrieval at moderate scale
- [The New Stack — Memory for AI Agents: A New Paradigm of Context Engineering](https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/) — JIT pattern named
- [Cloudflare — Introducing Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/) — managed-service JIT
- [VentureBeat — GAM dual-agent memory architecture](https://venturebeat.com/ai/gam-takes-aim-at-context-rot-a-dual-agent-memory-architecture-that) — context rot mitigation
- Multiple commentaries on lost-in-the-middle and steady context bloat

New sources discovered:
- [GAM hierarchical graph-based agentic memory (arXiv 2604.12285)](https://arxiv.org/html/2604.12285)
- [MachineLearningMastery — 6 Best AI Agent Memory Frameworks 2026](https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/)
