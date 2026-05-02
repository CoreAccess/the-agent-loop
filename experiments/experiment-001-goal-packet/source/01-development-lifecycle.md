# Research: 2.4 — Development Lifecycle (Think→Plan→Build→Review→Test→Ship→Reflect)

Date: 2026-04-27
Status: Re-grill complete. Decisions recorded below.

---

## What This Sub-Category Covers

The repeating cycle that governs every feature, task, or sprint in an AI-assisted project. This is not initialization (that's 2.1-2.3) — it's the ongoing rhythm of development. It is the spine of the framework; every other category plugs into one or more of its phases.

---

## Key Findings

### 1. gstack is the most detailed existing implementation

gstack (Garry Tan / YC) has fully operationalized the Think→Plan→Build→Review→Test→Ship→Reflect cycle with 30+ specialized skills. It is the strongest reference implementation we have. Key structure:

| Phase | gstack Skills | What it produces |
|-------|-------------|-----------------|
| **Think** | `/office-hours` (6 forcing questions) | Design doc, reframed problem, alternatives with effort estimates |
| **Plan** | `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/plan-devex-review`, `/autoplan` | Architecture diagrams, test plan, failure mode matrix, design system, scoped feature plan |
| **Build** | `/design-shotgun`, `/design-html` | Feature code, UI components |
| **Review** | `/review`, `/design-review`, `/investigate`, `/codex` | Reviewed branch with auto-fixes, root cause analysis, cross-model findings |
| **Test** | `/qa`, `/qa-only`, `/benchmark`, `/canary` | Bug reports, regression tests, performance baseline, post-deploy health metrics |
| **Ship** | `/ship`, `/land-and-deploy`, `/document-release` | Merged + deployed code, updated documentation |
| **Reflect** | `/retro`, `/learn` | Retrospective summary, persistent project learnings |

**Handoff mechanism:** Each phase explicitly consumes the artifacts from the previous phase. Nothing falls through the cracks by design.

### 2. The cycle has been compressed by AI — but not eliminated

2026 SDLC research: traditional 2-week sprints → "bolts" (hours or days). AI has accelerated each phase but the phases themselves remain valid. The structure is not slower because AI is involved — it's faster because the structure prevents rework.

Key stat: AI agent teams can fit 3-5× the feature surface into the same sprint duration.

### 3. "Think" is the most underinvested phase in the ecosystem

gstack's `/office-hours` uses 6 forcing questions to challenge product assumptions BEFORE planning begins. This is the most asymmetrically valuable phase — 30 minutes of good thinking prevents days of wrong implementation.

The 6 forcing questions concept from gstack:
1. What problem are we actually solving?
2. Who specifically has this problem?
3. What alternatives exist?
4. What would make this unnecessary?
5. What are we NOT building?
6. What does success look like in 90 days?

Most developers skip Think entirely and go straight to Plan. Our framework should make Think mandatory, not optional.

### 4. "Reflect" closes the loop into memory (Category 6)

gstack's `/learn` skill manages "persistent project-specific patterns, pitfalls, and preferences." This is the bridge between the Development Lifecycle (Category 2) and Memory Systems (Category 6).

The Reflect phase should:
- Distill what was learned into the memory system (episodic → semantic, per Databricks)
- Update planning docs (STATUS, DECISIONS) with what changed
- Flag patterns that should be promoted to AGENTS.md conventions
- Feed performance baselines back into the testing baseline (Category 7)

Without Reflect, the cycle is open-loop. With it, each iteration makes the next one better.

### 5. Harness engineering: "structure in, structure out"

Red Hat (2026): the quality of AI output is determined by the quality of the environment (harness), not just the prompt. Applied to the development lifecycle:

- **Think:** Structure the problem before asking the AI anything
- **Plan:** Ground the plan in actual codebase (LSP/MCP repo impact map for brownfield)
- **Build:** Implement against a structured spec, not a vague prompt
- **Review:** Use structured review criteria, not "looks good to me"
- **Test:** Defined acceptance criteria and stopping rules
- **Ship:** Checklist-driven, not feel-based
- **Reflect:** Structured retrospective format, not freeform notes

Each phase needs its own "harness" — a structured template or skill that constrains inputs and produces predictable outputs.

### 6. Tests are created during Build, not after

2026 AI SDLC research: "AI agents create unit tests, integration tests, and edge case scenarios at the same time development begins rather than after it completes." This is a fundamental shift from traditional TDD — AI can hold both implementation and test in context simultaneously.

Implication for our framework: the Build phase includes test scaffolding, not just implementation. Test→Ship becomes validation, not creation.

### 7. Category connections — the lifecycle touches everything

| Phase | Primary Categories | Secondary Categories |
|-------|-------------------|---------------------|
| Think | 4 (Spec-Driven Dev) | 2.2 (Constitution), 9 (Context Loading) |
| Plan | 4 (Spec), 3 (Planning Docs) | 9 (Context Loading), 11 (Agentic Patterns) |
| Build | 9 (Context Loading) | 1 (Agent Contract), 8 (Change Gates) |
| Review | 8 (Change Gates) | 12 (Observable Dev), 10 (Error Handling) |
| Test | 7 (Testing & Verification) | 12 (Observable Dev) |
| Ship | 7 (Testing), 3 (Planning Docs) | 8 (Change Gates) |
| Reflect | 6 (Memory) | 3 (Planning Docs), 12 (Observable Dev) |

This is why the lifecycle is the spine — it orchestrates every other category.

### 8. The developer role has shifted to "orchestrator"

2026 research consensus: developers are no longer writers of code — they are orchestrators of AI systems. The lifecycle framework's job is to make orchestration systematic, not improvisational.

gstack's `/autoplan` embodies this: run CEO→design→eng→DX reviews automatically, surface only taste decisions for human approval. The human approves; the AI executes.

---

## Proposed Phase-by-Phase Framework Structure

For each phase, our framework should define:
1. **Entry criteria** — what must be true before this phase starts
2. **Skill(s)** — what skill(s) support this phase
3. **Human touchpoint** — where human input is required
4. **Output artifact** — what this phase produces
5. **Exit criteria** — what must be true before the next phase starts

### Think
- Entry: A task or feature has been identified
- Skills: `think` / `office-hours` equivalent
- Human touchpoint: Approve the reframed problem and chosen approach
- Output: Design doc with problem statement, approach, alternatives, estimates
- Exit: Human has approved the design doc

### Plan
- Entry: Approved design doc
- Skills: `plan` (architecture + task breakdown)
- Human touchpoint: Review architecture and task list
- Output: Architecture notes, ordered task list, test plan skeleton
- Exit: Human has approved the plan

### Build
- Entry: Approved plan
- Skills: `build` (implementation) — agent works from plan, not from memory
- Human touchpoint: Async review of progress; flag blockers
- Output: Implementation code + test scaffolding
- Exit: Code complete per plan, tests written
- **Cleanup mandate:** When removing a feature, agent must trace and remove all code attached to that feature unless it is referenced elsewhere. Dead code is not acceptable. Agents default to adding — this rule counteracts that bias.

### Review
- Entry: Code complete
- Skills: `review` (code review), `security-review` (if touching auth/data)
- Human touchpoint: Review flagged issues, approve fixes
- Output: Reviewed branch with issues resolved
- Exit: Review checklist passed

### Test
- Entry: Reviewed branch
- Skills: `qa` (browser/integration testing)
- Human touchpoint: Review failed tests, approve fix plan
- Output: All tests passing, regressions covered
- Exit: Acceptance criteria met

### Ship
- Entry: Tests passing
- Skills: `ship` (deploy + verify)
- Human touchpoint: Approve deployment, verify production
- Output: Feature live in production, docs updated
- Exit: Production health confirmed

### Reflect
- Entry: Feature shipped
- Skills: `reflect` (retrospective + learning distillation)
- Human touchpoint: Agent drafts a short list of candidate memories. Human reviews and approves, edits, or rejects each one. Nothing is written to memory until approved.
- Output: Approved learnings written to memory, planning docs updated, patterns captured
- Exit: Learnings saved, memory distilled
- **Preference learning:** What the human approves, edits, and rejects in each Reflect session shapes future drafts. Over time the agent builds a picture of how this specific human likes to work.

---

## Patterns to Borrow

| Pattern | Source | What to Take |
|---------|--------|-------------|
| 7-phase cycle with explicit handoffs | gstack | Adopt exactly — the handoff mechanism is the key |
| 6 forcing questions in Think | gstack `/office-hours` | Adapt for our `think` skill |
| Harness per phase | Red Hat harness engineering | Each phase needs a structured template |
| Tests created during Build | 2026 SDLC research | Build skill includes test scaffolding |
| `/learn` for persistent patterns | gstack | Reflect phase bridges to Category 6 (Memory) |
| `/autoplan` for automated phase sequence | gstack | Advanced feature for v2 |
| Artifacts consumed by next phase | gstack | Explicit handoff format between phases |

---

## Re-Grill Decisions

- **Phase depth scales to the task:** All 7 phases are always present — no phases are skipped, even for a bug fix. A bug fix Think phase might be one sentence. Consistency and safety over convenience.
- **Mid-phase interruption:** At session end, agent writes: (1) STATUS.md handoff note — what phase, what's done, what's next, open decisions; (2) phase checklist — items ticked as complete. Next session reads both and resumes from the last unchecked item.
- **Reflect memory distillation:** Agent drafts candidate memories; human reviews and approves/edits/rejects before anything is written. No automatic persistence. Human approval is the filter.
- **Self-healing / error pattern tracking (flagged — do not scope into v1):** Agent should track tool calls and approaches that repeatedly fail before succeeding with a different method. Over time, stop defaulting to failing patterns. Potential Category 13. Research needed before scoping.

## Questions Remaining for Deep Research

- What does a minimal viable `think` skill look like? (6 questions is gstack's implementation — what's ours?)
- How do skills for Claude Code differ from skills for Gemini/Codex in each phase?

---

## Sources

- [gstack — full sprint cycle breakdown](https://github.com/garrytan/gstack)
- [Red Hat harness engineering](https://developers.redhat.com/articles/2026/04/07/harness-engineering-structured-workflows-ai-assisted-development)
- [SDLC Is Dead — AI SDLC 2026](https://www.groovyweb.co/blog/sdlc-ai-era-software-development-2026)
- [AI-Driven Development Life Cycle — AWS](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
- [Microsoft AI-led SDLC](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896)
- [BMAD method](https://reenbit.com/the-bmad-method-how-structured-ai-agents-turn-vibe-coding-into-production-ready-software/)
- [Harness engineering arxiv](https://arxiv.org/html/2603.05344v1)
