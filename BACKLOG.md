# Backlog

Consolidated open questions and future work. Organized by area.
Answered questions are removed. Deferred items are noted with reason.

---

## Research Queue — Categories Not Yet Deep-Researched

Priority order is a recommendation — user decides at each cycle.

| Priority | Category | Notes |
|----------|----------|-------|
| 1 | **1 — Agent Contract** | AGENTS.md / CLAUDE.md design — foundational |
| 2 | **3 — Planning & Architecture Docs** | ADRs, STATUS, DECISIONS, BACKLOG — we're building these now |
| 3 | **5 — Skills & Reusable Capabilities** | Cross-agent portability question lives here |
| 4 | **4 — Spec-Driven Development** | spec-kit is reference; we own this category |
| 5 | **7 — Testing & Verification Loops** | LLM-as-judge, quality gates, framework evaluation for goal pursuit/adaptability |
| 6 | **9 — Context Loading & Management** | Narrow loading, scoped skills |
| 7 | **10 — Error Handling & Recovery** | Recovery loops, error logs |
| 8 | **11 — Agentic Patterns** | ReAct, Reflection, HITL — multi-agent is v2 |
| 9 | **12 — Observable Development** | Proactive visibility, progress logs |

---

## Open Questions — Category 2 (Bootstrap & Onboarding)

**2.1 — Onboarding Skill**
- What is the minimum viable question set? (what do experienced devs ask before starting a project?)
- How does onboarding work for an existing project — skill needs to inspect the codebase, not just ask questions
- What's the right output format for the onboarding conversation? (feeds into 2.2)

**2.2 — Shared Vision & Constitution**
- How does the constitution evolve when a project changes direction (pivot)?
- Version history: in the constitution itself, or does git handle it?
- What does a constitution look like for an existing project with architecture already baked in?
- How should Category 8 guardrail decisions be integrated into the generated AGENTS.md / Goal / STATUS scaffold?

**2.3 — Bootstrap Generation**
- Exact file content for each generated artifact (Go web app vs Python data pipeline vs React SPA)
- What does existing-project codebase inspection look like per agent (Claude Code, Gemini, Codex)?
- Should bootstrap be re-runnable on an existing project without destroying what's there?
- Cross-agent skill installation — Claude skills ≠ Gemini skills, how do we handle this?

**2.4 — Development Lifecycle**
- What does our minimal `think` skill look like? (gstack uses 6 forcing questions)
- How do lifecycle skills differ across Claude Code, Gemini, and Codex?

---

## Open Questions — Framework-Wide

- **v0.2 planning:** v0.1 is frozen. Future scaffold/product changes should land in v0.2, starting from the lessons in Experiments 005-006.
- **v0.2 scaffold validation:** Retest concise five-question onboarding, existing-project root `AGENTS.md` merge behavior, and downstream "second prompt" behavior after root adapter creation.
- **README/release clarity:** For v0.2, replace any placeholder release wording with final GitHub Releases links and exact install wording.
- **Distribution mechanism:** v0.1 uses a GitHub Release ZIP containing only `.agent-loop/`. v0.2 can revisit separate starter repo, scaffold branch/tag, prompt placement, or packaging automation if validation shows friction.
- **Framework evaluation/testing:** How do we test The Agent Loop itself for goal pursuit, adaptability, stop-rule obedience, signal-vs-noise discipline, and real-world usefulness inside Codex?
- **File system structure:** How should the framework's own directory structure be organized as it grows?
- **Category 11 scope:** Which agentic patterns (ReAct, Reflection, HITL, Planning) are core v1 vs v2?
- **Cross-agent portability (Category 5):** How much of each skill can be shared across Claude/Gemini/Codex vs. must be agent-specific?

---

## Candidate Sources To Revisit

- **Category 5 / Category 8 overlap:** Search Engine Land, "How to build SEO agent skills that actually work" (Itay Malinski, 2026-05-01): useful for skills as workspaces, explicit tools, references, memory, templates, progressive disclosure, review layers, sandbox testing, and tool-boundary guardrails. URL: https://searchengineland.com/build-seo-agent-skills-476252

---

## Flagged for Future Research (not current scope)

- **Category 13 — Self-Improving Agent:** Agent tracks tool calls and approaches that repeatedly fail before succeeding. Over time, stops defaulting to failing patterns. Feeds into preference learning via Reflect phase. Deep rabbit hole — do not scope until core categories are complete.
- **Goal systems and decision loops:** Explore whether the framework needs a lightweight "Goal Contract" covering objective, why, success criteria, constraints, resources, loop rules, stop conditions, and learning capture. Research note: `docs/research/future-goal-systems-and-decision-loops.md`.
- **Evaluation lab / benchmark design:** Design tests that evaluate agent policy, not just task outcome. Candidate dimensions: did the agent follow the chosen strategy, fit the environment, avoid overreacting to noise, stop when rules required, and adapt only with enough evidence. Likely belongs in Category 7, with links to goal systems and Category 12 observable development.
- **Multi-agent orchestration:** Deferred to v2. Single-agent patterns first.
- **CLI tool:** Deferred to v2.
- **Cross-project user memory:** Deferred until there is a real mechanism such as a CLI, user-space memory store, or shared local service. Do not promise it in v1 docs.
- **Cross-project personalization:** V1 `.agent-loop` is project-local. Future CLI/shared-memory work may allow user preferences, taste adaptation, and learned working style to carry across projects.
- **LLM-as-judge patterns:** Will surface naturally in Category 7 research.
