# Project Status

Last updated: 2026-04-29

---

## Where We Are

**Phase:** Research - Category 6 (Memory Systems)  
**Active category:** 6 - Memory Systems  
**Cycle step:** Step 6 - Session log / closeout. Category 6 first-pass deep research, re-grill Q1-Q50, docs update, and housekeeping are complete. The framework is now named `The Agent Learning Loop (TALL)`, with `The Agent Loop` as the short/spoken name.

---

## Research Cycle Progress

| Category | Broad Sweep | Deep Research | Re-Grill | Docs Updated |
|----------|-------------|---------------|----------|--------------|
| 1 - Agent Contract | Done | Pending | Pending | Pending |
| 2 - Project Bootstrap & Onboarding | Done | Done | Done | Done |
| 3 - Planning & Architecture Docs | Done | Pending | Pending | Pending |
| 4 - Spec-Driven Development | Done | Pending | Pending | Pending |
| 5 - Skills & Reusable Capabilities | Done | Pending | Pending | Pending |
| 6 - Memory Systems | Done | Done | Done | Done |
| 7 - Testing & Verification Loops | Done | Pending | Pending | Pending |
| 8 - Change Gates & Guardrails | Done | Pending | Pending | Pending |
| 9 - Context Loading & Management | Done | Pending | Pending | Pending |
| 10 - Error Handling & Recovery | Done | Pending | Pending | Pending |
| 11 - Agentic Patterns | Done | Pending | Pending | Pending |
| 12 - Observable Development | Done | Pending | Pending | Pending |

---

## Completed In This Pickup

- Resumed after the prior model stopped mid-Category 6 due to a rate limit.
- Loaded `AGENTS.md`, `STATUS.md`, `memory/project_framework_qa.md`, `BACKLOG.md`, `memory/MEMORY.md`, `memory/user_profile.md`, and existing Category 6 docs.
- Confirmed five Category 6 docs already existed and were first-pass complete:
  - `docs/research/category-6/1-kinds-of-memory.md`
  - `docs/research/category-6/2-what-to-save-and-when.md`
  - `docs/research/category-6/3-what-to-load-and-when.md`
  - `docs/research/category-6/4-keeping-memory-healthy.md`
  - `docs/research/category-6/5-memory-boundaries.md`
- Added missing sixth doc: `docs/research/category-6/6-storage-backends.md`.
- Captured out-of-cycle research note: `docs/research/future-goal-systems-and-decision-loops.md`.
- Folded Gamble Lab / poker simulation lessons into the goal-systems research note: goals need constraints, tests should evaluate policy rather than only outcomes, and adaptation needs confidence thresholds.
- Captured framework evaluation/testing as future research for Category 7 and related goal-systems work.
- Chose the public framework name: `The Agent Learning Loop (TALL)`, short name `The Agent Loop`, repo slug `the-agent-loop`, preferred internal folder `.agent-loop`.
- Added root `README.md` and `.gitignore` to start the repository identity and hygiene.
- Ran a stale-path check for `AgentProjectFoundation`; no active stale paths were found. Remaining old-name references are historical/superseded decision-log entries.
- Created `.agent-loop/README.md` as a placeholder to reserve the framework folder name without committing to the final internal layout.
- Decided that always-loaded files should use soft size budgets with warnings, not hard caps or principle-only guidance.
- Decided that Anthropic Contextual Retrieval should be documented as an advanced Anthropic-specific option, not a portable v1 default.
- Decided that TALL should include an explicit just-in-time memory-loading instruction: start from index/status, load only task-relevant memory files, and broaden only when retrieval fails or the task needs more context.
- Decided that memory consolidation timing should be stage-based: Reflect/batch consolidation for markdown v1, foreground checks for high-impact writes in product-grade DB or managed memory backends.
- Decided that project-local personalization should use two tiers in v1: always-loaded identity/style/workflow preferences relevant to the current project, with broader personal history loaded only when relevant.
- Decided that ambiguous memory scope should use a project-local heuristic: generally reusable preference vs project-only fact; if uncertain or sensitive, ask during Reflect. Cross-project persistence is deferred.
- Decided that stale/orphan memory cleanup should use health-check signals plus optional review windows as weak signals, never automatic expiration.
- Decided that local MCP memory servers should be included as an optional advanced v1 graduation path, not an onboarding default.
- Clarified the v1 personalization boundary: `.agent-loop` is project-local in v1, so personalization settings and taste adaptation do not automatically carry across projects. Cross-project behavior is deferred to future CLI/shared-memory work.
- Decided that when memory becomes product data, TALL should recommend Postgres first, with `pgvector` as an optional retrieval index rather than the default memory backend.
- Decided that v1 should generate private-memory ignore defaults and added `.agent-loop/memory/private/` plus `*.private.md` to this repo's `.gitignore`.
- Decided that v1 project-local personalization memories should use `scope: project` plus `kind: personalization`, rather than `scope: personal`.
- Decided that the v1 schema should reserve `scope: team` as a future value while clearly marking team/shared memory as unsupported in v1.
- Decided not to migrate current memory files into `.agent-loop` yet. Added a bridge note to `.agent-loop/README.md`: current `memory/` stays authoritative during research; future TALL project memory is expected under `.agent-loop/memory/`.
- Clarified terminology: "dogfood" means applying your own product/framework to itself, but it is jargon. Use "apply the framework to itself" or "self-application" instead.
- Updated all six Category 6 research docs with Q1-Q50 decisions, removed answered re-grill prompt sections, and corrected v1 project-local personalization drift.
- Ran housekeeping: `.tmp` contained no files to clean up, stale old-name references are only historical/superseded entries, and `BACKLOG.md` now moves Category 8 to the top of the research queue.

---

## Up Next

1. Confirm closeout and choose the next category.
2. Recommendation: Category 8 - Change Gates & Guardrails, because it directly covers the deferred Q6 thread on agent freedom, large reworks, and code cleanup.
3. Keep the framework evaluation/testing thread visible for Category 7; do not derail the next category unless the user explicitly chooses to switch.

---

## Blockers / Open Decisions

- Category 6 is complete through housekeeping. Awaiting closeout confirmation and next-category choice.
- Public name: `The Agent Learning Loop (TALL)`. Short/spoken name: `The Agent Loop`. Repo slug: `the-agent-loop`. Preferred internal folder: `.agent-loop`. Conflict check found no obvious exact-name ownership for the long form, but the component phrases are broad/common in agent architecture writing.
- Q6 from Category 2 (agent freedom vs. guardrails + code cleanup) still needs dedicated research, likely alongside Category 8.
- Category 13 (self-healing / preference learning) remains future scope.
- Cross-project personalization is deferred. V1 `.agent-loop` is project-local; future CLI/shared-memory work may allow user preferences and learned tastes to carry across projects.
- Framework evaluation/testing needs research: how to test goal pursuit, adaptability, stop-rule obedience, and signal-vs-noise discipline in Codex without creating fake confidence.

---

## Session Pickup

1. Read `AGENTS.md`.
2. Read `memory/project_framework_qa.md`.
3. Read this file for current state.
4. Read the six docs in `docs/research/category-6/`.
5. Confirm Category 6 closeout and choose the next category. Recommended: Category 8 - Change Gates & Guardrails.
