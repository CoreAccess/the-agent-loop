---
name: AI Framework Project — Core Decisions
description: Q&A decisions from grill-me session establishing framework scope, deliverables, audience, and preliminary categories. Update this file at every major decision point.
type: project
---

# AI Framework Project — Core Decisions

**Why:** Building an advanced framework for AI-assisted software development — template repo + onboarding skill + Mintlify docs + skills for top 3 agents. This memory preserves all Q&A so context is never lost to compaction.
**How to apply:** Load this file at the start of every session on this project. Update it before context gets long.

---

## Project Summary

Building an advanced AI-assisted development framework. It is both a product (template repo + skills) and a research project that expands over time.

Date established: 2026-04-27

---

## Decisions Log

### Q1 — Deliverable Structure (decided 2026-04-27)
- **Phase 1 (launch):** Template repository as base
- **Phase 2 (launch):** Human-in-the-loop onboarding skill (more advanced than grill-me) — generates shared vision doc, then full project bootstrap
- **Phase 3 (launch):** Mintlify documentation site — educates people on the framework and why it matters
- **Skills:** Built for top 3 agents: Claude Code, Gemini, Codex/ChatGPT
- **CLI tool:** Deferred to v2 (luxury, not launch requirement)

### Q2 — Target Audience (decided 2026-04-27)
- Design for **B first** (experienced AI-assisted devs — sharpest critics, best validators)
- Serve A (personal use), B (experienced devs), C (broader community)
- Mintlify docs unlock C without diluting the framework itself

### Q3 — Onboarding Skill Output (decided 2026-04-27)
- Answer: **D** — conversation → shared vision document → human confirms → full project bootstrap
- Bootstrap includes: AGENTS.md + planning docs (STATUS, DECISIONS, BACKLOG, architecture stubs) + memory scaffolding
- AGENTS.md is part of the full bootstrap, not separate

### Q4 — Category Discovery Approach (decided 2026-04-27)
- Answer: **C — Hybrid**
- Lock in preliminary list now, use as scaffold during research, open to splits/merges/additions after first pass
- Process: decide → research → document → re-grill → build → test
- Evidence-based: all decisions backed by web research

---

## Categories (v2 — updated after broad sweep research 2026-04-27)

| # | Category | What it covers | Status |
|---|----------|----------------|--------|
| 1 | Agent Contract | AGENTS.md / CLAUDE.md / GEMINI.md — authority, scope, rules, architecture constraints | Broad sweep done |
| 2 | Project Bootstrap & Onboarding | Init skill, shared vision doc, full scaffolding from zero. **Sub-category: Development Lifecycle** (Think→Plan→Build→Review→Test→Ship→Reflect) — this cycle heavily guides the whole framework | Broad sweep done |
| 3 | Planning & Architecture Docs | ADRs, STATUS, DECISIONS, BACKLOG — living agent memory | Broad sweep done |
| 4 | Spec-Driven Development | Specs before code, how specs constrain agent behavior. spec-kit is research inspiration here, not an integration target | Broad sweep done |
| 5 | Skills & Reusable Capabilities | Skill ecosystem design, cross-agent portability, skill authoring standards | Broad sweep done |
| 6 | Memory Systems | Session vs. long-term memory, memory types, when/what to persist. Karpathy wiki pattern + Databricks episodic/semantic hierarchy | Broad sweep done |
| 7 | Testing & Verification Loops | Quality gates, test strategies, completion checklists, fail-fast patterns, LLM-as-judge | Broad sweep done |
| 8 | Change Gates & Guardrails | Always/ask/never patterns, blast radius awareness, security constraints. Keep separate from Category 1 | Broad sweep done |
| 9 | Context Loading & Management | Task-to-doc maps, layered context loading, scoped skills on-demand (2-4k vs 10-20k token efficiency) | Broad sweep done |
| 10 | Error Handling & Recovery | Error logs, recovery loops, how agents surface and learn from mistakes | Broad sweep done |
| 11 | Agentic Patterns | ReAct, Reflection, Human-in-the-Loop, Planning patterns. Multi-agent is v2 | Broad sweep done |
| 12 | Observable Development | Proactive visibility during active work — progress logs, artifact inspection, running score/status tracking. Distinct from Error Handling (reactive) | Broad sweep done |

---

### Q5 — Research Phase Output (decided 2026-04-27)
- Answer: **C** — per-category research docs in `docs/research/` feed into a single master framework spec
- Per-category docs are working notes; master spec is the publishable design document and seed for Mintlify

### Q6 — Research Approach (decided 2026-04-27)
- Answer: **C** — broad sweep of all 12 links in parallel first, cluster findings against 11 categories, identify gaps, then go deep per category with targeted web searches
- Caveat: links are not perfect, some may be irrelevant — apply judgment
- spec-kit (https://github.com/github/spec-kit) is the priority link — it is the closest competitor and may already cover ground we plan to build

### Public name simplification (decided 2026-05-02)
- Public-facing name going forward is **The Agent Loop**.
- Drop the `TALL` acronym and stop calling the project `The Agent Learning Loop`, except when preserving historical context.
- Repo slug remains `the-agent-loop`; preferred internal framework folder remains `.agent-loop`.

### The Agent Loop v0.1 primary goal (decided 2026-05-02)
- v0.1 should focus on a **minimal tested scaffold**: the smallest project-local one-agent scaffold supported by Experiments 001-003.
- Self-application remains the operating method for building the project, but it is not the v0.1 product surface.
- Open Goal decisions remain: lifecycle wording with explicit Research phase, exact v0.1 artifact list, next validation experiment, and rule-promotion evidence threshold.

### The Agent Loop v0.1 loop shape (decided 2026-05-02)
- Conceptual loop accepted: Research first, then convert findings into a goal, do the work, record evidence, check results, reflect, and promote only what worked.
- `Research` is clear and should stay as the first phase.
- Public loop wording should be plain-language, and each step should be one or two words.
- The other terms from the draft loop (`Distill`, `Goal Packet`, `Execute`, `Trace`, `Evaluate`, `Promote`) need clearer public wording before they are finalized.

### Goal terminology (decided 2026-05-02)
- Stop calling the goal artifact `Goal Packet` in active and public framework language.
- Refer to the artifact as **Goal**; do not make "The" part of the formal term.
- Historical experiment paths, filenames, and titles may remain unchanged where changing them would obscure artifact provenance.

### v0.1 public loop wording (decided 2026-05-02)
- Final v0.1 public loop wording: `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`.
- Rationale: the wording is plain-language, compact, and keeps each step to one or two words while preserving the accepted loop shape.

## Resolved Questions

- **Categories 1 vs 8:** Keep separate. Research confirms: agent identity/contract (Codified Rules) and enforcement/guardrails (Security Sandbox, Policy Generation) are architecturally distinct. They coexist in AGENTS.md today but are separate design concerns.
- **spec-kit relationship:** Research inspiration only. We may diverge over time. Periodically check spec-kit for new innovations but own Category 4 fully ourselves.
- **Workflow cycle (Think→Plan→Build→Review→Test→Ship→Reflect):** Lives as sub-category of Category 2 but heavily guides the whole framework — it's a spine, not just a sub-section.
- **Observable Development:** Promoted to Category 12. Distinct from Error Handling (proactive visibility vs. reactive recovery).
- **Workflow Design as separate category:** Absorbed into Category 2 as sub-category (not a standalone category).

## Category 2 Re-Grill Decisions

### Reflect phase memory distillation — Re-Grill Q9 (decided 2026-04-27)
- **B** — agent drafts candidate memories, human reviews and approves/edits/rejects before anything is written
- Agent does the synthesis work; human is the final filter
- This creates a loop where the agent learns the human's preferences over time — what they approve, what they reject, what they refine shapes future drafts

### Emerging ideas from Q9 (flagged for future research — scope risk noted)
- **Preference learning:** The memory system should build a picture of how this specific human likes to work over time — not just project facts but working style, taste, decisions patterns. Feeds back into how the agent behaves in future sessions.
- **Error pattern tracking (self-healing):** Agent should track tool calls or approaches that repeatedly fail before succeeding with a different method. Over time: stop defaulting to failing patterns, favor proven ones. This is a self-improving feedback loop distinct from one-off error recovery (Category 10).
- **Scope risk:** Both ideas are deep rabbit holes. Capture as seeds only. Do not expand until core categories are research-complete. Candidate for a new Category 13 — Self-Improving Agent, or as expansions of Category 6 (Memory) and Category 10 (Error Handling).

### Minimum phase set for a quick task — Re-Grill Q8 (decided 2026-04-27)
- **B** — all 7 phases always present, depth scales to the task
- No phases skipped — a bug fix still has Think, Plan, etc. but they may be one sentence each
- Keeps the habit and the safety net intact without adding overhead for small tasks

### Mid-phase interruption — Re-Grill Q7 (decided 2026-04-27)
- **A + C** — handoff note (STATUS.md) covers "where are we"; phase checklist covers "what's left"
- Agent writes/updates both at session end and reads both at session start
- No reliance on human memory for state

### Complexity ceiling granularity — Re-Grill Q6 (DEFERRED — needs research + synthesis)
- None of the four original options (A-D) are good — they all err toward restriction, which kills agent creativity
- Core tension: agents need freedom to think and make choices (coding is an artform, not just a spec); but too many auth prompts slow work and annoy the user
- Insight 1: **Default should be freedom, not restriction.** Good foundations (constitution + AGENTS.md) do the real work. Hard stops reserved only for genuinely irreversible or external-consequence actions.
- Insight 2: **Agents actively avoid removing code** — a well-known LLM behavior. Dead code accumulates. The framework must explicitly mandate cleanup: when removing a feature, agent must trace and remove all attached code unless it's referenced elsewhere.
- Insight 3: These are two separate problems: (a) what stops the agent, (b) what makes the agent clean up after itself. Conflating them into "complexity ceilings" was the wrong frame.
- **Initial instinct (user, 2026-04-27):** Full autonomy inside the codebase. Deploys and API calls also fine. Only stop and ask if the task is a very large rework or involves a significant refactor.
- **Next action:** Research how other frameworks handle agent freedom vs. guardrails, and how they enforce code cleanup/deletion. Then re-grill to sharpen "large rework" into a workable definition.

### Constitution vs AGENTS.md overlap — Re-Grill Q5 (decided 2026-04-27)
- **A with refinement** — Constitution = why. AGENTS.md = what (facts, rules, tech choices).
- Tech stack specifics live in AGENTS.md (e.g. `React, Tailwind, TypeScript`). The rationale for those choices lives in the Constitution.
- Agents read AGENTS.md first; consult Constitution only when they need context behind a decision.
- This keeps AGENTS.md small and agent-optimized. No duplication. Constitution wins on conflict.

### Three-tier project setup — Re-Grill Q4 (decided 2026-04-27)
- **D with B as safety net** — skill auto-detects depth from onboarding answers; no explicit tier selection
- If uncertain, falls back to a single clarifying question: "Quick Start" vs "Full Setup"
- No named tiers exposed to user (contradicts plain language rule)

### Onboarding question flow (decided 2026-04-27)
- **C + branches:** Fixed core of 5-6 universal questions, then adaptive branches by project type
- Universal core: project type, new vs. existing project, tech stack, launch definition, hard constraints

### "I don't know yet" handling (decided 2026-04-27)
- TBDs become **Pending Decisions** tagged with context clues gathered so far
- AI watches for signals as conversation develops and attempts to resolve through evidence-based research
- End of onboarding: AI closes remaining TBDs through research + human confirmation
- Every question pre-classified: **Blocking** (can't start without it) vs **Non-blocking** (sensible default applies)
- Non-blocking TBDs always have a fallback default — visible and explicit in generated files (e.g. `Tech stack: Python + FastAPI [DEFAULT — change this if you decide otherwise]`)
- Blocking TBDs remaining after research = explicit gate before bootstrap runs

### Existing file handling (decided 2026-04-27)
- **Blocking files** (constitution, AGENTS.md, CONTRACT.md): show diff, ask user — overwrite / skip / merge
- **Everything else** (planning docs, memory files): skip if exists, note what wasn't touched

### Plain language (decided 2026-04-27)
- "Greenfield" → "New Project"
- "Brownfield" → "Existing Project"
- All framework language must be instantly understandable at first glance — no jargon anywhere

### CONTRACT.md amendment rule (decided 2026-04-27)
- AI may propose amendments with rationale in structured format
- AI may never self-amend without explicit human approval in that session
- Once approved: AI makes the edit and records in DECISIONS.md

## Category 6 Re-Grill Decisions

### Memory vocabulary and metadata (decided 2026-04-28)
- **Hybrid taxonomy chosen.** User-facing docs should use practical memory buckets such as user, feedback, project, and reference.
- Each memory file should still carry structured metadata for `type`, `scope`, and `tier` so the system stays technically rigorous, supports storage/retrieval decisions, and can migrate to richer backends later.
- Rationale: cognitive-science terms are useful for design but too abstract for normal users. Practical labels keep the framework usable while metadata preserves precision.

### File roles in memory structure (decided 2026-04-28)
- **Hybrid file-role approach chosen.** Framework implementer docs should explicitly define file roles such as index, source, log, memory record, and schema.
- Onboarding and user-facing docs should avoid presenting "file role" as a formal taxonomy. They should explain each file in plain language by what it is for.
- Rationale: file role is a real architectural distinction separate from `type`, `scope`, and `tier`, but exposing it as another axis during normal use adds unnecessary jargon.

### Working memory and current context (decided 2026-04-28)
- **Hybrid wording chosen.** Technical specs may use "working memory" as part of the memory model.
- User-facing docs should call this "current context" and focus on practical behavior: only always-needed material belongs in core context; everything else should be loaded just in time.
- Rationale: working memory matters for token cost and attention, but "current context" is clearer and avoids making users learn cognitive-science vocabulary.

### Procedural memory placement (decided 2026-04-28)
- **Split by frequency and authority.** `AGENTS.md` holds always-loaded, mandatory procedural behavior.
- Skills hold task-specific or reusable procedural playbooks that should load only when relevant.
- If a skill becomes universally required, promote the relevant rule into `AGENTS.md`. If an `AGENTS.md` section becomes too detailed or task-specific, move it into a skill.
- Rationale: this keeps core context small while preserving authority for rules the agent must always follow.

### Memory scope for v1 (decided 2026-04-28)
- **Personal + project scope chosen for v1.** Personal preferences and working style live in user-scoped memory. Project decisions, architecture, status, and conventions live in repo-scoped memory.
- Team/shared memory is real but deferred to v2 because it requires access control, conflict handling, and shared infrastructure.
- Rationale: personal preferences should not have to be re-taught for every project, while project memory should travel with the code and be versioned.
- **Superseded/refined on 2026-04-29:** v1 is project-local because The Agent Loop is installed as a `.agent-loop` folder per project. Project-local personalization remains in scope; automatic cross-project preference carryover is deferred.

### Team scope schema hook (decided 2026-04-29)
- **Reserve `scope: team` now.** The schema may allow `scope: team` as a future value so team/shared memory can be added later without renaming the field.
- V1 docs must clearly state that team/shared memory is not implemented in launch scope.
- Rationale: team memory is a real future need, but it requires access control, conflict handling, and shared infrastructure. Reserving the value keeps migration easy without promising v1 behavior.

### Memory storage location (decided 2026-04-28)
- **Split location chosen with a privacy escape hatch.** Personal memory lives in user space and is not committed. Project memory lives in the repo and is committed/versioned by default.
- Private or sensitive project memory is allowed but must be explicitly marked untracked or stored outside the repo.
- Rationale: project memory should travel with the code and use git as its audit trail, but the framework should not pretend every project memory is safe to commit.
- **Superseded/refined on 2026-04-29:** v1 cannot depend on user-space cross-project memory because The Agent Loop is installed as a project-local `.agent-loop` folder. Project-local personalization is in scope for v1; true cross-project personalization is deferred.

### V1 project-local personalization boundary (decided 2026-04-29)
- **Project-local v1 boundary chosen.** In v1, a user starts a project or adopts an existing project by adding a `.agent-loop` folder to that specific project.
- A new project starts with a fresh `.agent-loop`; The Agent Loop v1 has no reliable mechanism to know or carry cross-project behavior, preferences, or taste adaptation.
- Personalization settings can exist inside the current project's `.agent-loop`, but they should be understood as project-local personalization unless the user manually copies them.
- Cross-project personalization is deferred to future CLI/shared-memory work, where a user-space store or managed setup could make stable preferences portable.
- Rationale: the framework should not promise behavior it cannot implement in v1. Project-local setup is simpler, honest, and matches the launch mechanism.

### Memory scope ambiguity heuristic (decided 2026-04-29)
- **Default heuristic chosen inside the current project.** If a memory is a generally reusable user preference, classify it as personalization within this project's `.agent-loop`. If it applies only to the current project, classify it as project-scoped.
- If the item is genuinely uncertain or sensitive, ask during Reflect instead of guessing.
- Rationale: this gives agents a practical default without making every memory save a classification interview, while respecting the v1 boundary that preferences do not automatically carry across projects.

### Personal memory budget (decided 2026-04-28)
- **Tiered personal memory with a soft budget chosen.** Always-loaded personal memory should stay tiny: identity, communication style, and workflow preferences.
- Larger personal facts should live as archival/on-demand memory and load only when relevant.
- The framework should warn when always-loaded personal memory grows too large, but should not hard-fail on an exact token or byte cap because token counts vary by agent and tokenizer.
- Rationale: personal context is useful across projects, but every always-loaded token competes with current project context.

### Personal memory tiers (decided 2026-04-29)
- **Two project-local personalization tiers in v1 chosen.** Always-loaded personalization memory should include only identity, communication style, and workflow preferences relevant to the current project.
- Broader personal history, life facts, employer/project history, and context that may be irrelevant or inappropriate in another project should be conditional/on-demand.
- Rationale: style preferences may be useful inside the current project, but v1 does not provide automatic cross-project carryover. Wider personal context should load only when it matters to avoid privacy leakage and core-context bloat.

### Memory save triggers (decided 2026-04-28)
- **Hybrid save model chosen.** Bounded handoff/log updates can be automatic. Explicit user signals such as "remember this" can trigger candidate memories. Durable memory files are proposed during Reflect and require human approval.
- Continuous memory extraction is out of scope for v1.
- Rationale: the framework needs enough automatic state capture to resume sessions safely, but durable memory must remain trustworthy and visible to the human.

### Auto-write boundaries for memory files (decided 2026-04-28)
- **Automatic writes are limited to `STATUS.md` and append-only logs.** These files support resumability and audit without changing durable memory beliefs.
- Durable memory records and the memory index require explicit human approval before they are created or changed.
- Rationale: editing memory records or retrieval hooks changes what future agents believe or load, so those changes need human review.

### Memory file schema strictness (decided 2026-04-28)
- **Full frontmatter schema required for v1 markdown memory files:** `name`, `description`, `type`, `scope`, `tier`, `source`, `created`, `updated`, and `status`.
- Rationale: the extra fields are cheap in markdown and valuable for migration, retrieval, health checks, and trust. `tier` helps prevent context bloat; `created`/`updated` support recency and decay; `status` supports superseded/deprecated memory without deleting history; `source` prevents hallucinated memories from becoming ground truth.

### Project-local personalization schema (decided 2026-04-29)
- **Use `scope: project` plus `kind: personalization` in v1.** Personalization memories live inside the project-local `.agent-loop`, so `scope` should reflect the actual storage and authority boundary.
- Do not use `scope: personal` for v1 project-local personalization, because that implies cross-project persistence the launch mechanism does not provide.
- Do not overload `type` with `preference`; `type` remains reserved for the memory taxonomy such as semantic, episodic, procedural, or reference.
- Rationale: project-local preferences and taste adaptation are real, but the schema must not pretend they follow the user across projects.

### Memory source stamps (decided 2026-04-28)
- **Flexible typed source stamps chosen.** The `source` field may use typed references such as `session:`, `commit:`, `file:`, `issue:`, `url:`, or `user-confirmed:` depending on where the memory came from.
- The invariant is that every durable memory needs a source a future human or agent can inspect.
- Rationale: different memory types come from different evidence. Decisions made in chat may point to `user-confirmed:<date>` or `session:<date>`; code facts may point to `file:<path>` or `commit:<sha>`; research claims may point to `url:<source>`.

### Durable memory reject list (decided 2026-04-28)
- **Broad reject list chosen.** Durable memory should reject secrets, credentials, PII, transient reasoning, small talk, general definitions, facts derivable from the repo, anything not source-stamped, anything not human-approved, anything already covered by an existing memory, and anything likely to expire quickly.
- The framework should be biased toward not saving. Durable memory should hold things specific to this user, this project, or this decision trail.
- Rationale: memory bloat and hallucinated saves reduce trust. If the agent can cheaply rediscover something from code, docs, or public knowledge, it does not belong in durable memory.

### Reflect memory candidate volume (decided 2026-04-28)
- **Soft cap chosen.** Reflect should aim to surface 1-3 high-confidence durable memory candidates per session.
- The agent may exceed the soft cap only when the session genuinely produced unusually many durable decisions or lessons.
- Rationale: human-approved memory works only if review stays lightweight. Too many candidates cause rubber-stamping; a hard cap risks hiding important decisions from dense sessions.

### Implicit pattern capture (decided 2026-04-28)
- **Cautious implicit-pattern capture chosen for v1.** Reflect may propose inferred preference or behavior-pattern memories.
- Inferred candidates must be clearly labeled as inference, include the observations that support them, and require human confirmation before being saved.
- Rationale: implicit preferences are valuable but risky. The safe pattern is: "I infer X from Y and Z. Should I remember that?"

### Default memory retrieval strategy (decided 2026-04-28)
- **Index-driven just-in-time retrieval chosen for v1, with keyword search as a supporting tool.** Keep the memory index in core/current context and load individual memory files only when relevant.
- Agents should use keyword/full-text search (`rg` or equivalent) when exact terms, paths, names, or identifiers are needed.
- Vector or hybrid retrieval is a graduation path, not the v1 default.
- Rationale: index-driven JIT gives the best cost/complexity ratio for small and moderate project memory while preserving token budget and avoiding full-load context bloat.

### JIT memory-loading instruction (decided 2026-04-29)
- **Default behavior with judgment chosen.** Root agent instructions should tell agents to start from the memory index and current status, load only memory files relevant to the current task, and broaden only when retrieval fails or the task genuinely needs more context.
- Avoid a brittle "never load memory unless needed" hard rule, because some tasks need wider background to prevent false confidence or missed decisions.
- Rationale: this preserves token discipline while giving agents enough judgment to recover when the first retrieval pass is insufficient.

### Always-loaded file size budgets (decided 2026-04-29)
- **Soft budgets with warnings chosen.** Always-loaded files such as `AGENTS.md`, root adapter files, `STATUS.md`, and the memory index should have target size ranges rather than hard caps.
- When these files grow too large, agents should warn and suggest moving detail into skills, deeper docs, or archival memory files.
- Rationale: core/current context is expensive, but hard caps create fake precision because tokenizers, project needs, and agent harnesses vary. Principle-only guidance is too easy to ignore.

### Memory index format (decided 2026-04-28)
- **Minimal index entries chosen.** Each `MEMORY.md` entry should include title, link, and a high-quality one-line retrieval hook.
- The full metadata belongs in the memory file frontmatter, not duplicated in the index.
- Rationale: the memory index is core context, so every extra field is a recurring token tax. The index's job is retrieval triage, not full metadata display.

### Retrieval graduation criteria (decided 2026-04-28)
- **Hybrid graduation criteria chosen.** Framework docs should publish rough memory-size thresholds as orientation, but pain signals are the real trigger for graduating beyond markdown/index-driven memory.
- Pain signals include: agent often misses memories that exist, index upkeep becomes painful, retrieval requires semantic similarity over large prose, or multiple writers need concurrency.
- Rationale: numeric thresholds help users reason, but they should not become fake rules. Retrieval failure plus maintenance burden matters more than count alone.

### Source-specific retrieval optimizations (decided 2026-04-29)
- **Advanced provider-specific option chosen.** Anthropic Contextual Retrieval should be documented as a useful graduation path for Claude/Anthropic-heavy projects, not recommended as the portable v1 default.
- The Agent Loop's default retrieval guidance should remain cross-agent: index-driven just-in-time loading, keyword search for exact terms, and backend graduation based on retrieval pain.
- Rationale: Anthropic Contextual Retrieval has strong evidence, but the framework should not couple its default memory model to one provider's technique. Agent-specific optimizations are acceptable when clearly labeled.

### Storage backend ladder (decided 2026-04-28)
- **Graduated backend ladder chosen.** V1 project memory starts as repo markdown. SQLite/local MCP, Postgres with optional pgvector, dedicated vector databases, graph memory, and managed memory services are graduation paths, not onboarding defaults.
- Recommended positioning: repo markdown for default v1 project memory; SQLite/local MCP for many local sessions or cross-agent local recall; Postgres + optional pgvector for product-grade or multi-user memory; dedicated vector DBs for large unstructured semantic corpora; graph/managed memory for advanced or v2/team-oriented scenarios.
- Rationale: the framework should start with portable, inspectable, versionable memory and graduate only when real pain appears.

### Product-grade memory backend (decided 2026-04-29)
- **Postgres-first recommendation chosen.** When memory becomes product data, The Agent Loop should recommend Postgres as the serious default backend.
- `pgvector` should be positioned as an optional retrieval index inside Postgres, not as the core memory model.
- Standalone vector databases should be recommended for large unstructured semantic corpora or proven semantic-retrieval pain, not ordinary structured preferences, decisions, source stamps, status, audit, and access-control needs.
- Rationale: product memory usually needs transactions, metadata filtering, auth, audit, backups, joins, and operational maturity. Vector search is useful, but it is one index over the durable record.

### Local MCP memory bridge (decided 2026-04-29)
- **Optional advanced v1 path chosen.** The Agent Loop should mention local MCP memory servers as a graduation path for users who need shared local recall across Codex, Claude Code, Gemini, Cursor, or similar agents.
- Local MCP memory should not be part of default onboarding.
- Rationale: it is a practical bridge between repo markdown and product-grade database memory, but it adds enough tooling complexity that it should remain opt-in.

### Vector database positioning (decided 2026-04-28)
- **Strong guidance chosen.** Framework docs should say not to start with a vector database unless the user has large unstructured prose or proven semantic-search pain.
- Vector DBs are useful as a graduation path, but they are a bad default for structured project memory, preferences, and decisions.
- Rationale: starting with vector storage adds embedding, model, index, retrieval, and maintenance burden before the user has proved they need semantic retrieval.

### Graph memory schema hooks (decided 2026-04-28)
- **`supersedes` only for v1.** Add an optional `supersedes` frontmatter field to support memory invalidation and replacement.
- Do not add a general `related` field in v1. Broader relationship graphs are deferred until graph memory has real tooling.
- Rationale: `supersedes` is immediately useful for memory health, while manual relationship fields can become noisy graph maintenance before the framework needs them.

### Delete vs supersede policy (decided 2026-04-28)
- **Depends on memory value.** Decisions and rationale should be superseded so history remains inspectable. Low-value mistakes, duplicates, bad inferred preferences, broken references, and stale operational facts may be deleted after approval.
- Rationale: important decision trails deserve history, but memory health also requires removing clutter. For committed project memory, git history already provides an audit trail for deleted files.

### Memory health and lint cadence (decided 2026-04-28)
- **Layered lint cadence chosen.** Reflect should include a light memory health check every session. Deeper memory lint runs periodically or when memory problems appear.
- Light Reflect check: look for duplicate or conflicting memories created this session, stale assumptions surfaced during the work, obvious broken links, and format issues.
- Deep lint: broader scan for contradictions, orphan memories, stale files, schema drift, and retrieval/index problems.
- Rationale: memory health should be habitual, but full lint every session would create unnecessary overhead and prompt fatigue.

### Memory consolidation timing (decided 2026-04-29)
- **Stage-based consolidation chosen.** Markdown/default v1 should consolidate during Reflect or periodic batch lint rather than running duplicate/contradiction checks before every write.
- Product-grade database or managed-memory backends may use foreground `ADD / UPDATE / DELETE / NOOP`-style checks for high-impact writes, plus periodic lint.
- Rationale: v1 should stay lightweight and human-readable, while higher-stakes or higher-volume backends can justify the latency and model-call cost of foreground consistency checks.

### Stale memory handling (decided 2026-04-28)
- **Contextual stale-memory prompts chosen.** Reflect should ask what memory needs updating or superseding when the session changed direction, reversed a decision, altered architecture, corrected an assumption, or otherwise made prior memory suspect.
- Do not ask a generic "what changed?" question every session.
- Rationale: high-value stale memory is hard to catch automatically, but asking every session creates prompt fatigue.

### Orphan and stale memory policy (decided 2026-04-29)
- **Hybrid review-signal policy chosen.** V1 markdown memory should flag stale or orphan candidates during lint when files are unindexed, broken-linked, superseded, contradicted, or stale-looking.
- Optional review windows such as "not touched in 90 days" may be used as weak review prompts, never as proof that a memory is wrong.
- No memory should be deleted or expired automatically. Human approval is required for deletion or supersession.
- Rationale: age can help find memory that deserves review, but old decisions can remain valid. Cleanup should preserve trust and auditability.

### Recency and decay defaults (decided 2026-04-28)
- **Recency as tie-breaker chosen.** When retrieving or reconciling active memories, explicit status/authority comes first, relevance second, source quality third, and recency breaks ties.
- Recency should not be the primary rule. A newer offhand comment should not outweigh an older deliberate decision.
- Rationale: recency helps when memories are otherwise comparable, but over-weighting it can destabilize deliberate decisions and long-lived project principles.

### Append-only logs (decided 2026-04-28)
- **Lightweight append-only logs chosen for v1.** Every project should get an append-only log or equivalent, but entries should capture notable events rather than full transcripts.
- Log entries should cover decisions made, handoffs, major failures/recoveries, memory changes proposed or approved, and session close summaries.
- Rationale: automatic writes are allowed for append-only logs, so the framework needs a clear destination for those writes. Keeping logs lightweight prevents transcript bloat.

### Conversation summary policy (decided 2026-04-28)
- **No default separate conversation summaries.** The framework should use `STATUS.md` for current handoff state, append-only logs for notable events, and durable memory files for distilled beliefs, decisions, and preferences.
- Session/conversation summary files should be exceptional, not part of the default loop.
- Rationale: default session summaries create another growing recall layer that overlaps with better-scoped artifacts.

### Memory backend export requirement (decided 2026-04-28)
- **Hard export rule chosen.** Any memory backend the framework recommends must export to plain Markdown or JSON.
- Rationale: memory becomes one of the most valuable artifacts in the project. If it is trapped inside a vendor, agent harness, vector store, or opaque service, the framework has failed its portability goal.

### No-git projects and memory auditability (decided 2026-04-28)
- **Strongly recommend git, do not hard-block.** If a project is not a git repo, the framework should explain that project memory is designed to be versioned and ask whether to initialize git before creating repo-scoped memory.
- Users may proceed without git for quick or local experiments.
- Rationale: the framework leans on git as the audit trail for committed project memory, but blocking bootstrap entirely would be too heavy for small experiments.

### Apply Category 6 decisions to this project (decided 2026-04-28)
- **Partial low-risk self-application chosen.** After Category 6, this project should align low-risk memory conventions such as schema/frontmatter, `STATUS.md`, `MEMORY.md`, and log conventions.
- Larger structure changes should be deferred until the full framework research phase settles.
- User is open to initializing a git repo for this project now, but public repo framing must be decided first because the project should be findable by other developers while clearly marked as an untested work in progress.
- Rationale: the project should apply the framework to itself without creating unnecessary churn before the framework spec stabilizes.

### Public repository framing (decided 2026-04-28)
- **Public research-project framing chosen.** If this project is initialized as a git repo and made public/findable, it should present itself as an active research and build project, not a stable framework template or alpha product.
- README and repository description should clearly say the project is public so experienced AI-assisted developers can inspect the research, follow decisions, and offer feedback while APIs, file structure, templates, and recommendations may still change.
- Rationale: public discoverability supports feedback and credibility, but the project must not imply production readiness before the framework has been tested.

### README positioning themes (decided 2026-04-28)
- README should open with the practical pain of AI coding workflows: lost context, decision drift, forgotten project history, repeated bug loops, weak handoffs, and agents repeatedly rediscovering the same failures.
- README should clearly state the framework's value: a stronger starting foundation for AI-assisted development, with project memory, onboarding, agent contracts, lifecycle loops, guardrails, and reusable skills.
- README should position the framework as more advanced and broader than spec-kit-style workflows: spec-driven development is one layer, but this project covers the wider operating system around AI-assisted software work.
- Keep the repo framed as active research / untested WIP, but make the opening engaging and problem-led rather than stale or mechanical.
- Approved README wording emphasizes that the framework helps agents work with the project rather than just the current prompt, avoids recurring bug loops, and gives developers a stronger starting foundation.

### Memory filename conventions (decided 2026-04-28)
- **Loose descriptive filename convention chosen.** Memory filenames should be descriptive, stable, human-readable, and use lowercase kebab-case or snake_case.
- Avoid vague names like `notes.md`. Avoid date-first names unless the date is genuinely the topic, such as an append-only log entry.
- Do not require type/scope prefixes because those duplicate frontmatter and make filenames noisier.
- Rationale: filenames are part of retrieval, but the retrieval value comes from clear topic names, not rigid metadata encoding.

### Private project memory defaults (decided 2026-04-28)
- **Private folder plus private filename suffix chosen.** The framework should provide a standard ignored private memory folder such as `memory/private/` and also support an ignored filename suffix such as `*.private.md`.
- Private memory is for sensitive project context, not secrets, credentials, or PII. Those should still be rejected from memory entirely.
- Rationale: a private folder is clear for humans, while a private filename suffix helps when private memory belongs near related public memory.

### Private memory ignore defaults (decided 2026-04-29)
- **Generate ignore defaults in v1.** The Agent Loop should add ignore patterns for `.agent-loop/memory/private/` and `*.private.md`.
- These defaults should be created during bootstrap so private project memory is not accidentally committed.
- Secrets, credentials, API keys, tokens, and PII still do not belong in memory at all.
- Rationale: the private-folder and private-suffix convention only works if the generated repo hygiene matches it by default.

### Project-root clutter concern (opened 2026-04-28)
- User raised a new structural concern: the framework should avoid cluttering the user's project filesystem with too many top-level files and folders.
- Possible direction: keep most framework contents inside a dedicated framework folder, with only minimal root-level marker/adapter files where agent auto-discovery requires them.
- Possible enhancement: start with a default folder name, then during onboarding detect or ask about the user's filesystem naming conventions and align the framework folder name where reasonable.
- Needs re-grill because this affects bootstrap structure, context loading, agent discovery, and public template ergonomics.

### Framework folder structure (decided 2026-04-28)
- **Dedicated framework folder plus thin root adapters chosen.** Most framework files should live in one dedicated folder to avoid cluttering the user's project root.
- Root-level files should be minimal markers/adapters only where agent auto-discovery requires them, such as `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`, pointing agents to the real framework files.
- The dedicated folder name is not decided. It should derive from the eventual framework name, not a generic placeholder like `.ai-framework`.
- Rationale: this keeps user projects clean while preserving predictable agent discovery.

### Framework folder placeholder (decided 2026-04-29)
- **Placeholder-only approach chosen.** Create `.agent-loop/README.md` now to reserve the agreed internal framework folder name.
- Do not create deeper `.agent-loop` structure yet; wait until the framework structure design is settled.
- Rationale: this applies the naming decision and keeps momentum without prematurely locking the internal layout.

### Memory migration bridge (decided 2026-04-29)
- **Minimal bridge chosen.** Keep the current root `memory/` folder authoritative during this research phase.
- Add a note to `.agent-loop/README.md` that future Agent Loop project memory is expected to live under `.agent-loop/memory/`.
- Do not migrate memory files until the broader framework folder structure is settled.
- Rationale: this captures the direction without moving core memory files before structure work is complete.

### Plain language for self-application (decided 2026-04-29)
- Avoid using "dogfood" or "dogfooding" in user-facing framework language.
- Use plain wording such as "apply the framework to itself," "use The Agent Loop on this project," or "self-application."
- Rationale: "dogfood" is common engineering shorthand for using your own product, but it is jargon and conflicts with The Agent Loop's plain-language principle.

### Framework naming research (opened 2026-04-28)
- User wants to choose a memorable framework name now before locking folder names or public repo framing.
- Name requirements: popular/easy to remember/easy to say, distinct inside the AI-assisted software development industry, no obvious direct competition or confusingly similar project, acronym or short name useful if clever enough.
- Requires GitHub and general web research before deciding.
- User prefers the next pass to consider science-fiction-inspired names or human names, especially short female names that can expand into a meaningful acronym.
- Early research eliminated several names due to direct or adjacent AI/developer-tool conflicts:
  - `Ada`: used by multiple AI assistants, including Mercury's open source developer onboarding chatbot Ada and Read AI's Ada digital twin.
  - `Ava`: direct AI coding assistant usage, including Ava/Supernova in the Visual Studio Marketplace and other AVA assistant projects.
  - `Samantha`/`Annie`: already used by AI assistants with developer, SRE, IDE, or MCP-adjacent positioning.
  - `Nora`, `Nia`, `Orla`, `Lyra`, `Alma`, `Maia`, `Cora`, `Clio`, `Ivy`, `Diana`: direct AI coding agent, AI agent framework, AI memory, or developer-tool collisions.
  - `MABEL` was attractive as "Memory, Agents, Bootstrap, Evidence, Lifecycle," but GitHub has an exact `mabel-framework` project that calls itself "Mabel Framework," so it should be avoided for public framework naming.
- User rejected `Anne` / `ANNE` as the active direction because the acronym expansion felt forced, especially "Norms" as the middle `N`.
- New naming pass shifted to unpopular short human female names, using SSA-derived baby-name data as the rarity filter and then checking general web + GitHub for AI/dev/framework collisions.
- Strong collision eliminations from the rare-name pass:
  - `Enora`: direct active `Enora-AI` quality engineering / compliance automation product, too close to this framework's evidence and quality-gate territory.
  - `Sanna`: direct active trust infrastructure for AI agents, including policy enforcement and governance receipts, too close to guardrails/change-gate territory.
  - `Anouk`: direct AI-powered browser extension framework.
  - `Dione`: direct AI app installer / open-source AI application platform.
  - `Alva`, `Nera`, `Evia`, `Niva`, `Vira`, `Lira`, `Avra`, `Miren`, `Nessa`: direct AI products, AI agents, AI platforms, or AI-ready developer/service platforms.
- Current strongest shortlist from the rare-name pass:
  - `Eleri` / `ELERI`: "Evidence-Led Engineering Repository Intelligence" or "Evidence-Led Engineering Review Intelligence"; rare in SSA-derived data and no obvious direct AI/dev/framework collision found.
  - `Ilona` / `ILONA`: "Iterative Lifecycle Onboarding and Navigation Architecture"; rare and no direct AI/dev/framework collision found.
  - `Siona` / `SIONA`: "Structured Iteration, Onboarding, and Navigation Architecture"; rare, with only weak/irrelevant AI character or small-repo noise found so far.
  - `Aelia` / `AELIA`: "Agentic Evidence Lifecycle Intelligence Architecture"; rare and acronymically strong, but has soft brand noise from Aelia/Tech Aelia software businesses.
  - `Tavia` / `TAVIA`: "Traceable Agentic Verification and Iteration Architecture"; rare and acronymically strong, but has soft AI-assistant/domain/business noise.
  - `Zelia` / `ZELIA`: possible "Zero-drift Evidence-Led Iteration Architecture"; rare and relatively clean, but the `Z` expansion is less natural than the top candidates.
- User rejected the rare-name shortlist and asked to loosen the naming criteria toward a decent, descriptive, plain-English repository name that can be remembered and does not obviously conflict with similar projects.
- Plain-English collision pass found `AgentProjectKit` already used in adjacent AI-engineering/project-bootstrap material, so avoid `Agent Project Kit` even though it initially sounded strong.
- Superseded plain-English recommendation: `Agent Project Foundation` / repo slug `agent-project-foundation`. This was later replaced by `The Agent Learning Loop (TALL)` on 2026-04-29.
- Rationale: it is descriptive, memorable enough, explains the repo as a foundation for AI-assisted software projects, avoids the generic/stale `AI Framework` wording, and had no obvious exact same-space collision in the quick GitHub/web pass.

### Framework public name (decided 2026-04-28, superseded 2026-04-29)
- **Name chosen:** `Agent Project Foundation`.
- **Long descriptive form:** `The Agent Project Foundation framework`.
- **Repo slug:** `agent-project-foundation`.
- Avoid `Agent Project Foundational Framework` because it reads more awkwardly, and avoid making the official slug `agent-project-foundation-framework` unless a host platform forces extra disambiguation.
- Collision check found no exact GitHub repository hits for `Agent Project Foundational Framework`, `Agent Project Foundation Framework`, `agent-project-foundational-framework`, or `agent-project-foundation-framework`.
- Rationale: the short name is plain English, memorable, and flexible; the long form still communicates that this is a framework without turning the repo name into a mouthful.
- Superseded by `The Agent Learning Loop (TALL)`.

## Framework Principles (non-category — apply everywhere)

### Cross-Discipline Research (established 2026-04-27)
The hardest problems in this framework — how agents make decisions, manage uncertainty, set boundaries, learn from mistakes, define ethical constraints — are versions of problems humans have studied for a long time. These fields are active research sources, not just inspiration:

- **Human decision-making / cognitive psychology:** How humans make decisions under uncertainty, handle ambiguity, and avoid cognitive traps. Directly applicable to how agents should decide, when to stop, and how to handle "I don't know."
- **The scientific method:** Hypothesis → experiment → observe → conclude → iterate. Our development cycle (Think→Plan→Build→Review→Test→Ship→Reflect) is structurally the same loop. When framework decisions are hard, ask: what would the scientific method do here?
- **Self-regulation and habit psychology:** How humans monitor their own behavior, correct mistakes, and build consistent habits over time. Directly feeds into the self-healing / self-improving agent ideas (potential Category 13).
- **Learning theory and memory science:** How humans form memories, what gets retained vs. forgotten, how experience transfers to new situations. Directly applicable to Category 6 (Memory Systems).
- **Ethics and philosophy:** How do we define "right" behavior when rules conflict? What are the moral constraints on an autonomous agent? Relevant to Category 8 (Change Gates) and Category 1 (Agent Contract). Philosophy has argued about agency and responsibility for centuries — mine it.
- **Systems thinking:** How complex systems behave, feedback loops, emergent behavior, and unintended consequences. Applicable to the whole framework, especially multi-agent (v2).
- **Management and organizational science:** How humans delegate, set accountability, and manage performance. Directly maps to how a developer manages an agent — the power dynamic and trust model is similar.

**How to apply:** When a category's questions feel genuinely hard — no clear answer, all options have tradeoffs — search these fields for analogous problems. The answer may already exist under a different name.

### Research Sources (established 2026-04-27)
Deep research must include real-world developer sources, not just official docs and blog posts:
- **Reddit and developer forums** — the best source for pain points and frustrations. Developers complaining about a tool or pattern are telling you what actually breaks in practice. Start with obvious subreddits but actively look for new communities as research progresses — the list of places developers gather should grow over time, not stay fixed.
- **GitHub** — reference implementations, real solutions to real problems, and emerging patterns. Issues and discussions are especially valuable — they show where frameworks fall short and how the community works around it.
- **Actively discover new sources:** as research uncovers new communities, forums, Discord servers, newsletters, or discussion spaces where developers are active, note them and add them to the research pool. The goal is to keep expanding the sources we check, not to rely on a fixed list that goes stale.
- **Weigh real-world sources heavily:** a consistent complaint across multiple forum threads is stronger signal than a polished blog post from a tool vendor. One source type describes the world as they want it; the other describes it as it is.

### Periodic Housekeeping (established 2026-04-27)
The framework must treat cleanup as first-class work, not an afterthought. Specific behaviors:
- Remove temporary files once they've served their purpose (e.g. links.md → deleted after broad sweep, content folded into research docs)
- Keep docs in sync with decisions — a doc that contradicts a later decision is worse than no doc
- Restructure the file system as the project grows — don't let early scaffolding become permanent clutter
- Remove stale questions, outdated sections, and draft artifacts on a regular cadence
- This should be a named step in the Reflect phase: "Is anything here that shouldn't be?"
- Agent freedom to suggest housekeeping during Reflect; human approves what gets removed

## Open Questions

- **Category 11 scope:** Which specific agentic patterns (ReAct, Reflection, Human-in-the-Loop, Planning) are core to v1 vs. v2? Needs deep research.
- **File system structure:** How should the framework's own directory structure be organized? (noted as future research task)
- **Cross-agent portability in Category 5:** How much of each skill can be shared across Claude/Gemini/Codex vs. must be agent-specific?
- **Three-tier project setup:** Quick / Standard / Full — what does each tier generate? (Category 2 open question)
- **Constitution vs AGENTS.md overlap:** What goes in each? How do we avoid duplication? (Category 2 open question)
- **Complexity ceiling granularity:** How specific should CONTRACT.md ceilings be? (Category 2 open question)
- **Mid-phase interruption:** What happens when a session ends mid-lifecycle-phase? (Category 2 open question)

---

## Research Sources (from links.md)

- https://github.com/github/spec-kit
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://github.com/paulDuvall/ai-development-patterns
- https://machinelearningmastery.com/the-roadmap-to-mastering-agentic-ai-design-patterns/
- https://www.databricks.com/blog/memory-scaling-ai-agents
- https://github.com/google-gemini/gemini-skills/
- https://github.com/mattpocock/skills/tree/main
- https://github.com/garrytan/gstack
- https://dev.to/sarony11/agentic-platform-engineering-how-to-build-an-agent-infrastructure-that-scales-from-your-laptop-to-11np
- https://devblogs.microsoft.com/all-things-azure/agentic-platform-engineering-with-github-copilot/
- https://developers.openai.com/codex/use-cases/frontend-designs
- https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems

---

## RESUME FROM HERE — Next Session Start Point

**Status:** Mid Re-Grill on Category 2. User took a break after Q3 was answered. Q4 was posed but NOT answered.

**Exact next action:** Greet the user, confirm they want to continue the re-grill, then re-ask Re-Grill Q4 below — do not skip it or assume an answer.

### Re-Grill Q4 — Three-tier project setup (UNANSWERED — ask this first)

"Three-tier project setup: Quick / Standard / Full"

BMAD uses three tracks for different project scales. We need to decide if we do the same, because this determines what the project setup generates and how long the onboarding conversation runs.

- **(A) No tiers — one size fits all.** Every project gets the full setup. Simple to explain, but overkill for a quick bug fix or tiny weekend script.
- **(B) Two tiers — "Quick Start" and "Full Setup."** Quick Start = constitution stub + CONTRACT.md + AGENTS.md only. Full Setup = everything. User picks at the start.
- **(C) Three tiers — "Task", "Project", "System."** Task = single feature or bug fix, minimal artifacts. Project = standard product or MVP, full artifacts. System = complex multi-domain system. User picks at the start.
- **(D) Auto-detected from onboarding answers.** No explicit tier selection — skill infers right depth from what it learns. If uncertain, falls back to B as a single clarifying question.

My recommendation: **D with B as safety net.** Auto-detection is most frictionless. Three explicit tiers (C) adds vocabulary the user has to learn before they've done anything — contradicts our plain language principle.

### Remaining Re-Grill Questions After Q4

After Q4 is answered, continue with these in order:

**Q5 — Constitution vs AGENTS.md overlap**
Both files could end up with similar content (architecture rules, tech stack). What goes in each and how do we avoid duplication?

**Q6 — Complexity ceiling granularity**
How specific should CONTRACT.md ceilings be? Too coarse = ignored. Too fine = impossible to maintain.

**Q7 — Mid-phase interruption**
What happens when a user's session ends mid-lifecycle-phase (e.g. mid-Build)? How does the next session pick up?

**Q8 — Minimum phase set for a quick task**
Does a simple bug fix need to run the full Think→Plan→Build→Review→Test→Ship→Reflect cycle, or is there a lighter path?

**Q9 — Reflect phase: auto vs manual memory distillation**
Does the Reflect skill automatically push learnings to the memory system, or does the human review and approve what gets persisted?

---

## Session Log

| Date | What happened |
|------|--------------|
| 2026-04-27 | Initial grill-me session. Q1-Q4 resolved. Preliminary category list (11 categories) sketched. AGENTS.md and memory system created. Memory moved to project root. |
| 2026-04-27 | Q5-Q6 resolved (research output = per-category docs → master spec; approach = broad sweep first). Broad sweep research completed across 9/12 links. Categories updated to v2 (12 categories). Observable Development added as Category 12. Workflow cycle (Think→Plan→Build→Review→Test→Ship→Reflect) confirmed as Category 2 sub-category and framework spine. spec-kit confirmed as research inspiration only. Broad sweep doc written to docs/research/broad-sweep.md. Next: deep research per category. |
| 2026-04-27 | Category 2 deep research complete. 4 sub-category docs written to docs/research/category-2/. Key findings: CONTRACT.md (complexity ceilings) should be a first-class bootstrap artifact; greenfield/brownfield split is fundamental to bootstrap design; gstack's 7-phase sprint cycle with explicit handoffs is the strongest reference implementation; "Think" phase is most underinvested and should be mandatory; Reflect phase is the bridge to Category 6 (Memory). BMAD surfaced as major framework worth studying. Next: re-grill Category 2 findings, then choose next category. |
| 2026-04-27 | Category 2 re-grill started. Q1-Q3 answered (see Category 2 Re-Grill Decisions above). Q4 posed but user took a break — unanswered. Q4-Q9 queued in RESUME FROM HERE section. RESUME.md created at project root for session pickup. AGENTS.md updated with resume instructions. |
| 2026-04-27 | Category 2 re-grill completed. Q4-Q9 all answered. Key additions: auto-detected project depth (D+B), Constitution=why/AGENTS.md=what split, Q6 deferred for deep research (agent freedom vs. guardrails + code cleanup behavior), phase checklists + STATUS.md handoff for interruption, all phases always present (depth scales), human-approved memory distillation. Two new seeds flagged: preference learning and error pattern self-healing — scoped out of v1 research but noted as potential Category 13. Next: update category-2 docs, then deep research on next category. |
| 2026-04-27 | Housekeeping session. links.md and RESUME.md deleted. STATUS.md, DECISIONS.md, BACKLOG.md created — framework applied to itself. Research cycle checklist added to AGENTS.md. Framework principles added: housekeeping as first-class work, agent cleanup mandate, real-world research sources (Reddit/GitHub/forums + actively discover new communities), apply-framework-to-itself principle. Cross-discipline research principle added: psychology, philosophy, ethics, scientific method, and organizational theory are active research sources for hard framework problems. Session closed. Next session: Category 6 deep research — Memory Systems. |

### Category 6 deep research resumed (logged 2026-04-28)
- Resumed after prior model stopped mid-Category 6 due to rate limit.
- Loaded project contract, status, backlog, memory index, user profile, decisions, broad sweep, and all existing Category 6 docs.
- Confirmed five first-pass Category 6 docs already existed: kinds of memory, what to save and when, what to load and when, keeping memory healthy, and memory boundaries.
- Added the missing sixth first-pass doc: `docs/research/category-6/6-storage-backends.md`.
- Category 6 deep research is now first-pass complete. Next action: prepare and run Category 6 re-grill questions one at a time; no Category 6 decisions are finalized until re-grill.

### Project-local Codex grill-me skill installed (logged 2026-04-28)
- User clarified the Claude skill source is `.claude/skills/grill-me` and that the Codex install should live inside this project, not in Codex's global user skill directory.
- Added only `grill-me` to `.codex/skills/grill-me` inside the repo.
- Copied the Claude `SKILL.md` unchanged and added Codex UI metadata at `.codex/skills/grill-me/agents/openai.yaml` so the skill is easier to find.
- Removed the mistaken global copy at `C:\Users\adamd\.codex\skills\grill-me`; the project-local copy is the intended source.
- Codex's Python validator could not run because the local Python environment is missing `yaml`; manual structural checks confirmed the skill has `name`, `description`, display name, and `$grill-me` default prompt metadata.

### Category 6 re-grill started (logged 2026-04-28)
- Category 6 re-grill began after first-pass Memory Systems research.
- Q1 decided: use hybrid memory vocabulary. Practical user-facing buckets stay visible; structured metadata records `type`, `scope`, and `tier`.
- Q2 decided: define file roles explicitly in implementer docs while keeping user-facing docs plain-language and purpose-based.
- Q3 decided: technical specs may use "working memory"; user-facing docs should say "current context" and teach just-in-time loading discipline.
- Q4 decided: always-loaded mandatory procedural behavior belongs in `AGENTS.md`; task-specific procedural playbooks belong in skills, with promotion/demotion between the two as usage changes.
- Q5 decided: v1 supports personal + project scope; team/shared memory is deferred to v2.
- Q6 originally decided: personal memory lives in user space and project memory lives in the repo. Superseded/refined by Q45/Q48: v1 `.agent-loop` is project-local, so personalization memories use `scope: project` plus `kind: personalization`; cross-project user memory is deferred.
- Q7 decided: personal memory uses a tiny always-loaded core plus archival/on-demand personal facts; enforce with a soft budget/warning, not a hard cap.
- Q8 decided: use a hybrid save model: automatic bounded handoff/log updates, explicit event-triggered candidate memories, human-approved durable memories during Reflect, and no continuous extraction in v1.
- Q9 decided: automatic writes are limited to `STATUS.md` and append-only logs; durable memory records and memory index updates require explicit human approval.
- Q10 decided: v1 markdown memory files require full frontmatter: `name`, `description`, `type`, `scope`, `tier`, `source`, `created`, `updated`, and `status`.
- Q11 decided: source stamps use flexible typed references such as `session:`, `commit:`, `file:`, `issue:`, `url:`, or `user-confirmed:`; every durable memory must be inspectable.
- Q12 decided: durable memory has a broad reject list and should be biased toward not saving unless the item is specific, source-stamped, human-approved, non-duplicative, and durable.
- Q13 decided: Reflect should surface 1-3 high-confidence durable memory candidates by default, exceeding that soft cap only after unusually decision-dense sessions.
- Q14 decided: Reflect may propose implicit-pattern memories in v1, but they must be labeled as inference, cite supporting observations, and require human confirmation.
- Q15 decided: v1 uses index-driven just-in-time memory retrieval, supported by keyword search for exact terms; vector/hybrid retrieval is a later graduation path.
- Q16 decided: memory index entries stay minimal: title, link, and one-line retrieval hook; full metadata stays in file frontmatter.
- Q17 decided: use rough numeric thresholds for orientation, but treat retrieval failure and maintenance burden as the real triggers to graduate beyond markdown/index-driven memory.
- Q18 decided: v1 starts with repo markdown and documents a graduation ladder through SQLite/local MCP, Postgres + optional pgvector, vector DBs, graph memory, and managed services.
- Q19 decided: docs should strongly warn users not to start with vector databases unless they have large unstructured prose or proven semantic-search pain.
- Q20 decided: add optional `supersedes` as the only v1 graph-style schema hook; defer broader relationship fields such as `related`.
- Q21 decided: supersede decisions and rationale, but allow approved deletion for low-value mistakes, duplicates, bad inferred preferences, broken references, and stale operational facts.
- Q22 decided: use layered memory health checks: light Reflect lint every session, deeper lint periodically or when memory problems appear.
- Q23 decided: Reflect asks stale-memory questions only when the session changed direction, reversed a decision, altered architecture, corrected an assumption, or made prior memory suspect.
- Q24 decided: recency is a retrieval/reconciliation tie-breaker after status/authority, relevance, and source quality.
- Q25 decided: v1 creates a lightweight append-only log for notable events, not full transcripts.
- Q26 decided: no default separate conversation summaries; use `STATUS.md`, append-only logs, and durable memory files instead.
- Q27 decided: every recommended memory backend must export to plain Markdown or JSON.
- Q28 decided: strongly recommend git for repo-scoped memory auditability and ask whether to initialize it, but do not hard-block quick/local experiments.
- Q29 decided: partially apply Category 6 decisions to this project after the category closes; low-risk memory conventions now, larger structural migrations later. Git setup is acceptable but needs public/WIP framing first.
- Q30 decided: if public, frame this as an active research and build project for AI-assisted software development frameworks, not a stable template or alpha product.
- Q31 decided: README positioning should lead with concrete AI coding pain points, especially recurring bug loops and weak starting foundations, and explain that this framework is broader/more advanced than spec-kit-style spec-only workflows. User approved the drafted wording.
- Q32 decided: memory filenames should use loose descriptive naming: stable, human-readable kebab-case or snake_case topic names, without mandatory type/scope prefixes.
- Q33 decided: use both a standard ignored private memory folder and private filename suffix; private memory is not for secrets/credentials/PII.
- Q34 decided: use one dedicated framework folder plus minimal root adapter files for agent discovery. Folder name remains blocked on framework naming.
- Q35 originally decided: final name was `The Agent Learning Loop (TALL)`, short/spoken name `The Agent Loop`, repo slug `the-agent-loop`, and preferred internal folder `.agent-loop`. Superseded on 2026-05-02 by public name `The Agent Loop`.
- Q36 decided: create only `.agent-loop/README.md` now as a placeholder; defer deeper internal structure until structure design is settled.
- Q37 decided: always-loaded files use soft size budgets with warnings; agents should suggest moving detail into skills, docs, or archival memory when files grow too large.
- Q38 decided: document Anthropic Contextual Retrieval as an advanced Anthropic-specific option, not as The Agent Loop's portable v1 retrieval default.
- Q39 decided: root agent instructions should explicitly enforce JIT memory loading as default behavior with judgment: start from index/status, load task-relevant memory, broaden only when needed.
- Q40 decided: use stage-based memory consolidation timing: markdown v1 consolidates during Reflect/batch lint; product-grade DB or managed memory may use foreground checks for high-impact writes.
- Q41 decided: project-local personalization uses two tiers in v1: always-loaded identity/style/workflow preferences relevant to the current project, and conditional personal history/life facts loaded only when relevant.
- Q42 decided: ambiguous memory scope uses the project-local heuristic: generally reusable preference vs project-only fact; if uncertain or sensitive, ask during Reflect. Cross-project persistence is deferred.
- Q43 decided: orphan/stale memory cleanup uses health-check signals first, optional review windows as weak prompts, and never automatic deletion/expiration.
- Q44 decided: include local MCP memory servers as an optional advanced v1 graduation path, but not an onboarding default.
- Q45 decided: v1 personalization is project-local because `.agent-loop` is installed per project. Cross-project behavior, preference carryover, and taste adaptation are deferred to future CLI/shared-memory work.
- Q46 decided: when memory becomes product data, recommend Postgres first, with `pgvector` as an optional retrieval index; standalone vector DBs are for large semantic corpora.
- Q47 decided: v1 should generate private-memory ignore defaults: `.agent-loop/memory/private/` and `*.private.md`; secrets, credentials, and PII are still rejected from memory entirely.
- Q48 decided: v1 project-local personalization memories should use `scope: project` plus `kind: personalization`, not `scope: personal`; `type` remains reserved for the memory taxonomy.
- Q49 decided: reserve `scope: team` as a future schema value, while clearly marking team/shared memory as unsupported in v1.
- Q50 decided: keep current `memory/` authoritative during research, add a bridge note that future Agent Loop memory is expected under `.agent-loop/memory/`, and defer migration until structure is settled.

### Framework naming rare-name pass (logged 2026-04-28)
- User rejected `Anne` / `ANNE` and clarified that acronym expansions must sound logical and cool, not merely match letters.
- Ran a rare short female-name pass using SSA-derived baby-name data, then checked likely candidates against general web and GitHub.
- Eliminated multiple attractive names due to direct AI/dev/framework collisions, especially `Enora`, `Sanna`, `Anouk`, `Dione`, `Alva`, `Nera`, `Evia`, `Niva`, `Vira`, `Lira`, `Avra`, `Miren`, and `Nessa`.
- Current strongest shortlist to present back: `Eleri`, `Ilona`, `Siona`, `Aelia`, `Tavia`, and `Zelia`.

### Framework naming plain-English pass (logged 2026-04-28)
- User rejected the rare-name shortlist and asked to loosen criteria toward a descriptive, easy-to-remember repo name.
- Checked plain-English options against GitHub/web. `Agent Project Kit` should be avoided because `AgentProjectKit` already appears in similar AI-engineering bootstrap material.
- Recommended candidate at that time: `Agent Project Foundation` with repo slug `agent-project-foundation` (later superseded).

### Framework public name chosen (logged 2026-04-28)
- User approved the `Agent Project Foundation` direction and asked whether the long form should be `Agent Project Foundational Framework` or `Agent Project Foundation Framework`.
- Final naming decision: official name `Agent Project Foundation`; long descriptive form `The Agent Project Foundation framework`; repo slug `agent-project-foundation`.
- Quick collision check found no exact GitHub repository hits for the long forms or matching framework slugs. Keep `Agent Project Foundation` short in public-facing titles and use "framework" descriptively in prose.
- Superseded on 2026-04-29 by `The Agent Learning Loop (TALL)`.

### Framework naming reopened (logged 2026-04-29)
- User paused the folder-structure decision and reopened naming because `Agent Project Foundation` does not sound natural when spoken aloud.
- Preferred starting candidates from the user, in order: `Agent Foundation`, `Agent Workbench`, `Project Groundwork`.
- Initial conflict research found all three have meaningful collisions or confusion risk:
  - `Agent Foundation` overlaps with an existing `agent-foundation` AI agent skill and is close to the Linux Foundation's Agentic AI Foundation / AGENTS.md stewardship language.
  - `Agent Workbench` is already used by OutSystems and by multiple agent workbench projects.
  - `Project Groundwork` collides with an exact GitHub repository and the broader `Groundwork` term is active in AI/devtool workflows, including a VS Code extension and Claude Code plugin.
- No new final name has been chosen yet.

### AGI naming branch explored (logged 2026-04-29)
- User proposed testing `The AGI Framework`, `AGI Framework`, or AGI-foundation/framework language because the project is exploring a foundational way for software agents to perform better through goals, loops, adaptation, and memory.
- Live conflict research found `The AGI Framework` already used by an open-source modular AGI project, `AGI Foundation` has exact GitHub collisions, and the broader AGI namespace is crowded with AIOS Foundation/OpenAGI, Sentient Foundation, Hyperon AGI Framework, and other AGI-branded projects.
- Naming concern: `AGI` captures ambition but may overpromise or misframe this project as claiming to build AGI rather than a practical framework for AI-assisted software development. Prefer AGI-adjacent language only if it stays concrete and defensible.
- User rejected noun-stacked names like `Agent Intelligence Framework`; the name must have spoken flow and semantic coherence in a sentence. Treat `framework` as a descriptive subtitle, not necessarily part of the product name.
- Current strongest naming finalists from the user: `The Agent Loop` first, `Wayfinder` second. `The Agent Loop` has the best semantic fit and spoken flow, but "agent loop" is a known generic architecture phrase and already appears in AI/dev content. `Wayfinder` has strong brand feel but heavier direct collisions, including an AI-agent/blockchain Wayfinder and package-name usage.
- User noted that the acronym `TALL` would be useful if the long name could expand from `The Agent Loop ...`. Candidate expansion: `The Agent Learning Loop`, with public short name still `The Agent Loop`, slug `the-agent-loop`, and likely internal folder `.agent-loop`.
- Follow-up conflict check found no obvious exact-name ownership for `The Agent Learning Loop` or `TALL` tied to that phrase. Nearby concepts (`agent loop`, `agent learning loop`, `learning loop`) are broad/common and have scattered usage, so the name is not unique as a concept but appears usable as a project identity if positioned as `The Agent Loop` / `TALL`.
- Final naming decision: use `The Agent Learning Loop (TALL)` as the full name, `The Agent Loop` as the short/spoken name, `the-agent-loop` as the repo slug, and `.agent-loop` as the preferred internal framework folder. Root `README.md` should lead with `The Agent Learning Loop (TALL)`.

### Goal systems and decision loops research note (logged 2026-04-28)
- User raised an out-of-scope but relevant philosophical thread: human goals, survival constraints, money as a survival/resource mechanism, decision loops, scientific method, and AGI-like goal pursuit.
- Researched human motivation, hunter-gatherer survival constraints, money functions, cybernetic/scientific/OODA loops, LLM agent research, and AI safety/open-endedness.
- Captured a durable research note at `docs/research/future-goal-systems-and-decision-loops.md`.
- Main candidate idea: a lightweight "Goal Contract" that records objective, why, success criteria, constraints, resources, loop rules, stop conditions, escalation triggers, and learning capture. Do not add a new category yet; revisit after Category 6 closes.

### Gamble Lab lessons applied (logged 2026-04-29)
- User created a simple poker/gambling lab to help Codex reason about goals, constraints, adaptation, and testing.
- Folded the lesson from `.tmp/lesson.md` into `docs/research/future-goal-systems-and-decision-loops.md`.
- Key lessons preserved: goals are weak without constraints; plans need goal, environment model, and policy; tests should evaluate policy rather than only outcomes; adaptation can be harmful without confidence thresholds; stop rules and signal-vs-noise discipline matter.
- Captured a new future research thread in `BACKLOG.md`: framework evaluation/testing for goal pursuit, adaptability, stop-rule obedience, and real-world usefulness inside Codex. This likely belongs in Category 7, with links to goal systems and Observable Development.

### Repo identity started (logged 2026-04-29)
- Applied the final naming decision to the local repository identity.
- Added root `README.md` headed `The Agent Learning Loop (TALL)` and a basic `.gitignore`.
- Updated `STATUS.md`, `DECISIONS.md`, `BACKLOG.md`, and this memory file to use the new public name and mark `Agent Project Foundation` as superseded.
- Initialized a local Git repository and set the default branch to `main`; no initial commit has been made yet.

### Framework folder placeholder created (logged 2026-04-29)
- Ran a stale-path check for `AgentProjectFoundation`, `Agent Project Foundation`, and `agent-project-foundation`; no active stale paths were found. Remaining old-name references are historical/superseded decision-log entries.
- User chose the placeholder-only option for the dedicated framework folder.
- Created `.agent-loop/README.md` to reserve the internal folder name while deferring the final internal layout.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q36.

### Core context budget decision (logged 2026-04-29)
- User chose soft budgets with warnings for always-loaded files such as `AGENTS.md`, root adapter files, `STATUS.md`, and the memory index.
- Hard caps were rejected as too brittle across agents, tokenizers, and project needs.
- Principle-only guidance was rejected as too easy to ignore.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q37.

### Source-specific retrieval decision (logged 2026-04-29)
- User chose to document Anthropic Contextual Retrieval as an advanced Anthropic-specific option.
- TALL's v1 default remains portable across Codex, Claude Code, Gemini, and similar agents.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q38.

### JIT memory-loading instruction decision (logged 2026-04-29)
- User agreed to the default-with-judgment JIT loading rule.
- Root agent instructions should start agents from the memory index and current status, load only task-relevant memory files, and broaden only when retrieval fails or wider context is required.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q39.

### Memory consolidation timing decision (logged 2026-04-29)
- User agreed to the stage-based consolidation policy.
- Markdown/default v1 should keep writes lightweight and consolidate during Reflect or batch lint.
- Product-grade database or managed-memory backends may use foreground duplicate/contradiction checks for high-impact writes, while still running periodic lint.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q40.

### Personal memory tiers decision (logged 2026-04-29)
- User chose two personal tiers in v1.
- Always-loaded personal memory should stay limited to identity, communication style, and workflow preferences.
- Broader personal history/life facts should be conditional and loaded only when relevant.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q41.

### Memory scope ambiguity decision (logged 2026-04-29)
- User chose the default scope heuristic.
- Memories that apply across projects are personal; memories that apply only to the current project are project-scoped.
- If scope is genuinely uncertain or the memory is sensitive, ask during Reflect.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q42.

### Orphan and stale memory policy decision (logged 2026-04-29)
- User agreed to the hybrid stale/orphan policy.
- V1 markdown memory should flag cleanup candidates using health-check signals such as unindexed files, broken links, superseded records, contradictions, and stale-looking content.
- Optional age windows may prompt review but must not trigger automatic deletion or expiration.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q43.

### Local MCP bridge and v1 personalization boundary (logged 2026-04-29)
- User agreed that local MCP memory servers should be included as an optional advanced v1 graduation path, not a default onboarding requirement.
- User then clarified an important v1 boundary: TALL is added to each project as a fresh `.agent-loop` folder, so v1 has no real way to know cross-project behavior or adapt globally to personal tastes.
- Updated the memory model to treat v1 personalization as project-local. Cross-project personalization is deferred to future CLI/shared-memory work.
- Updated `STATUS.md`, `DECISIONS.md`, `BACKLOG.md`, and this memory file. Category 6 re-grill is now decided through Q45.

### Product-grade memory backend decision (logged 2026-04-29)
- User chose to explicitly recommend Postgres first when memory becomes product data.
- `pgvector` should be documented as an optional retrieval index, not the default memory model.
- Standalone vector databases remain a specialized option for large unstructured semantic corpora or proven semantic-search pain.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q46.

### Private memory ignore defaults decision (logged 2026-04-29)
- User agreed to generate private-memory ignore defaults in v1.
- Added `.agent-loop/memory/private/` and `*.private.md` to this repo's `.gitignore` as low-risk self-application.
- Reconfirmed that private memory is not for secrets, credentials, API keys, tokens, or PII; those should be rejected from memory entirely.
- Updated `.gitignore`, `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q47.

### Project-local personalization schema decision (logged 2026-04-29)
- User agreed that v1 personalization memories should be labeled as project-scoped rather than personal-scoped.
- Interpreted the schema as `scope: project` plus `kind: personalization`, because `type` is already reserved for the memory taxonomy.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q48.

### Team scope schema hook decision (logged 2026-04-29)
- User chose to reserve `scope: team` in the memory schema now.
- Team/shared memory remains deferred and unsupported in v1.
- Updated `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q49.

### Memory migration bridge and terminology clarification (logged 2026-04-29)
- User chose the minimal bridge for memory migration: keep current `memory/` authoritative during research and add a note that future TALL project memory is expected under `.agent-loop/memory/`.
- Added that note to `.agent-loop/README.md`.
- User asked what "dogfood" means and why it was used. It means using your own product/framework on itself, but it is jargon.
- Updated memory language to prefer "apply the framework to itself" or "self-application."
- Updated `.agent-loop/README.md`, `STATUS.md`, `DECISIONS.md`, and this memory file. Category 6 re-grill is now decided through Q50 and ready for docs update.

### Category 6 docs updated (logged 2026-04-29)
- Updated all six Category 6 research docs with Q1-Q50 re-grill decisions.
- Replaced old "Questions remaining" sections with applied-decision summaries.
- Corrected v1 personalization drift: `.agent-loop` is project-local, personalization memories use `scope: project` plus `kind: personalization`, and cross-project preference carryover is future CLI/shared-memory work.
- Updated `STATUS.md` to mark Category 6 re-grill and docs updated as done. Next step is Category 6 housekeeping.

### Category 6 housekeeping complete (logged 2026-04-29)
- Ran housekeeping after the Category 6 docs update.
- `.tmp` contained no files to clean up.
- Verified old `Agent Project Foundation` references are historical/superseded decision-log entries, not active naming drift.
- Updated `BACKLOG.md` to remove Category 6 from the active research queue and move Category 8 - Change Gates & Guardrails to the top recommendation.
- Updated `STATUS.md` to Step 6 closeout. Recommended next category is Category 8 because it directly covers the deferred Q6 thread on agent freedom, large reworks, and code cleanup.

### Session closed for the night (logged 2026-04-29)
- User chose not to start Category 8 tonight and asked to save out until the next session.
- Updated `STATUS.md` to mark Category 6 complete and closed out, with no active category.
- Next recommended action: confirm whether to start Category 8 - Change Gates & Guardrails. If confirmed, update `STATUS.md` to active Category 8 / Step 1 before researching.
- GitHub repo is configured and pushed at `https://github.com/CoreAccess/the-agent-loop.git`; `main` tracks `origin/main`.

### GitHub repository published (logged 2026-04-29)
- Created the initial local git commit: `1d2369d Initial TALL research framework`.
- Verified `.claude/` and `.codex/` are ignored and not tracked.
- Added remote `origin` as `https://github.com/CoreAccess/the-agent-loop.git`.
- Pushed `main` to GitHub and set it to track `origin/main`.

### AGENTS-SAMPLE.md removed from GitHub history (logged 2026-04-29)
- User noticed `AGENTS-SAMPLE.md` should have been ignored before the GitHub push and added it to `.gitignore`.
- Removed `AGENTS-SAMPLE.md` from tracking while keeping the local ignored copy.
- Rewrote git history to remove `AGENTS-SAMPLE.md` from every reachable commit, deleted local filter-branch backup refs, expired reflogs, ran garbage collection, and force-pushed cleaned `main` to GitHub.
- Verification showed no reachable commits or objects listing `AGENTS-SAMPLE.md`; remote `main` moved to cleaned commit `e1c0453`.
- Secret-pattern scans found only documentation text about secrets/tokens, not actual credential values, so there was nothing concrete to rotate from the exposed file.

### Agentic Engineering Transcript (logged 2026-04-29)
- User supplied the transcript for Brendan O'Leary's YouTube video "Agentic Engineering" as `transcript.md` in the project root.
- This serves as external reference material for AI-assisted workflows, context engineering, and the agentic engineering paradigm.
- Added `transcript.md` to `.gitignore` so the local transcript can remain available without being committed accidentally.

### Agentic Engineering research note captured (logged 2026-04-29)
- Created `docs/research/agentic-engineering-brendan-oleary.md` as an out-of-cycle research note.
- Treat the talk as supporting evidence only, not core truth or a framework decision source by itself.
- Main evidence threads captured: AI agents as junior-engineer-like collaborators, context engineering discipline, research-plan-implement workflow, AGENTS.md vs skills separation, permission tuning, MCP/tool context overhead, and PR-like review of agent work.
- Carry the note into Category 8 (guardrails/permissions), Category 9 (context loading), Category 5 (skills), Category 7 (verification), Category 11 (agentic patterns), and Category 12 (observable development).

### CMS incubator migration and v0.1 Goal started (logged 2026-05-02)
- User clarified that the CMS project should not continue; the CMS workspace is now only an incubator case study and possible future applied vertical.
- The Agent Loop is the focused project.
- User confirmed two v0.1 decisions: public name is `The Agent Loop` only, dropping `The Agent Learning Loop` and `TALL`; v0.1 primary goal is a minimal tested project-local one-agent scaffold supported by Experiments 001-003.
- Explicit Research must remain in the framework loop before major decisions are promoted. Research includes prior art, competing tools, GitHub discussions, docs, forums, developer pain, and adjacent fields when useful.
- User agreed with the v0.1 loop shape but said the terminology needs to be much clearer; `Research` can stay, and each public step name should be one or two words.
- User then clarified that active framework language should stop saying `Goal Packet` and should refer to the artifact as **Goal**, not **The Goal**.
- User accepted final v0.1 public loop wording: `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`.
- User paused next-task selection to review project filesystem organization, naming conventions, and scaling hygiene. They specifically raised deleting local `AGENTS-SAMPLE.md` and `transcript.md`, and noted file growth/context bloat as a concern that should be addressed but may not be the immediate top priority.
- Updated `STATUS.md`, `DECISIONS.md`, `BACKLOG.md`, `README.md`, `.agent-loop/README.md`, and this memory file for active naming and v0.1 decision state.
- Next action: inspect and recommend project filesystem organization before selecting the next implementation/research task.

### Root cleanup and Goal terminology correction (logged 2026-05-02)
- User clarified that the formal artifact term should be `Goal`, not `The Goal`, because "The Goal step" sounds unnatural.
- Updated active references and the v0.1 public loop wording to `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`.
- Deleted local ignored root files `AGENTS-SAMPLE.md` and `transcript.md`.
- Kept `.gitignore` entries for both files to prevent accidental reintroduction.
- Updated `AGENTS.md` so it no longer requires or lists `AGENTS-SAMPLE.md`.
- Updated the Agentic Engineering note to say the transcript was distilled into the note and removed.
- Left historical experiment names and paths intact, including `experiment-001-goal-packet`, because those preserve artifact provenance.

### Local agent folder cleanup before Codex restart (logged 2026-05-02)
- User requested deleting `.claude/` and `.tmp/`, renaming `.codex/` to `.agents/`, and saving state before restarting Codex.
- Deleted `.claude/` and `.tmp/`.
- Copied `.codex/` to `.agents/`; `.agents/skills/grill-me/SKILL.md` and `.agents/skills/grill-me/agents/openai.yaml` exist.
- Windows denied removal of `.codex/` because current Codex session files under `.codex/skills/grill-me/` are locked. User said they will delete `.codex/` manually before restart.
- Updated `.gitignore` to ignore `.agents/*`, while keeping `.claude/*` and `.codex/*` ignored as safeguards.
- Updated `AGENTS.md`, `DECISIONS.md`, `STATUS.md`, and this memory file so a fresh session can pick up the filesystem review.

### Filesystem review pickup and next-task recommendation (logged 2026-05-02)
- Loaded the required session context plus the CMS incubator case study and Experiment 003 evaluator review.
- Verified `.codex/`, `.claude/`, and `.tmp/` are absent after restart; `.agents/` exists locally and remains ignored.
- Current repo shape is coherent: root control files, `docs/research/`, `docs/case-studies/`, isolated `experiments/` capsules, authoritative research memory in `memory/`, and `.agent-loop/` as a placeholder only.
- Naming drift looks controlled: active docs use `The Agent Loop` and `Goal`; old `Goal Packet` / `goal-packet` names remain in historical experiment artifacts where provenance matters.
- Scaling risk to watch: `memory/project_framework_qa.md` is now about 90 KB / 717 lines, and experiments are the largest content area at about 316 KB across 93 files. Keep startup files short and rely on indexes plus just-in-time loading.
- Recommended next action: make one lightweight repository layout convention decision and document it, without bulk moves. Then start Category 8 - Change Gates & Guardrails because it directly covers Q6, agent freedom, large rework stop rules, and code cleanup.
