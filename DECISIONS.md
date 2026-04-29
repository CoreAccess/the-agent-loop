# Decisions Log

Quick reference for major decisions. Full narrative and rationale in `memory/project_framework_qa.md`.

---

## Framework Scope

| Date | Decision | Chosen |
|------|----------|--------|
| 2026-04-27 | Deliverable structure | Template repo + onboarding skill + Mintlify docs + skills for Claude/Gemini/Codex. CLI deferred to v2. |
| 2026-04-27 | Target audience | Design for experienced devs first (sharpest critics). Serve all via Mintlify docs. |
| 2026-04-27 | Category discovery approach | Hybrid — lock in list now, open to revision after research |
| 2026-04-27 | Research output format | Per-category docs → master framework spec → Mintlify |
| 2026-04-27 | Research approach | Broad sweep of all sources first, then deep per category |
| 2026-04-28 | Public framework name | Superseded: `Agent Project Foundation`; reopened because spoken word flow was weak. |
| 2026-04-29 | Public framework name | `The Agent Learning Loop (TALL)`; short/spoken name: `The Agent Loop`; repo slug: `the-agent-loop`; preferred internal folder: `.agent-loop`. |
| 2026-04-29 | Framework folder bootstrap | Create only `.agent-loop/README.md` now to reserve the folder name; defer deeper internal structure until the structure design is settled. |

## Categories

| Date | Decision | Chosen |
|------|----------|--------|
| 2026-04-27 | Categories 1 vs 8 overlap | Keep separate — Agent Contract and Change Gates are distinct design concerns |
| 2026-04-27 | spec-kit relationship | Research inspiration only — we own Category 4 fully |
| 2026-04-27 | Workflow cycle | Think→Plan→Build→Review→Test→Ship→Reflect is the framework spine; lives as Category 2 sub-category |
| 2026-04-27 | Observable Development | Promoted to Category 12 — proactive visibility is distinct from reactive error handling |

## Category 2 — Project Bootstrap & Onboarding

| Date | Decision | Chosen |
|------|----------|--------|
| 2026-04-27 | Onboarding skill output | Conversation → Shared Vision → human confirms → full project bootstrap |
| 2026-04-27 | Onboarding question flow | Hybrid: fixed core of 5-6 universal questions + adaptive branches by project type |
| 2026-04-27 | "I don't know" handling | Pending Decisions — Blocking vs Non-blocking. Non-blocking gets visible default. Blocking = gate before bootstrap. |
| 2026-04-27 | Project depth selection | Auto-detected from onboarding answers. Falls back to one question: Quick Start vs Full Setup. No tier vocabulary exposed. |
| 2026-04-27 | Existing file handling | Blocking files (constitution, AGENTS.md, CONTRACT.md): show diff, ask. Everything else: skip if exists. |
| 2026-04-27 | Constitution vs AGENTS.md | Constitution = why (rationale). AGENTS.md = what (facts, rules, tech stack). Agent reads AGENTS.md first, consults constitution for reasoning. |
| 2026-04-27 | Complexity ceilings (Q6) | DEFERRED — needs research. Initial position: full autonomy inside codebase; only stop for very large reworks or significant refactors. |
| 2026-04-27 | Mid-phase interruption | STATUS.md handoff note + phase checklist. Agent writes both at session end, reads both at session start. |
| 2026-04-27 | Phase depth for small tasks | All 7 phases always present. Depth scales to the task — a bug fix Think phase may be one sentence. |
| 2026-04-27 | Reflect memory distillation | Agent drafts candidate memories. Human reviews and approves/edits/rejects. Nothing written until approved. |
| 2026-04-27 | CONTRACT.md amendments | AI proposes with rationale. Human approves. AI makes the edit. Recorded in DECISIONS.md. |

## Framework Principles

| Date | Decision | Chosen |
|------|----------|--------|
| 2026-04-27 | Language standard | Plain language everywhere — no jargon. Every term must be understood in under 2 seconds. |
| 2026-04-27 | Agent code cleanup | Agents must remove code when features are removed, unless used elsewhere. Dead code is not acceptable. |
| 2026-04-27 | Housekeeping | Cleanup is first-class work. Remove temp files, keep docs in sync, flag stale content during Reflect. |
| 2026-04-27 | Apply framework to itself | As framework decisions are made, apply them to this project. Re-evaluate and catch up periodically. |
| 2026-04-28 | Token & context efficiency | Framework-wide design constraint: minimize token + context-window usage without losing functionality. Storage backend (file/DB/vector/hybrid) is a primary research lever. Each research doc gets a "Token cost" section. |
| 2026-04-29 | Always-loaded file budgets | Use soft size budgets with warnings for core/current-context files. Agents should suggest moving detail into skills, docs, or archival memory when these files grow too large. |
| 2026-04-29 | Source-specific retrieval guidance | Keep v1 retrieval portable by default. Document Anthropic Contextual Retrieval as an advanced Anthropic-specific option, not the cross-agent default. |
| 2026-04-29 | JIT memory-loading instruction | Root agent instructions should say to start from index/status, load only task-relevant memory files, and broaden only when retrieval fails or the task needs more context. |
| 2026-04-29 | Memory consolidation timing | Use a stage-based policy: markdown v1 consolidates during Reflect/batch lint; product-grade DB or managed memory may use foreground checks for high-impact writes plus periodic lint. |
| 2026-04-29 | Personal memory tiers | Within a project-local `.agent-loop`, use two personalization tiers: always-loaded identity/style/workflow preferences, and conditional personal history/life facts loaded only when relevant. |
| 2026-04-29 | Memory scope ambiguity | Use the heuristic inside the current project: generally reusable preference vs project-only fact. Cross-project persistence is deferred. If uncertain or sensitive, ask during Reflect. |
| 2026-04-29 | Orphan and stale memory policy | Use health-check signals first, plus optional review windows as weak prompts. Never delete or expire memory automatically. |
| 2026-04-29 | Local MCP memory bridge | Include local MCP memory servers as an optional advanced v1 graduation path for shared local recall; keep them out of onboarding defaults. |
| 2026-04-29 | V1 personalization boundary | `.agent-loop` is project-local in v1. Personalization settings and taste adaptation do not automatically carry across projects; cross-project behavior is deferred to future CLI/shared-memory work. |
| 2026-04-29 | Product-grade memory backend | When memory becomes product data, recommend Postgres first, with `pgvector` as an optional retrieval index. Standalone vector DBs are for large semantic corpora. |
| 2026-04-29 | Private memory ignore defaults | Generate ignore defaults for private memory: `.agent-loop/memory/private/` and `*.private.md`. Secrets, credentials, and PII still do not belong in memory. |
| 2026-04-29 | Project-local personalization schema | In v1, personalization memories use `scope: project` plus `kind: personalization`, not `scope: personal`, because `.agent-loop` is project-local. |
| 2026-04-29 | Team scope schema hook | Reserve `scope: team` as a future schema value, but clearly mark team/shared memory as unsupported in v1. |
| 2026-04-29 | Memory migration bridge | Keep current `memory/` authoritative during research. Add a note that future TALL project memory is expected under `.agent-loop/memory/`; defer migration until structure is settled. |
