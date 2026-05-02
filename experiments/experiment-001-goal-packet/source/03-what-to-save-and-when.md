# Sub-Category 6.2 — What to Save and When

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 2 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

The save decision is the front door of every memory system. Get it wrong on the side of "save too much" and the store fills with noise — practitioners report **60-70% of conversation tokens are small talk, repetition, or transient reasoning**. Get it wrong on the side of "save too little" and the agent forgets things the user told it minutes ago.

Two questions to answer:

1. **When** does a moment cross the threshold from "in-flight conversation" to "worth persisting"?
2. **What shape** does the saved item take — verbatim, summary, distilled fact, structured record?

Every concrete agent memory system in 2026 makes a different bet on these two. The framework needs an opinion.

---

## The trigger problem — five patterns in the field

Every shipped system uses one of five trigger patterns. They have different cost, accuracy, and trust profiles.

### Pattern 1 — Continuous LLM extraction (mem0)

**How it works:** After each conversation turn (or batch of turns), an LLM pass reads the new content, the rolling summary, and recent messages. It extracts discrete facts. Each fact becomes a memory entry.

**Heuristic mem0 actually uses:** Definitional content like "What is machine learning?" generates no memory. Personal or temporal content like "Yesterday I learned about ML in class" does — because it has personal experience and temporal context.

**Cost:** One extra LLM call per save trigger. Mem0 reports the cost is offset by ~90% downstream context-stuffing savings.

**Trust:** Auto-approved — no human review. Errors compound silently.

**When it works:** High-volume conversational agents (chatbots, customer support) where reviewing every save is impossible.

**When it breaks:** Long sessions accumulate hallucinated saves. After a few hundred conversations, vector stores bloat, retrieval quality degrades, and the agent starts citing things the user never said.

### Pattern 2 — Agent-decides via tool call (Letta/MemGPT)

**How it works:** The agent itself decides during its reasoning loop. When something seems important, it calls `core_memory_replace`, `memory_insert`, or `archival_memory_insert`. No separate extraction pass — the model is the trigger.

**Heuristic:** Implicit. Whatever the model thinks is important. Usually surfaces in fine-tuning + system-prompt instructions.

**Cost:** Embedded in the regular reasoning loop — no extra call. But every memory write is a function-call tax.

**Trust:** Auto-approved. Higher variance than mem0 because the model is doing two jobs (reasoning + curation).

**When it works:** Long-horizon agents that need to manage their own state — coding agents, research agents, anything multi-session where context bursts.

**When it breaks:** The model gets distracted into bookkeeping and forgets the actual task. Or saves trivial things because the system prompt over-promotes "remember this." Documented pain on Reddit.

### Pattern 3 — End-of-session digest (Anthropic memory tool docs, "multi-session software development pattern")

**How it works:** Before the session ends, the agent updates a progress log with what was completed, what remains, and any open decisions. Driven by an explicit instruction in the system prompt: "ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded."

**Cost:** One save pass per session. Cheap.

**Trust:** Auto, but bounded — only one write moment per session, easier to audit.

**When it works:** Long-running coding tasks where the unit of work is a session. This project's `STATUS.md` handoff pattern is exactly this.

**When it breaks:** If the agent crashes or the user closes the session abruptly, no save happens. The whole pattern depends on a graceful shutdown.

### Pattern 4 — Event-triggered (mostly described in practitioner blogs)

**How it works:** Specific events fire a save. Common triggers:
- User correction ("no, actually X")
- Preference statement ("I prefer terse responses")
- Task completion (final output reached)
- Explicit user signal ("remember that")

**Cost:** Cheap and predictable — only fires on signal.

**Trust:** Higher than continuous because triggers are observable. But misses anything the heuristic doesn't catch.

**When it works:** Conversational assistants where corrections and preferences are the high-value memories.

**When it breaks:** The agent stops learning anything that doesn't fit the trigger list. Implicit knowledge (the user always wants Python, not JS — never stated explicitly, just observed across sessions) is invisible.

### Pattern 5 — Agent drafts, human approves (this project's current pattern)

**How it works:** The agent identifies a candidate memory, drafts the entry, presents it to the user. Nothing is written until the user approves or edits.

**Cost:** Minimal LLM cost. Maximum human cost — every save needs review.

**Trust:** Highest. Bad memories never enter the store.

**When it works:** Solo-dev workflows on long-lived projects where every memory matters and review fatigue is low. This project's `Reflect memory distillation` decision (2026-04-27 DECISIONS log) chose this explicitly.

**When it breaks:** Volume. Anything past ~5 candidate memories per session and the user starts rubber-stamping.

### Comparing the five

| Pattern | Cost | Accuracy ceiling | Trust | Best for |
|---------|------|------------------|-------|----------|
| Continuous LLM extraction | Medium (per-save LLM call) | Medium (silently drifts) | Low | High-volume conversational |
| Agent-decides tool call | Low (no extra call) | Medium-low (model does two jobs) | Low | Long-horizon stateful agents |
| End-of-session digest | Very low | High (one focused write) | Medium | Multi-session work like coding |
| Event-triggered | Very low | Medium (misses implicit) | Medium-high | Preference + correction capture |
| Agent drafts, human approves | High (human time) | Highest | Highest | Solo dev, framework projects |

**For our framework (target: experienced AI-assisted devs):** the right answer is hybrid, not single-pattern.

---

## What shape does the saved item take?

The shape question is independent of the trigger. Across systems, three shapes show up.

### Shape A — Verbatim record

What was actually said or done. Conversation logs, tool-call traces.

- **Used by:** Letta recall memory (raw chat history), Karpathy `log.md`
- **Pro:** Lossless. Can be re-summarized later when better tooling exists.
- **Con:** Massive. Token cost on retrieval. Most of it is noise.

### Shape B — Summary

Compressed prose version of a session, segment, or event.

- **Used by:** mem0 rolling summary, Anthropic compaction
- **Pro:** Cheaper than verbatim. Preserves narrative flow.
- **Con:** Compression is lossy. Specific facts get smudged. Retrieving "what did the user say about Postgres?" from a paragraph summary is harder than from a discrete fact.

### Shape C — Discrete fact / atomic record

One memorable thing per entry. Structured: subject, predicate, object, source, timestamp.

- **Used by:** mem0 memory entries, this project's individual `.md` memory files (loosely)
- **Pro:** Searchable. Updateable atomically. Compresses well. Each fact has its own metadata (when learned, source, confidence).
- **Con:** Loses context. A fact in isolation can be misleading (the user said "I love Tailwind" — but only after I clarified that we were using it everywhere already).

### Mem0's atomic-fact format (concrete schema)

mem0 saves memories as discrete facts with:
- A short text statement ("user prefers Python")
- An LLM-extracted classification
- Vector embedding
- Optional graph relationships (Mem0g variant)
- Timestamps for creation and update

This is the most replicable schema in the field. Worth borrowing.

### When each shape fits

| Shape | Best for | Tier (from sub-cat 1) |
|-------|----------|------------------------|
| Verbatim | Audit trail, "what really happened" | Recall |
| Summary | Session handoffs, narrative reconstruction | Recall or Archival |
| Discrete fact | Anything that should be queryable | Archival |

In practice, well-designed systems use all three layered: log.md is verbatim (recall), session summaries are prose (recall), memory facts are discrete (archival). Karpathy's wiki pattern explicitly does this.

---

## Failure modes (worth designing against)

These are cited consistently across practitioner sources.

### F1 — Memory bloat (60-70% noise rule)

Most conversation tokens are not memorable. Save indiscriminately and after a few hundred sessions the store is mostly small talk, repetition, and transient reasoning. Retrieval precision falls because the haystack grew faster than the needles.

**Mitigation:** A trigger heuristic that *rejects* by default. Memory is precious; the bias should be toward not-saving unless the entry passes a test.

### F2 — Hallucinated saves

The agent invents a memory ("the user told me they prefer X") that the user never said. Once written, it becomes ground truth for future sessions.

**Mitigation:** Anchor every save to a source — the conversation turn that triggered it. Make it auditable. Human-approved patterns prevent this entirely; auto patterns need source-stamping.

### F3 — Stale memory contradicting current truth

User said X six months ago. Said NOT-X yesterday. Both saved. Agent now has contradictory memories and either picks the wrong one or hedges.

**Mitigation:** Update-in-place over append-only. mem0 supports this. Sub-category 4 (keeping memory healthy) covers consolidation.

### F4 — Implicit knowledge never captured

The user always uses Python, never Java. They never said "I prefer Python." The agent has the data (every code sample they shared was Python) but no trigger fires. Implicit preferences stay implicit.

**Mitigation:** Observation-based triggers — periodic "what patterns do I see?" passes. Anthropic Code's auto-memory does this for some categories. Easy to over-use.

### F5 — Save fatigue (review pattern only)

Human-approved saves work until the user is reviewing 10 candidate memories per session. Then approval becomes rubber-stamping and the trust advantage evaporates.

**Mitigation:** Quality gate on what becomes a candidate at all. Better to surface 1 high-confidence candidate than 10 maybes.

---

## Token cost

Save-time cost is a different beast from load-time cost. Worth treating separately.

### Save-time cost

| Pattern | LLM calls per save | Tokens per save (typical) |
|---------|--------------------|----------------------------|
| Continuous LLM extraction | 1 (extraction) | 1k-3k (recent context + extraction prompt) |
| Agent-decides tool call | 0 extra (in-loop) | 100-500 (tool args) |
| End-of-session digest | 1 (digest pass) | 2k-5k (session summary) |
| Event-triggered | 0-1 depending on shape | 100-1000 |
| Human-approved | 1 (draft) + N (revisions) | 500-2000 |

Save-time cost is amortized — it happens once per save. Load-time cost (sub-category 3) repeats every retrieval. So save-time should optimize for **accuracy** over **cost** in most cases.

### What the saved item costs at storage and retrieval time

A discrete fact (~100 tokens) vs a verbatim turn (~500 tokens) vs a session summary (~2k tokens). When the index lists 50 memories and the agent has to pick which to load, the discrete-fact format is dramatically cheaper to scan. This loops back to the shape choice — atomic facts win on retrieval token cost even if they cost more LLM calls to create.

### Cost cliff: hybrid means double-paying

The temptation is "save in all three shapes — verbatim for audit, summary for narrative, facts for query." This compounds save cost. The well-designed systems pick: Karpathy uses log + wiki (skips standalone summary). mem0 skips verbatim. Letta uses verbatim recall + structured core (skips summary). The framework should pick a default combination, not all three.

---

## Patterns to borrow for our framework

1. **Bias toward not-saving.** The default should be "this conversation produced no memories" unless an entry passes the test. Push back on the temptation to record everything.

2. **Multiple triggers, not one.** Anthropic-style end-of-session digest + event-triggered saves on user signal + human-approved Reflect candidates. Each captures different memory types. Continuous LLM extraction is overkill for our audience.

3. **Source-stamp every memory.** Every saved item carries the conversation turn or commit hash that produced it. Prevents F2 (hallucinated saves) and supports F3 (consolidation).

4. **Atomic facts as the dominant shape.** One memory file = one durable fact, with a one-line index entry. Verbatim records belong in `log.md`-style recall storage, not the memory files themselves.

5. **Adopt mem0's classification heuristic.** Rough rule: if the content is general/definitional, do not save. If it is personal, temporal, or preference-bearing, save it. Plain-language version for our docs: "save things that are about *this* user, *this* project, or *this* moment."

6. **Reflect phase is the human-approved gate.** Already decided in 2026-04-27 DECISIONS log. Confirm and codify: the framework's primary save pattern is human-approved at Reflect. End-of-session digest and event-triggered saves can be autonomous because they are bounded and predictable.

7. **Reject verbatim from the memory files.** Conversation logs (verbatim) belong in a separate recall layer (or git history, for code projects). The memory files are for distilled, queryable knowledge only.

---

## Re-grill decisions applied

1. Use a hybrid save model: automatic bounded handoff/log updates, explicit event-triggered candidates, and Reflect-phase human-approved durable memories.
2. Automatic writes are limited to `STATUS.md` and append-only logs. Durable memory files and memory index changes require explicit human approval.
3. Memory frontmatter requires a source stamp. Source values may use typed references such as `session:`, `commit:`, `file:`, `issue:`, `url:`, or `user-confirmed:`.
4. Reflect may propose implicit-pattern memories in v1, but they must be labeled as inferences, cite observations, and require confirmation.
5. Reflect should usually surface 1-3 high-confidence memory candidates.
6. Durable memory should reject secrets, credentials, PII, transient reasoning, small talk, general definitions, facts derivable from repo/code, unsourced claims, duplicates, and quickly expiring facts.
7. Do not create default separate conversation summaries. Use `STATUS.md`, append-only logs, and durable memory files instead.

---

## Sources

Direct reads:
- [mem0 — Memory types docs](https://docs.mem0.ai/core-concepts/memory-types) — layered architecture, security guidance
- [Anthropic memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — multi-session pattern, "ASSUME INTERRUPTION" instruction, end-of-session digest model

Search-surfaced:
- [mem0 — Long-Term Memory for AI Agents](https://mem0.ai/blog/long-term-memory-ai-agents) — extraction pipeline
- [DataCamp — Mem0 tutorial](https://www.datacamp.com/tutorial/mem0-tutorial) — extraction examples
- [DEV — Every AI Agent Framework Has a Memory Problem](https://dev.to/diego_falciola_02ab709202/every-ai-agent-framework-has-a-memory-problem-heres-how-i-fixed-mine-1ieo) — practitioner pain
- [VentureBeat — How xMemory cuts token costs and context bloat](https://venturebeat.com/orchestration/how-xmemory-cuts-token-costs-and-context-bloat-in-ai-agents) — bloat statistics
- [Towards Data Science — Practical Guide to Memory for Autonomous LLM Agents](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/) — failure modes
- [Letta docs — Memory management](https://docs.letta.com/advanced/memory-management/) — write triggers, function call patterns
- [Letta blog — Agent Memory](https://www.letta.com/blog/agent-memory) — automatic core/archival decisions

New sources discovered (added to research pool):
- [Mem0 paper — Production-Ready AI Agents with Scalable Long-Term Memory (arXiv 2504.19413)](https://arxiv.org/html/2504.19413v1)
- [Mesh Memory Protocol (arXiv 2604.19540)](https://arxiv.org/html/2604.19540) — multi-agent memory
- [Oracle — Agent Memory Why Your AI Has Amnesia](https://blogs.oracle.com/developers/agent-memory-why-your-ai-has-amnesia-and-how-to-fix-it)
