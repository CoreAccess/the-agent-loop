# AGENTS.md — AI Framework Research & Build Project

This project is building an advanced framework for AI-assisted software development. It is both a product and a living research project. The framework will include a template repository, a human-in-the-loop onboarding skill, Mintlify documentation, and skills ported to Claude Code, Gemini, and Codex/ChatGPT.

## 1. Authority and Scope

Priority order when instructions conflict:

1. Explicit user request in the current chat.
2. This AGENTS.md file.
3. Memory files (see Section 2 for path).

## 2. Context Loading

At the start of every session:

1. Read this AGENTS.md.
2. Read `STATUS.md` — current project state and what to do next.
3. Read `memory\project_framework_qa.md` — full decision record and session log.
4. Read `BACKLOG.md` — open questions relevant to the next task.

## 3. Memory Discipline — Critical

**Save to memory at every natural breakpoint.** Do not wait for the user to ask.

Natural breakpoints include:
- A significant decision has been made (Q&A answer confirmed)
- A research finding changes or validates a category
- The conversation has gone 8-10+ exchanges without a save
- The user signals the session is winding down
- Before switching to a new sub-task

When saving:
- Update `project_framework_qa.md` — append to the Decisions Log and Session Log
- Update `MEMORY.md` index if new memory files are created
- Use this format for decision entries:

```
### [Topic] (decided YYYY-MM-DD)
- Key decision and rationale
- Open questions if any remain
```

**Why this matters:** This project spans many sessions. LLM context compaction will erase conversation history. Memory files are the only durable record of what was decided and why.

## 4. Current Phase

**Phase: The Agent Loop v0.1 Goal and filesystem organization**

**What's been completed:**
- Broad sweep research: all 12 links → `docs/research/broad-sweep.md`
- Category 2 sub-category research: `docs/research/category-2/` (4 docs)
- Category 2 re-grill: all Q1-Q9 answered, research docs updated, housekeeping done
- Category 6 Memory Systems deep research, re-grill, docs update, and housekeeping
- CMS incubator artifacts migrated into `experiments/` and `docs/case-studies/`
- Public name simplified to `The Agent Loop`
- v0.1 public loop wording decided: `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`

**Immediate next action:**
- Review filesystem organization, naming conventions, and scaling hygiene before choosing the next research or experiment task.
- Note: Q6 (agent freedom + code cleanup) still needs dedicated research alongside Category 8 (Change Gates)

## 5. Categories (v2 — post broad-sweep research)

1. Agent Contract
2. Project Bootstrap & Onboarding *(sub-category: Development Lifecycle — Think→Plan→Build→Review→Test→Ship→Reflect)*
3. Planning & Architecture Docs
4. Spec-Driven Development *(spec-kit is research inspiration, not integration target)*
5. Skills & Reusable Capabilities
6. Memory Systems
7. Testing & Verification Loops
8. Change Gates & Guardrails *(separate from Category 1 by design)*
9. Context Loading & Management
10. Error Handling & Recovery
11. Agentic Patterns *(multi-agent is v2)*
12. Observable Development *(proactive visibility during active work — distinct from reactive Error Handling)*

## 6. Planned Project Structure

```
/
├── AGENTS.md                        # This file - behavior contract + process
├── STATUS.md                        # Current project state + session pickup
├── DECISIONS.md                     # Key decisions log (quick reference)
├── BACKLOG.md                       # Open questions + future work
├── README.md                        # Public project overview
├── .agent-loop/                     # Future framework install folder
├── .agents/                         # Local agent skills/config, ignored
├── memory/
│   ├── MEMORY.md                    # Memory index
│   ├── project_framework_qa.md      # Full decision narrative + session log
│   └── user_profile.md              # User working style
├── docs/
│   ├── case-studies/                # Applied lessons from experiments/incubators
│   └── research/                    # Research notes per category
└── experiments/                     # Isolated experiment capsules
```

## 7. Change Gates

Always do:
- Save decisions to memory at natural breakpoints.
- Back decisions with research or evidence before finalizing.
- Update `MEMORY.md` when new memory files are created.
- Keep `project_framework_qa.md` as the authoritative decision record.
- Treat housekeeping as first-class work: remove temp files once they've served their purpose, keep docs in sync with decisions, flag stale content during Reflect. When suggesting cleanup, note it and ask — never delete silently.

Ask first:
- Changing the category list after research validates it.
- Creating new top-level directories or structural changes.
- Adding skills or templates (these come after research is done).

Never do:
- Make permanent architectural decisions without research backing.
- Overwrite or delete memory files without explicit user approval.
- Skip the shared vision / grilling process when starting a new major sub-task.
- Treat this AGENTS.md as frozen — update it as the project evolves.

## 8. Target Audience (design priority)

Design for **B first**: experienced AI-assisted developers who are sharp critics and best validators.
Serve A (personal use), B (experienced devs), C (broader community via Mintlify docs).

## 9. Research Cycle Checklist

Each category follows this repeating cycle. Tick each step before moving to the next.

**Step 1 — Choose category**
- [ ] Confirm with user which category to research next
- [ ] Update STATUS.md with active category and cycle step

**Step 2 — Deep research**
- [ ] Identify 3-5 targeted sources for this category
- [ ] Search Reddit, developer forums, Discord servers, GitHub discussions, and any other spaces where developers are active — real pain points and frustrations reveal what actually breaks in practice, not what authors want to be true
- [ ] Actively discover new communities and sources as research progresses — add them to the research pool, don't rely on a fixed list
- [ ] Search GitHub for reference implementations, how other developers are solving the same problems, and what patterns are emerging in the wild
- [ ] When a question feels genuinely hard, look beyond software — human psychology, philosophy, ethics, cognitive science, the scientific method, and organizational theory have all solved analogous problems. Mine them. (Full list in `memory/project_framework_qa.md` → Cross-Discipline Research)
- [ ] Write sub-category docs in `docs/research/category-N/`
- [ ] Note patterns to borrow and questions remaining per doc

**Step 3 — Re-grill**
- [ ] Prepare questions based on research findings
- [ ] Work through Q&A with user one question at a time
- [ ] Save all decisions to `memory/project_framework_qa.md` as they are confirmed

**Step 4 — Update docs**
- [ ] Update sub-category docs with re-grill decisions
- [ ] Remove answered questions from "Questions Remaining" sections
- [ ] Confirm no drift or duplication across docs

**Step 5 — Housekeeping**
- [ ] Check for temp files or stale content to remove
- [ ] Update DECISIONS.md with new decisions
- [ ] Update BACKLOG.md — remove answered questions, add new ones
- [ ] Update STATUS.md — mark cycle complete, set up next

**Step 6 — Session log**
- [ ] Add entry to Session Log in `memory/project_framework_qa.md`
- [ ] Confirm user is satisfied before closing
