# Sub-Category 6.1 — Kinds of Memory

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 1 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

Before we can decide what to save, what to load, how to keep it healthy, or where to put it, we need a shared vocabulary for the **kinds** of things being stored. Every other sub-category in Category 6 inherits from this one. If we get the vocabulary wrong, the framework will paper over real distinctions.

The good news: across cognitive science, academic AI papers, and the working memory systems shipped by mem0, Letta, LangGraph, and Anthropic in 2026, the taxonomy has converged. There are **three useful axes**, not one.

---

## The three axes

Most writeups pick one axis and treat it as "the" taxonomy. They are talking past each other. The three axes are independent.

### Axis A — Type (what the memory holds)

This is the cognitive-science axis, formalized by Princeton's CoALA framework (2023) and adopted across the field.

| Type | What it is | Example | Source |
|------|------------|---------|--------|
| **Working / In-context** | The active context window. Everything the model processes in one inference: system prompt, retrieved chunks, tool outputs, reasoning. Finite. | Current chat plus injected file contents. | Baddeley & Hitch 1974 → CoALA 2023 |
| **Episodic** | Records of past events tied to time. Conversation logs, tool-call traces, prior queries and their results. | "Three months ago the user asked for Q2 revenue and we returned $X." | Tulving 1972 |
| **Semantic** | Facts and concepts, time-independent. Definitions, rules, business glossary. | "Revenue means net of returns, per Finance approval 2026-01-15." | Tulving 1972 |
| **Procedural** | Skills, behavioral rules, "how to act." System prompts, tool routing logic, playbooks. | "Pricing questions must use `certified_pricing_v3`." | Squire 1987 |

A possible fifth — **Organisational Context Memory** — was proposed by Atlan in 2026 to cover governance state (versioned definitions, certification flags, access policies). It's not a different storage type so much as semantic memory with a governance overlay. Worth flagging but not a separate primitive for our framework.

The mem0 taxonomy uses **factual / episodic / semantic / procedural** — "factual" is roughly user-specific semantic memory split out as its own bucket. We can collapse factual into semantic without losing anything.

### Axis B — Tier (how close to the active context)

This is the storage-tier axis, made explicit by MemGPT/Letta. Computer-architecture analogy.

| Tier | Analogy | Loaded when | Cost |
|------|---------|-------------|------|
| **Core** | RAM | Every turn — always in context | High (steady token tax) |
| **Recall** | Disk cache | On query — searchable conversation history | Medium (retrieval call + injected results) |
| **Archival** | Cold storage | On query — processed, indexed knowledge | Medium-low (only when needed) |

This axis is what the type axis lacks: it tells us **what we pay in tokens**. A piece of semantic memory in core tier costs us tokens every turn. The same semantic fact in archival costs us nothing until queried.

Anthropic's memory tool in 2026 sits at the **archival** end by default — files are only loaded via explicit `view` calls. Claude Code's auto-memory (which this project uses) is split: `MEMORY.md` is core (loaded automatically every turn), individual memory files are archival (loaded only when relevant).

### Axis C — Scope (who the memory belongs to)

The Databricks axis. Independent of type and tier.

| Scope | Belongs to | Examples |
|-------|------------|----------|
| **Personal** | One user | Individual preferences, private workflows, identity-tied facts |
| **Project** | One project / repo | Architecture rules, planning docs, decision history |
| **Team / Organisational** | A group | Shared naming conventions, business glossary, internal SOPs |

For our framework's audience (single developers running coding agents), the dominant split is **personal vs project**. Team scope matters once the framework is adopted by orgs.

### Why three axes matter

Any concrete memory item lives at one point on each axis. Examples:

- "User prefers terse code reviews" → **Type:** semantic. **Tier:** core (loaded every turn). **Scope:** personal.
- "We tried PostgreSQL row-level security in Sprint 12 and it leaked" → **Type:** episodic. **Tier:** archival. **Scope:** project.
- "Always run `make lint` before commit" → **Type:** procedural. **Tier:** core. **Scope:** project.
- "Customer X's account ID is 4471" → **Type:** semantic. **Tier:** archival. **Scope:** project.

Most existing taxonomies fail when they conflate axes. mem0 mostly talks about type. Letta mostly talks about tier. Databricks mostly talks about scope. The framework needs all three to give clean guidance.

---

## How real systems map onto the axes

| System | Type axis | Tier axis | Scope axis |
|--------|-----------|-----------|------------|
| **Anthropic memory tool** (raw) | Agnostic — files can hold anything | All archival; client controls storage backend | Agnostic — client controls |
| **Claude Code auto-memory** (this project) | 4 buckets: user / feedback / project / reference (purpose-based, maps loosely to type) | `MEMORY.md` is core; memory files are archival | Mixed — `user_profile` is personal, `project_*` is project |
| **Letta / MemGPT** | Type-agnostic | Explicit: core / recall / archival | Per-agent |
| **mem0** | factual / episodic / semantic / procedural | Vector store + optional graph (mostly archival) | User and agent scope |
| **LangGraph + LangMem** | Episodic / semantic / procedural | Short-term (in thread) vs long-term (cross-thread) | Custom namespaces |
| **Karpathy wiki pattern** | Sources / wiki / index / log / schema (file-role-based, not type-based) | `index.md` is core; wiki pages are archival | Per-wiki |

Two takeaways:

1. **Anthropic's memory tool is intentionally type-agnostic.** It ships file ops only; the type taxonomy is a convention you put on top. Claude Code's `user/feedback/project/reference` is one such convention — well-designed but specific to the harness, not the API.
2. **Karpathy's split is orthogonal to the cognitive-science split.** Sources/wiki/index/log/schema are *file roles*, not *content types*. A wiki page can hold semantic facts; a log entry holds episodic events; the index is procedural (it tells the agent how to navigate). The framework should adopt this — file role is a separate, useful axis.

---

## Cognitive science grounding (cross-discipline)

The agent memory taxonomy did not invent itself. It was lifted directly from psychology research that long predates LLMs. The translation is mostly clean, with two warnings.

| Researcher | Year | Contribution | AI translation | Translation quality |
|------------|------|--------------|----------------|---------------------|
| Atkinson & Shiffrin | 1968 | Sensory → short-term → long-term flow | Working memory → external store | Clean |
| Baddeley & Hitch | 1974 | Working memory model (phonological loop, visuospatial sketchpad, central executive) | "In-context memory" — but agents have no executive separation | Partial |
| Tulving | 1972 | Episodic vs semantic distinction | Adopted as-is | Clean |
| Squire | 1987 | Declarative vs procedural memory | Procedural memory = system prompts + skills | Clean |
| Ebbinghaus | 1885 | Forgetting curve (memory decays unless reinforced) | Stale-memory problem; expiration policies | Clean — and we should use it |

**Warning 1 — working memory is not just "context window."** Human working memory has structured sub-systems (phonological loop for verbal, visuospatial for spatial, central executive for control). LLM context is a flat token sequence. The translation flatters the LLM. In practice this shows up as the "lost in the middle" problem: tokens in the middle of a long prompt get ignored. Worth remembering when we recommend "keep it in core memory" — there is no executive prioritising what to attend to.

**Warning 2 — semantic vs procedural is fuzzy in AI.** "Always run `make lint` before commit" is presented as procedural in the field, but it's really a semantic fact ("the rule is X") that shapes behavior when loaded. Human procedural memory is implicit — you can't articulate how to ride a bike. AI procedural memory is fully articulated text. The distinction is useful but should not be overweighted.

**Cross-discipline borrow worth taking:** The forgetting curve. Memory that is never re-accessed should decay. Anthropic's memory tool docs explicitly recommend "clearing out memory files periodically that haven't been accessed in an extended time" — a direct application. Our framework should bake decay/expiration into Sub-category 4 (keeping memory healthy) rather than treating it as optional hygiene.

---

## Token cost

This section per the framework principle: every memory pattern has to declare its tax.

### Cost by tier (the dominant lever)

| Tier | Token cost | When it bites |
|------|------------|---------------|
| **Core** | Linear with size, every turn | A 5KB always-loaded file × 50 turns × $X/Mtoken adds up fast. "Lost in the middle" means more tokens ≠ more attention. |
| **Recall** | Pay only on query (search results injected) | Query overhead ~100-500 tokens; results 500-2000 tokens. Adds up on chatty tasks. |
| **Archival** | Near zero until used | Pay only the `view` call when a file is read. Index file is the gatekeeper. |

The Mem0 benchmark reports **~90% token savings vs naive context stuffing** by moving from core (everything always loaded) to archival (query-on-demand). The number depends heavily on workload, but the order of magnitude is consistent.

### Cost by type (less important, but real)

- **Semantic** facts compress well — "Revenue = net of returns" is short. Cheap.
- **Episodic** records are verbose — a tool-call trajectory can be hundreds of tokens. Expensive if kept raw; cheap if distilled.
- **Procedural** rules are short but multiply — 30 rules × 50 tokens = 1500 token tax in core every turn.
- **Working** memory is whatever the current task needs. Compute its size; budget for it.

### The "core memory" anti-pattern

The biggest token failure mode in file-based memory (this project's current setup) is **everything-in-core**: `MEMORY.md` plus every memory file all loaded on every turn. With ~10 memories at 2KB each, you've consumed ~20KB of context before the user types. Reported in practice as "memory files eating 15% of your window before you start."

Two mitigations:

1. **Index + on-demand load** (Karpathy, Anthropic): index file is core, content files are archival. Index entries are one-line hooks, agent reads only what it needs.
2. **Move out of files entirely** (Letta, mem0): vector or hybrid retrieval over a database. No file scan. Token cost is per-query, not per-turn.

This project's `MEMORY.md` already follows pattern 1. Whether to graduate to pattern 2 is a Sub-category 6 (storage backend) question.

---

## Patterns to borrow for our framework

1. **Adopt all three axes.** When the framework names a memory item, it should be classifiable on type, tier, scope. Re-grill should test this — it forces clarity.
2. **Add file role as a fourth axis** (Karpathy). Source / synthesized / index / log / schema are real distinctions, orthogonal to cognitive-science type.
3. **Default tier is archival.** Items go in core only when justified by per-turn relevance. Forces explicit cost decisions.
4. **Type-agnostic file ops, type-aware conventions.** Anthropic ships generic ops; Claude Code layers type conventions. Our framework should mirror this — base layer is mechanism, type taxonomy is documented convention.
5. **Forgetting is a feature.** Decay/expiration designed in from day one, not bolted on after memory bloats.
6. **One concrete memory item gets one row in `index.md`** — not in the file itself. Index entries describe what each memory is *for*, so the agent can decide whether to read it.

---

## Re-grill decisions applied

1. Use a hybrid vocabulary. User-facing docs use practical buckets; memory files still carry structured `type`, `scope`, and `tier` metadata.
2. File roles are explicit in implementer docs but described in plain purpose-based language for users.
3. Technical specs may say "working memory"; user-facing docs should say "current context."
4. `AGENTS.md` holds always-loaded mandatory procedural rules. Skills hold task-specific procedural playbooks.
5. V1 is project-local: `.agent-loop` is installed per project. Personalization memories use `scope: project` plus `kind: personalization`; automatic cross-project preference carryover is deferred.
6. `scope: team` is reserved as a future schema value, but team/shared memory is unsupported in v1.
7. Decay is handled through retrieval tie-breakers and human-reviewed health checks, not automatic expiration.

---

## Sources

Direct reads:
- [Karpathy, LLM-maintained wikis](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — file-role axis (sources/wiki/index/log/schema)
- [Databricks, Memory Scaling for AI Agents](https://www.databricks.com/blog/memory-scaling-ai-agents) — episodic/semantic + personal/organizational
- [Anthropic, Memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — 6 file ops, archival-by-default, multi-session pattern
- [Atlan, Types of AI Agent Memory](https://atlan.com/know/types-of-ai-agent-memory/) — CoALA framework, governance critique, cognitive-science origin table
- [mem0, How memory shapes us](https://mem0.ai/blog/how-memory-shapes-us-a-deep-dive-into-the-types-of-memory) — sensory → working → long-term hierarchy
- [Belitz, MD files vs Claude memory](https://blog.belitz.se/posts/my-md-files-vs-claudes-memory) — practitioner verdict on opacity vs discipline tradeoff

Search-surfaced:
- [Letta docs, Understanding memory management](https://docs.letta.com/advanced/memory-management/) — core/recall/archival tier model
- [LangGraph memory overview](https://docs.langchain.com/oss/python/langgraph/memory) — short-term/long-term + episodic/semantic/procedural
- [Anthropic engineering, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — referenced as the broader pattern
- Multiple commentaries on context rot and "lost in the middle" — token cost evidence

New sources discovered (added to research pool for later sub-categories):
- Vectorize — mem0 vs Letta comparison
- TokenMix — 2026 memory layer comparison
- MemMachine arXiv 2604.04853 — ground-truth-preserving memory
- DeepLearning.AI — Long-term agentic memory with LangGraph
- Anthropic — Effective harnesses for long-running agents (referenced from memory tool docs)
