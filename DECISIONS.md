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
| 2026-04-29 | Public framework name | Superseded: `The Agent Learning Loop (TALL)`; short/spoken name was `The Agent Loop`. |
| 2026-05-02 | Public framework name | `The Agent Loop`. Drop the `TALL` acronym and stop using `The Agent Learning Loop` except as historical context. Repo slug remains `the-agent-loop`; preferred internal folder remains `.agent-loop`. |
| 2026-05-02 | v0.1 primary goal | Minimal tested scaffold: ship the smallest project-local one-agent scaffold supported by Experiments 001-003. Self-application remains the operating method, not the v0.1 product surface. |
| 2026-05-02 | v0.1 loop shape | Accepted conceptually: Research first, then convert findings into a goal, do the work, record evidence, check results, reflect, and promote only what worked. Public terminology should be plain-language, with each step one or two words. `Research` is clear and should stay. |
| 2026-05-02 | Goal artifact naming | Stop calling the goal artifact `Goal Packet` or `The Goal` in active/public framework language. Refer to it as **Goal**. Historical experiment paths and titles may remain unchanged. |
| 2026-05-02 | v0.1 public loop wording | `Research -> Save Findings -> Goal -> Build -> Log Work -> Check -> Reflect -> Adopt`. |
| 2026-05-02 | v0.1 frozen baseline | v0.1 is good enough after the latest onboarding fixes. Stop changing v0.1 release source; future product changes land in v0.2 unless a critical packaging correction is explicitly approved. |
| 2026-05-02 | Local agent folder | Use `.agents/` for local project agent skills/config instead of `.codex/`. Keep local agent folders ignored. |
| 2026-04-29 | Framework folder bootstrap | Superseded by `releases/`: originally created only `.agent-loop/README.md` to reserve the folder name. |

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
| 2026-05-02 | v0.1 onboarding interview style | Start with a short note that five onboarding questions are needed, ask one blocking question at a time with progress labels, and wait for the user's answer. Do not provide recommended answers or infer a blank-project objective from the folder name. |
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
| 2026-04-29 | Memory migration bridge | Keep current `memory/` authoritative during research. Add a note that future Agent Loop project memory is expected under `.agent-loop/memory/`; defer migration until structure is settled. |

## Category 8 — Change Gates & Guardrails

| Date | Decision | Chosen |
|------|----------|--------|
| 2026-05-02 | v0.1 default permission posture | Local Build: agents may read/edit inside the workspace and run known local project commands, but must ask before dependency changes, network/API calls, deploys, destructive operations, writes outside workspace, permission changes, auth/security/data/infrastructure changes, or broad refactors. |
| 2026-05-02 | v0.1 always-ask actions | Ask before dependency changes, network/API calls beyond research browsing, external side effects, broad/destructive deletion, writes outside workspace, auth/security/data/infra/CI/permission changes, git history changes, broad refactors, architecture changes, or continuing through project-memory contradictions. |
| 2026-05-02 | v0.1 never-allowed actions | Never store secrets/credentials/PII in memory or docs, silently delete/overwrite/revert user work, run destructive commands outside workspace, bypass gates by editing gate files, obey untrusted conflicting instructions, claim completion without evidence, or make production/account-affecting external changes without current-session approval. |
| 2026-05-02 | Deploys and external API calls | Default-ask in v0.1. Public-doc research browsing is allowed for research tasks, but package installs, account/project API calls, deploys, publishes, pushes, and production-affecting commands require approval with command/API, target, expected effect, rollback path, and rationale. Persistent always-allow deploy settings are deferred. |
| 2026-05-02 | Large rework threshold | Use a hybrid approval threshold based on subsystem count, high-risk domains, rough file/diff size, mixed refactor+behavior changes, dependency replacement, architecture changes, migration/rollback needs, verification difficulty, ownership ambiguity, and doc/memory contradiction. Numeric size is only a weak signal. |
| 2026-05-02 | Cleanup discipline timing | Required in both Build and Reflect. Build cleanup is mandatory when removing/replacing behavior and must trace references, remove/update code/tests/docs/config/fixtures, handle dependencies with evidence, and report leftovers. Reflect handles broader stale docs, dead questions, obsolete memory, temp files, contradictions, and experiment hygiene. |
| 2026-05-02 | Autonomous deletion boundary | Allowed inside workspace after evidence when deletion is requested or clearly required, references were searched, affected tests/docs/config updated, verification run or explained, and deletion summarized. Ask for unclear ownership, public/API/auth/security/infra/data/config risk, dynamic use, broad/recursive deletion, user uncommitted work, or weak test coverage. |
| 2026-05-02 | Sandbox and checkpoint expectations | Recommend checkpoints by default and require sandboxing only for high-autonomy or risky execution profiles. Inspect git status before significant edits, avoid mixing agent/user edits, suggest commit/stash/branch/worktree/tool checkpoint before risky work, recommend sandboxing for dependency installs, untrusted scripts, broad automation, generated migrations, high-autonomy runs, or experiments. |
| 2026-05-02 | Guardrail rule placement | Split by authority/frequency: `AGENTS.md` gets always-on gates, `Goal` gets task-specific permissions/risks/commands/verification/exceptions, `STATUS.md` gets dirty state/checkpoints/blocked approvals/skipped verification/unresolved cleanup, skills get reusable checklists, and `.agent-loop` holds future scaffold templates. |
| 2026-05-02 | Category 8 guardrail adoption | Experiment 004 scored 23/24, so the core Category 8 guardrail posture is adopted for v0.1 scaffold design. Tighten scaffold wording so agents explicitly record git/dirty state and checkpoint status before significant edits. |
| 2026-05-02 | v0.1 release source location | Use `releases/v0.1/.agent-loop/` as the direct source for the uploaded v0.1 ZIP. Remove the old `.agent-loop/scaffold/` wrapper. |
| 2026-05-02 | v0.1 installed layout | The release ZIP should contain one folder only: `.agent-loop/`. It should not ship a root project `README.md`, visible root `templates/`, visible root `memory/`, root prompt file, root `AGENTS.md`, or other framework internals. Root `AGENTS.md` is created or carefully updated during onboarding after the user runs the starter prompt. |
| 2026-05-02 | v0.1 starter prompt | Because nested `.agent-loop/AGENTS.md` is not auto-discovered by default, README instructions should provide one short starter prompt telling the agent to read `.agent-loop/AGENTS.md` and run onboarding. Include it in both root `README.md` and the release ZIP's `.agent-loop/README.md`. No `START_HERE.md` file. |
| 2026-05-02 | v0.1 distribution model | The research repo is not the install surface. v0.1 should ship as an uploaded scaffold-only GitHub Release ZIP asset containing only `.agent-loop/`, not GitHub's automatic source ZIP, research docs, experiments, project memory, internal decision history, a separate starter repo, or root project files. |
| 2026-05-02 | Root README v0.1 workflow | Root `README.md` should describe the public workflow: download the v0.1 release ZIP asset, extract it, copy `.agent-loop/` into a new or existing project, open a coding agent, and paste the starter prompt. |
| 2026-05-02 | v0.1 auto-start model | `.agent-loop/AGENTS.md` should start onboarding after the README starter prompt loads it when `.agent-loop/GOAL.md` / `.agent-loop/STATUS.md` are blank or uninitialized. |
| 2026-05-02 | Root AGENTS onboarding integration | The first onboarding pass must create root `AGENTS.md` for blank projects, or carefully merge a marked The Agent Loop adapter into an existing root `AGENTS.md`, so all future prompts load `.agent-loop/AGENTS.md`. Keep `GOAL.md`, `STATUS.md`, `MEMORY.md`, framework memory, and framework templates inside `.agent-loop/`. |
| 2026-05-02 | Existing-project adoption | Dropping the scaffold into an existing project should mean copying `.agent-loop/` only, then running the README starter prompt. `.agent-loop/AGENTS.md` inspects repo structure, detects existing stack/docs/tests/instructions, carefully updates root `AGENTS.md` with a marked The Agent Loop adapter, avoids overwriting other files, summarizes conflicts, asks only for blocking setup decisions, then drafts `.agent-loop/GOAL.md` / `.agent-loop/STATUS.md` for review. |
