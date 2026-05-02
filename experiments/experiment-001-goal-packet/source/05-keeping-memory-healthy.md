# Sub-Category 6.4 — Keeping Memory Healthy

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 4 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

Memory without maintenance rots. Practitioners report this consistently:

- After a few hundred conversations, vector stores become bloated, retrieval quality degrades, and costs scale linearly.
- "A highly-retrieved memory about a user's employer is highly relevant — until it isn't, at which point it becomes confidently wrong rather than just outdated."
- Karpathy: "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."

The framework needs explicit maintenance machinery, not "we'll clean it up later." This sub-category covers what the machinery looks like.

Four failure modes to design against (introduced in sub-category 2, expanded here):
- **Bloat** — store grows without curation
- **Contradiction** — old fact says X, new fact says NOT-X, both saved
- **Staleness** — fact was true, no longer is, no decay applied
- **Drift** — semantic meaning of a memory shifts under it (the codebase changed; the memory references files that no longer exist)

---

## Four maintenance operations

The field has converged on four operations. Anthropic's memory tool ships them as primitives; mem0 implements them as an LLM-driven pipeline; Karpathy describes them prose-style. They are the same four operations.

### Operation 1 — Distillation (episodic → semantic)

**What:** Take raw episodic records (conversation logs, tool-call traces, session histories) and extract the durable lesson. Store the lesson in semantic memory. Optionally drop the raw record.

**Real implementations:**
- **mem0 extraction phase** runs an LLM pass that pulls discrete facts out of conversation turns.
- **LightMem** does offline consolidation, "distilling high-value episodic evidence into de-identified, long-term semantic knowledge."
- **MemAlign** uses an LLM to "distill episodic memories into generalized rules and patterns."
- **HeLa-Mem** uses Hebbian distillation — episodic items co-activated together get strengthened semantic links.

**Cost:** One LLM call per distillation pass. Run as a background job (overnight, end-of-week, or end-of-session).

**Trigger options:** Time-based (daily/weekly), volume-based (every N episodic entries), event-based (session end), or agent-decided (during reasoning).

**Verdict:** Distillation is the **least-served** operation in current frameworks per the 2026 academic survey. Most systems either skip it or collapse it into the save step. For our framework: this is the Reflect-phase work.

### Operation 2 — Consolidation (deduplicate, merge, resolve contradictions)

**What:** When a new memory is similar to an existing one, decide: add new, update existing, delete old, or do nothing.

**Real implementation — mem0's four-op classifier:**
- `ADD` — no semantically equivalent memory exists → create new
- `UPDATE` — existing memory needs augmentation with complementary info
- `DELETE` — existing memory is contradicted by new info → remove
- `NOOP` — fact already exists or is irrelevant → ignore

The classifier is an LLM call gated by vector similarity — only candidates above a similarity threshold get classified. Below threshold, default is `ADD`.

**Mem0g (graph variant):** Conflict detection marks contradicting relationships as invalid rather than deleting them, supporting temporal reasoning. "We agreed in March 2026 to use Postgres; in May 2026 we switched to SQLite" — both kept, with the older marked superseded.

**Cost:** One classifier call per save (or per save batch). Can be amortized.

**Why it matters:** Without consolidation, the same fact gets saved 10 different ways. Retrieval becomes ambiguous; the agent picks whichever variant came up first.

### Operation 3 — Decay / forgetting

**What:** Memories that aren't accessed lose salience over time. Eventually they expire or get archived to cold storage.

**Six policies in the literature:**
- **FIFO** — oldest first. Simple but blind to importance.
- **LRU** (least recently used) — optimal when usefulness decays exponentially with time.
- **Priority decay** — weight memories by importance score, decay the score over time. Best for heterogeneous memory types.
- **Reflection-summary** — when about to evict, summarize multiple memories into one before deletion.
- **Random drop** — surprisingly effective baseline; prevents over-fitting to recency.
- **Hybrid** — combination of above.

**Practical implementation patterns:**
- Multiply semantic similarity by an exponential decay factor based on time since last access during retrieval scoring. Memories not recalled recently lose salience gradually — Ebbinghaus curve applied directly.
- Native TTL (time-to-live) at the storage layer auto-expires entries.
- Versioned entity records — updates overwrite prior values with timestamps; old values still queryable for audit.

**Anthropic memory tool guidance** (from docs): "Consider clearing out memory files periodically that haven't been accessed in an extended time."

**Cost:** Decay is cheap if implemented at retrieval time (multiply scores). Eviction is also cheap (one delete). Reflection-summary before eviction is more expensive but preserves information.

**The staleness problem (open):** Detecting when a high-relevance memory has become wrong is unsolved. Decay handles low-relevance staleness. High-relevance staleness ("the user's job changed") needs explicit invalidation, often human-driven.

### Operation 4 — Lint / health check (Karpathy)

**What:** Periodic pass that finds problems: contradictions across memories, orphan entries (memories with no incoming references), broken links (memory references a file that no longer exists), stale entries past their TTL, and entries that violate format conventions.

**Karpathy's framing:** Lint is the third primitive operation alongside ingest and query. It's how memory stays self-consistent.

**Real implementations:** Most production systems don't have a named lint operation, but functionally equivalent processes exist:
- **mem0g** invalidation-marking is a form of lint.
- Many production agents run weekly cleanup jobs that scan for stale or duplicate entries.

**Cost:** One pass over the entire store. Expensive at scale; cheap for small stores. Can be batched and run off-peak.

**Verdict:** Lint is more important for our framework than for chatbot-style agents because our memory stays small and human-readable — the lint output can surface problems to the user during Reflect, not auto-fix them.

---

## Background vs. foreground maintenance

Two operating modes show up across the field:

### Foreground — at write time

Consolidation runs synchronously when a save is attempted. The classifier blocks the save until it decides ADD/UPDATE/DELETE/NOOP.

- **Pro:** Memory store is always consistent.
- **Con:** Adds latency to every save. Classifier failures break saves.

Used by: mem0.

### Background — periodic batch

Distillation, decay, and lint run as scheduled batch jobs. Saves are append-only and fast; the cleanup happens later.

- **Pro:** Saves are cheap. Failures are isolated.
- **Con:** Memory store can be temporarily inconsistent (recently-saved duplicates, contradictions, staleness).

Used by: LightMem (offline consolidation), most production systems for distillation and decay.

**Hybrid (recommended for our framework):**
- Foreground: nothing — keep saves cheap.
- End-of-session: agent flags possible duplicates / contradictions during Reflect (consolidation) and proposes candidate distillations.
- Periodic (weekly?): lint pass surfacing health issues to user.
- Always-on: decay applied at retrieval time (scoring), not as a separate process.

This matches the existing decision (Reflect = human-approved memory distillation) and extends it.

---

## Versioning and audit trails

Several systems maintain history rather than overwriting:

- **mem0g** marks contradicting relationships as invalid rather than deleting.
- **Versioned entity records** maintain a separate version history per entity; updates create new versions tagged with timestamps.
- **Karpathy's `log.md`** is append-only by design — every operation is recorded chronologically.

For a coding-agent framework, **git history is the cheapest audit trail**. If memory files live in the project repo (which they do for `MEMORY.md` patterns), every edit is already logged with timestamps and diffs. The framework should lean on this — don't reinvent versioning that git already does.

For databases (sub-category 6 question), versioning needs explicit columns: `created_at`, `updated_at`, `superseded_by`, `valid_from`, `valid_to`. Standard event-sourcing patterns.

---

## Token cost

Maintenance is cheap *per-operation* but adds up.

| Operation | Cost per run | Frequency | Aggregate cost |
|-----------|--------------|-----------|----------------|
| Distillation | 1-3 LLM calls (small context) | End of session or weekly | Low if batched |
| Consolidation | 1 LLM classifier call per save | Every save | Medium — proportional to save volume |
| Decay scoring | Negligible (math) | Every retrieval | Negligible |
| Decay eviction | 1 delete per evicted entry | Periodic | Negligible |
| Lint pass | One scan + LLM judgment per issue | Weekly | Medium — proportional to store size |

The dominant maintenance cost in production is **consolidation at save time**. Mem0's design eats this cost; the alternative (append-only saves, deduplicate later) trades latency for batch cost.

For a small file-based store (<100 entries), the framework can skip consolidation entirely and lean on lint. For larger stores, consolidation becomes worth the cost.

---

## Patterns to borrow for our framework

1. **Reflect is the primary distillation moment.** Already decided. Codify the role: at end of session, agent reviews episodic content (the conversation, decisions made, code changed), proposes distilled memories, human approves.

2. **Adopt mem0's ADD/UPDATE/DELETE/NOOP vocabulary.** When the agent proposes a memory during Reflect, classify it as one of the four. Forces explicit thinking about contradictions and duplicates.

3. **Lean on git history for audit.** Memory files live in the project. Edit history is already preserved. No separate versioning machinery for v1.

4. **Decay at retrieval time, not as a sweep.** When the agent scans the index and multiple files match, prefer recent. No background eviction process needed for moderate stores.

5. **Lint as a Reflect-phase agent task.** During Reflect, the agent actively scans for: contradictions across memory files, orphan entries (memories with no current relevance), broken links to files that no longer exist, format violations. Surfaces a punch list to the user. User decides what to act on.

6. **Append-only `log.md` as recall layer.** Karpathy's pattern. Every session's notable events get appended chronologically. Cheap to write, never edited, retrievable for audit. Distinct from `MEMORY.md` (durable distilled facts) and `STATUS.md` (current state).

7. **Stale-relevance is a known unsolved problem; surface it.** The framework should not pretend to solve high-relevance staleness automatically. Reflect prompts should include a question like "Has anything we believed before changed?" — keeps the user in the loop on invalidation.

8. **Distillation is high-value and currently underserved.** The 2026 survey says distillation is the least-implemented operation. Our framework treating Reflect as a first-class distillation phase is genuinely differentiated, not just convention-following.

---

## Re-grill decisions applied

1. Use layered lint: a light memory health check during Reflect every session, with deeper lint periodically or when memory problems appear.
2. Reflect asks stale-memory questions only when the session changed direction, reversed a decision, altered architecture, corrected an assumption, or made earlier memory suspect.
3. Recency is a tie-breaker, not the main retrieval rule.
4. V1 creates a lightweight append-only log for notable events, not full transcripts.
5. Git is strongly recommended for repo-scoped memory auditability, but it should not hard-block quick/local experiments.
6. Consolidation timing is stage-based: markdown v1 consolidates during Reflect/batch lint; product-grade DB or managed memory may use foreground checks for high-impact writes.
7. Orphan/stale cleanup uses health-check signals plus optional review windows as weak prompts. Never delete or expire memory automatically.
8. Supersede decisions and rationale; allow approved deletion for low-value mistakes, duplicates, bad inferred preferences, broken references, and stale operational facts.

---

## Sources

Direct reads:
- [Anthropic memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — file size limits, expiration recommendation
- [mem0 Update Memory docs](https://docs.mem0.ai/core-concepts/memory-operations/update) — ADD/UPDATE/DELETE/NOOP four-op classifier
- [mem0 paper (arXiv 2504.19413)](https://arxiv.org/html/2504.19413v1) — production-ready memory architecture, conflict resolution

Search-surfaced:
- [Fazm — Memory Triage for AI Agents](https://fazm.ai/blog/ai-agent-memory-triage-retention-decay) — six forgetting policies, staleness problem
- [Towards Data Science — Practical Guide to Memory for Autonomous LLM Agents](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/) — failure modes, decay implementations
- [ICLR 2026 MemAgents workshop proposal](https://openreview.net/pdf?id=U51WxL382H) — distillation underserved
- [LightMem (referenced in search)](https://arxiv.org/) — offline consolidation pattern
- [HeLa-Mem (arXiv 2604.16839)](https://arxiv.org/html/2604.16839) — Hebbian distillation
- [MemAlign (referenced in search)](https://arxiv.org/) — episodic-to-semantic distillation via LLM
- [YourMemory GitHub — Ebbinghaus forgetting curve decay](https://github.com/sachitrafa/YourMemory) — concrete implementation, +16pp recall vs mem0
- [Karpathy gist — lint operation](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — third primitive alongside ingest/query

New sources discovered:
- [Memory Survey paper (arXiv 2603.07670)](https://arxiv.org/html/2603.07670v1) — comprehensive 2026 mechanism survey
- [Agent-Memory-Paper-List (Shichun-Liu)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) — curated 2026 reading list
