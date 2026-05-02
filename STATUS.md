# Project Status

Last updated: 2026-05-02

---

## Where We Are

**Phase:** v0.1 frozen; v0.2 planning next
**Active category:** None; Category 8 - Change Gates & Guardrails is complete.  
**Cycle step:** v0.1 is accepted as good enough and should no longer receive product changes. Future scaffold/product changes should land in v0.2.

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
| 8 - Change Gates & Guardrails | Done | Done | Done | Done |
| 9 - Context Loading & Management | Done | Pending | Pending | Pending |
| 10 - Error Handling & Recovery | Done | Pending | Pending | Pending |
| 11 - Agentic Patterns | Done | Pending | Pending | Pending |
| 12 - Observable Development | Done | Pending | Pending | Pending |

---

## Completed In This Pickup

- Reviewed user-provided Experiment 005 launch-test output in `experiments/experiment-005-v01-launch-test-results/`.
- Opened `agent-response.png`; actor reported updating only `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md`.
- Compared `agent-loop-results/` against `releases/v0.1/.agent-loop/`; only `GOAL.md` and `STATUS.md` differ.
- Inspected `releases/v0.1/v0.1.zip`; archive root contains only `.agent-loop/`, matching the intended release package shape.
- Created `experiments/experiment-005-v01-launch-test-results/evaluation/evaluator-review.md`.
- Experiment 005 result: 12/21 partial pass after root-adapter clarification. ZIP/package fidelity and cautious change discipline passed; blank-project onboarding failed to create root `AGENTS.md` and failed to ask for the actual project objective before drafting a generic onboarding Goal.
- Root `AGENTS.md` finding: user clarified the desired v0.1 behavior. The ZIP should still contain only `.agent-loop/`, but onboarding must create root `AGENTS.md` for blank projects or carefully merge a marked adapter into existing root `AGENTS.md`; otherwise future prompts will not load the framework.
- Updated `releases/v0.1/.agent-loop/AGENTS.md` so onboarding creates/updates root `AGENTS.md`, asks blank-project blocking questions before drafting Goal/Status, and keeps framework working files inside `.agent-loop/`.
- Updated root `README.md` starter prompt to require root `AGENTS.md` creation/merge before Goal drafting.
- Updated `releases/v0.1/.agent-loop/README.md`, `GOAL.md`, `STATUS.md`, and `templates/reflect-checklist.md` to reflect root adapter onboarding.
- Rebuilt `releases/v0.1/v0.1.zip` from the updated release source using `tar -a -cf` so archive entries use portable `.agent-loop/...` paths.
- Static ZIP validation passed: all archive entries are under `.agent-loop/`; no root `AGENTS.md` is shipped; archived `.agent-loop/AGENTS.md` contains root adapter markers plus blank-project and existing-project rules.
- Created `experiments/experiment-006-v01-root-agents-retest/` with a blank-project and existing-project retest matrix, run prompt, and evaluation rubric.
- Evaluated the user-provided Experiment 006 blank-project rerun in `experiments/experiment-006-v01-root-agents-retest/results/`.
- Result: blank-project retest is a partial pass. Root `AGENTS.md` was created correctly and `.agent-loop/` scaffold files were unchanged, but the actor asked all five onboarding questions at once without recommendations.
- Created `experiments/experiment-006-v01-root-agents-retest/evaluation/evaluator-review.md`.
- Initially adopted a one-question onboarding refinement with recommendations; this was superseded after the next rerun showed blank-project recommendations were poorly grounded.
- Updated `releases/v0.1/.agent-loop/AGENTS.md`, root `README.md`, Experiment 006 `RUN_PROMPT.md`, and the Experiment 006 rubric with the one-question interview rule.
- Rebuilt `releases/v0.1/v0.1.zip` again and validated that archived `.agent-loop/AGENTS.md` contains both the root adapter rules and the one-question onboarding rule.
- Reviewed another Experiment 006 rerun screenshot. The actor now created root `AGENTS.md`, asked only Question 1 of 5, and waited before drafting Goal/Status, but it still dumped too much repo state and suggested a blank-project objective from the folder name.
- Refined the v0.1 onboarding style again: no full repo inspection dump in the first response, no recommended answers for onboarding questions, and never infer/suggest a blank-project objective from the folder name.
- Updated `releases/v0.1/.agent-loop/AGENTS.md`, root `README.md`, Experiment 006 `RUN_PROMPT.md`, rubric, and evaluator review to reflect the concise five-question onboarding style.
- Rebuilt `releases/v0.1/v0.1.zip` and validated that archived `.agent-loop/AGENTS.md` contains the no-dump, no-recommendation, no-folder-objective, and `Question 1 of 5` rules.
- Added the full starter prompt to `releases/v0.1/.agent-loop/README.md` so the downloaded ZIP is self-contained without adding a separate `START_HERE.md` or root prompt file.
- User accepted the current v0.1 state as good enough for v0.1 and asked to stop changing it.
- Decided all future scaffold/product changes now land on v0.2. Do not edit `releases/v0.1/.agent-loop/` or `releases/v0.1/v0.1.zip` unless the user explicitly approves a critical v0.1 packaging correction.
- Confirmed Category 8 - Change Gates & Guardrails as the next active research category.
- Reviewed Search Engine Land's May 1, 2026 article "How to build SEO agent skills that actually work" and flagged it as a future Category 5 source with Category 8 overlap.
- Completed first-pass Category 8 deep research and created an index plus five research docs:
  - `docs/research/category-8/README.md`
  - `docs/research/category-8/1-permission-models-and-autonomy.md`
  - `docs/research/category-8/2-high-impact-actions-and-stop-rules.md`
  - `docs/research/category-8/3-change-size-refactors-and-cleanup.md`
  - `docs/research/category-8/4-sandboxing-rollback-and-external-access.md`
  - `docs/research/category-8/5-developer-pain-and-reference-implementations.md`
- Completed Category 8 re-grill Q1-Q9.
- Updated Category 8 docs with re-grill decisions and removed answered question framing.
- Created `experiments/experiment-004-guardrail-realistic-edit/`.
- Experiment 004 tests a realistic local Python project edit with Local Build autonomy, cleanup/deletion discipline, stop rules, checkpoint/sandbox expectations, verification, and Reflect.
- Seed baseline tests pass: `uv run python -m unittest discover -s tests` from the experiment `project/` ran 4 tests successfully.
- Evaluated returned Experiment 004 actor run and wrote `experiments/experiment-004-guardrail-realistic-edit/evaluation/evaluator-review.md`.
- Experiment 004 result: 23/24 strong pass. Only material deduction: actor did not explicitly record a git status/checkpoint check before editing.
- Independent verification passed: `uv run python -m unittest discover -s tests` from the experiment `project/` ran 4 tests successfully.
- User approved cleanup of generated Experiment 004 `__pycache__/` files; removed them after verifying resolved paths were inside the workspace.
- Added `docs/research/category-8/6-v0.1-guardrail-adoption.md`.
- Adopted Category 8 guardrails for v0.1 scaffold design, with tightened wording requiring actors to record git/dirty state and checkpoint status before significant edits.
- Created `.agent-loop/scaffold/v0.1/` as the first product-shaped v0.1 scaffold draft.
- Added source templates for `AGENTS.md`, `STATUS.md`, `GOAL.md`, `MEMORY.md`, `memory/active/`, `memory/proposed/`, `memory/log.md`, `memory/decisions.md`, `templates/atomic-memory.md`, `templates/goal.md`, and `templates/reflect-checklist.md`.
- Updated `.agent-loop/README.md` to point to the v0.1 scaffold draft.
- Decided the current research repo should not be the user install surface.
- Refined distribution direction: use a scaffold-only release ZIP for v0.1; do not create a separate starter repo for now.
- Removed `.agent-loop/scaffold/v0.1/templates/START_HERE.md`; startup must not depend on an installed prompt file.
- Refined startup model: the GitHub README starter prompt loads `.agent-loop/AGENTS.md`, which starts onboarding when `.agent-loop/GOAL.md` / `.agent-loop/STATUS.md` are blank or uninitialized.
- Strengthened existing-project adoption behavior: inspect repo first, detect existing stack/docs/tests/instructions, avoid overwrites, summarize conflicts, ask only blocking setup questions, then draft `GOAL.md` / `STATUS.md` for review.
- Reworked the v0.1 scaffold source so installed framework internals live under project `.agent-loop/`, not root `memory/`, root `templates/`, or root framework docs.
- Refined the release model again: v0.1 ZIP should contain only `.agent-loop/`.
- Removed root adapter source files from the v0.1 release-source draft.
- Decided the GitHub README should provide the starter prompt that tells the agent to read `.agent-loop/AGENTS.md`; no `START_HERE.md`, prompt file, root `README.md`, or root `AGENTS.md` should be installed by default.
- Clarified that users should download an uploaded GitHub Release asset, not GitHub's automatic source-code ZIP.
- Decided the scaffold should not install a root project `README.md`, because existing projects almost certainly already own that file.
- Moved the v0.1 release package source from `.agent-loop/scaffold/v0.1/release-source/core/.agent-loop/` to `releases/v0.1/.agent-loop/`.
- Removed the obsolete root `.agent-loop/` scaffold wrapper.
- Updated root `README.md` to describe the public v0.1 workflow: download the GitHub Release ZIP asset, extract it, copy `.agent-loop/` into a new or existing project, open a coding agent, and run the starter prompt.
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
- Historical naming note: previously chose `The Agent Learning Loop (TALL)`, short name `The Agent Loop`, repo slug `the-agent-loop`, preferred internal folder `.agent-loop`. Superseded on 2026-05-02 by public name `The Agent Loop`.
- Added root `README.md` and `.gitignore` to start the repository identity and hygiene.
- Ran a stale-path check for `AgentProjectFoundation`; no active stale paths were found. Remaining old-name references are historical/superseded decision-log entries.
- Created `.agent-loop/README.md` as a placeholder to reserve the framework folder name without committing to the final internal layout.
- Decided that always-loaded files should use soft size budgets with warnings, not hard caps or principle-only guidance.
- Decided that Anthropic Contextual Retrieval should be documented as an advanced Anthropic-specific option, not a portable v1 default.
- Decided that The Agent Loop should include an explicit just-in-time memory-loading instruction: start from index/status, load only task-relevant memory files, and broaden only when retrieval fails or the task needs more context.
- Decided that memory consolidation timing should be stage-based: Reflect/batch consolidation for markdown v1, foreground checks for high-impact writes in product-grade DB or managed memory backends.
- Decided that project-local personalization should use two tiers in v1: always-loaded identity/style/workflow preferences relevant to the current project, with broader personal history loaded only when relevant.
- Decided that ambiguous memory scope should use a project-local heuristic: generally reusable preference vs project-only fact; if uncertain or sensitive, ask during Reflect. Cross-project persistence is deferred.
- Decided that stale/orphan memory cleanup should use health-check signals plus optional review windows as weak signals, never automatic expiration.
- Decided that local MCP memory servers should be included as an optional advanced v1 graduation path, not an onboarding default.
- Clarified the v1 personalization boundary: `.agent-loop` is project-local in v1, so personalization settings and taste adaptation do not automatically carry across projects. Cross-project behavior is deferred to future CLI/shared-memory work.
- Decided that when memory becomes product data, The Agent Loop should recommend Postgres first, with `pgvector` as an optional retrieval index rather than the default memory backend.
- Decided that v1 should generate private-memory ignore defaults and added `.agent-loop/memory/private/` plus `*.private.md` to this repo's `.gitignore`.
- Decided that v1 project-local personalization memories should use `scope: project` plus `kind: personalization`, rather than `scope: personal`.
- Decided that the v1 schema should reserve `scope: team` as a future value while clearly marking team/shared memory as unsupported in v1.
- Decided not to migrate current memory files into `.agent-loop` yet. Added a bridge note to `.agent-loop/README.md`: current `memory/` stays authoritative during research; future Agent Loop project memory is expected under `.agent-loop/memory/`.
- Clarified terminology: "dogfood" means applying your own product/framework to itself, but it is jargon. Use "apply the framework to itself" or "self-application" instead.
- Updated all six Category 6 research docs with Q1-Q50 decisions, removed answered re-grill prompt sections, and corrected v1 project-local personalization drift.
- Ran housekeeping: `.tmp` contained no files to clean up, stale old-name references are only historical/superseded entries, and `BACKLOG.md` now moves Category 8 to the top of the research queue.
- Created the initial local git commit and pushed `main` to `https://github.com/CoreAccess/the-agent-loop.git`.
- Closed the session for the night. Next pickup should start by confirming Category 8 or choosing a different next category.
- Captured an out-of-cycle video research note from Brendan O'Leary's "Agentic Engineering" talk: `docs/research/agentic-engineering-brendan-oleary.md`. Treat it as supporting evidence only, not a core source of truth. The local root transcript was distilled into the note and removed during cleanup.
- Removed local ignored root files `AGENTS-SAMPLE.md` and `transcript.md`; `.gitignore` keeps both ignored so they do not return accidentally.
- Updated `AGENTS.md` so it no longer requires or lists `AGENTS-SAMPLE.md`.
- Updated active terminology from `The Goal` to `Goal` and kept historical experiment titles/paths intact.
- Deleted local `.claude/` and `.tmp/`.
- Copied local project agent skill config from `.codex/` to `.agents/`; `.agents/skills/grill-me/` now exists.
- Could not remove `.codex/` during this session because Windows reports access denied on files currently locked by Codex. User said they will delete `.codex/` manually before restart.
- Updated `.gitignore` to ignore `.agents/*` while keeping `.claude/*` and `.codex/*` ignored as safeguards.

---

## Up Next

1. Start v0.2 planning from the known v0.1 lessons: root `AGENTS.md` adapter, concise five-question onboarding, existing-project merge behavior, and self-contained scaffold README.
2. Decide the first v0.2 validation target: existing-project onboarding, guided onboarding UX, or broader framework evaluation.
3. Keep `releases/v0.1/` frozen as the baseline artifact.

---

## Blockers / Open Decisions

- Category 6 and Category 8 are complete and closed out.
- GitHub remote is configured as `origin`; `main` tracks `origin/main`.
- Public name: `The Agent Loop`. Drop `The Agent Learning Loop` and `TALL` except as historical context. Repo slug: `the-agent-loop`. Preferred internal folder: `.agent-loop`.
- v0.1 primary goal: minimal tested project-local one-agent scaffold supported by Experiments 001-003. Self-application is the operating method, not the v0.1 product surface.
- v0.1 public loop wording: `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`.
- Goal artifact naming: use **Goal** in active/public framework language, not `Goal Packet` or `The Goal`. Historical experiment paths and titles may remain unchanged.
- v0.1 is frozen as the baseline artifact. Future scaffold/product changes land on v0.2.
- Local agent folder convention: use `.agents/` for project-local agent skills/config. Restart check confirmed `.codex/`, `.claude/`, and `.tmp/` are absent; `.agents/` exists and remains ignored.
- Category 2 Q6 agent freedom / guardrails / cleanup was resolved through Category 8 research and Experiment 004, then promoted into the v0.1 scaffold.
- Category 13 (self-healing / preference learning) remains future scope.
- Cross-project personalization is deferred. V1 `.agent-loop` is project-local; future CLI/shared-memory work may allow user preferences and learned tastes to carry across projects.
- Framework evaluation/testing needs research: how to test goal pursuit, adaptability, stop-rule obedience, and signal-vs-noise discipline in Codex without creating fake confidence.
- Experiment 004 passed with one caveat that has been converted into scaffold wording: record git/dirty state and checkpoint status before significant edits.
- Experiment 005 found a v0.1 onboarding gap: scaffold-only blank projects need root `AGENTS.md` creation, a blocking-question path before Goal drafting, and existing projects need careful root `AGENTS.md` merge behavior.
- Experiment 006 blank-project reruns showed the root adapter fix works at a basic level; remaining gap is guided onboarding quality, now refined to concise five-question framing with no recommendations and no folder-name objective inference.

---

## Session Pickup

1. Read `AGENTS.md`.
2. Read `memory/project_framework_qa.md`.
3. Read this file for current state.
4. Read `docs/case-studies/cms-incubator.md`.
5. Read `experiments/experiment-003-behavioral-obedience/evaluation/evaluator-review.md`.
6. Continue defining The Agent Loop v0.1 Goal one decision at a time.

## CMS Incubator Migration - 2026-05-02

Curated artifacts from the separate `CMS` incubator workspace were migrated into this repo.

Added:

- `experiments/experiment-001-goal-packet/`
- `experiments/experiment-002-memory-scaffold/`
- `experiments/experiment-003-behavioral-obedience/`
- `docs/case-studies/cms-incubator.md`

Summary:

- The CMS / website-factory idea is deferred as a future applied vertical.
- The Agent Loop is now the focused project.
- Experiments 001-3 each passed with independent score 20/21.
- The main unresolved caveat is precise unsafe-memory testing; future fixtures should use redacted placeholders and keep unsafe strings only in task prompts.
- Research should remain an explicit phase before major framework rules are promoted.

Recommended pickup:

1. Read `docs/case-studies/cms-incubator.md`.
2. Read `experiments/experiment-003-behavioral-obedience/evaluation/evaluator-review.md`.
3. Read `experiments/experiment-004-guardrail-realistic-edit/README.md`.
4. Read `experiments/experiment-004-guardrail-realistic-edit/evaluation/evaluator-review.md`.
5. Read `docs/research/category-8/6-v0.1-guardrail-adoption.md`.
6. Review `releases/v0.1/.agent-loop/`.
7. Create scaffold validation experiments for blank-project and existing-project adoption.
