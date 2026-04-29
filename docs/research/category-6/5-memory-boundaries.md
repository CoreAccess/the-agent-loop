# Sub-Category 6.5 — Memory Boundaries

Date: 2026-04-28
Phase: Category 6 deep research, sub-category 5 of 6
Status: Re-grill complete; decisions applied

---

## Why this sub-category exists

Sub-category 1 introduced the scope axis (personal / project / team) but only at vocabulary level. This sub-category answers the practical questions:

- Does the user's profile follow them across projects, or live inside each one?
- When project memory holds preferences, are they project-specific or user-wide?
- What about a future where teams adopt the framework — how do shared memories interact with private ones?
- Where do secrets and PII live, and what stays out of memory entirely?

Boundaries are mostly an organizational concern — they don't change the technical architecture as much as they change *which file lives where* and *who can read it*. But they shape every other sub-category once they're set, which is why they need a deliberate decision rather than a default.

---

## The three scopes (recap from sub-category 1, expanded)

| Scope | Belongs to | Lives where (file pattern) | Examples |
|-------|-----------|----------------------------|----------|
| **Personal** | One user | User's home dir or central memory store | "Prefers terse responses," "uses Go primarily," "is a senior dev" |
| **Project** | One project / repo | Inside the repo (committed) | Architecture decisions, planning docs, project-specific conventions |
| **Team / Shared** | A group | Shared infra (DB, central repo, MCP server) | Team naming conventions, internal SOPs, business glossary |

The framework's audience starts solo. Most users are one developer working on one or several projects. Personal + project scope is the dominant case. Team scope matters once orgs adopt the framework; v2 territory but worth designing the boundary so it's not painful to add later.

---

## The dominant boundary question — does user identity follow across projects?

Two patterns in the field:

### Pattern A — Project-scoped only, no cross-project user memory

**How it works:** All memory lives inside the project repo. Open a new project → start fresh. User profile is recreated per project (or skipped).

**Used by:** Most file-based agent frameworks today (gstack, default Claude Code patterns when the user doesn't move `~/.claude/memory/` content around).

**Pro:** Simple. Memory travels with the code (clone the repo, get the memory). No leakage between projects. Zero infra.

**Con:** User has to re-teach the agent their preferences for every project. "I prefer terse code reviews" — say it once per project, forever.

### Pattern B — User identity persists across projects

**How it works:** Personal memory lives in a user-scoped store (`~/.claude/memory/` or equivalent). Project memory lives in the repo. Agent loads both at session start. This is the pattern used by **this very project** — the auto-memory writes to `C:\Users\adamd\.claude\projects\...\memory\` which is user-scoped.

**Used by:** Claude Code auto-memory (split: per-project memory dir under `~/.claude`), Cursor's memory feature, ChatGPT memory.

**Pro:** "Tell the agent once, it remembers everywhere." User profile is portable.

**Con:** Cross-project leakage risk — project A's preferences may not apply to project B. Memory becomes a soup if not carefully scoped within the personal store.

### What real systems do

- **Claude Code auto-memory** (the current project's setup): Memory is **per-project** inside the user's home directory — `~/.claude/projects/<project-hash>/memory/`. Project-scoped storage, but in a user-scoped location. So personal observations about "this project" stay tied to this project, but they live in user space (not in the repo). A second project gets a different memory dir.
- **mem0**: Supports both `user_id` and `agent_id` as separate scopes; same memory layer can hold both.
- **Squad**: Memory lives in `.squad/` folder **inside the repo**, versioned with the code. Pure project-scoping. "When you clone a repo, you get an already onboarded AI team."
- **Memorix**: MCP-based shared project memory across multiple agents (Cursor, Claude Code, Windsurf). Project-scoped, agent-shared.
- **CrewAI**: Three memory types (short-term, long-term, entity). All agent-scoped.

### The split Claude Code already makes

Claude Code's auto-memory pattern is a clean lesson. It splits cleanly along **content type**, not just scope:

- `user_profile.md` — user-level facts about the human ("experienced developer, evidence-driven, prefers cycles")
- `feedback_*.md` — guidance about how to work ("plain language first")
- `project_*.md` — facts about *this* project ("AI Framework Project — Core Decisions")
- `reference_*.md` — pointers to external systems

The first two travel with the user *intent* but currently live per-project — meaning a thoughtful user has to copy them to new projects. The framework should improve on this: user-level memory should genuinely be user-scoped, not duplicated per project.

---

## Where memories should live (file location, not just type)

Combining scope with the file-role axis from sub-category 1:

| File / pattern | Scope | Lives where | Versioned with code? |
|---------------|-------|-------------|---------------------|
| `~/.claude/memory/user_profile.md` (or equivalent) | Personal | User home | No — personal |
| `~/.claude/memory/feedback_*.md` | Personal | User home | No |
| `<repo>/AGENTS.md` | Project | Repo root | Yes |
| `<repo>/MEMORY.md` (index) | Project | Repo root | Yes |
| `<repo>/memory/project_*.md` | Project | Repo memory dir | Yes |
| `<repo>/memory/decisions.md` | Project | Repo memory dir | Yes |
| `<repo>/STATUS.md` | Project (this session) | Repo root | Yes |
| Team store (DB or central repo) | Team | External | Versioned externally |

**The version-control split is the most consequential**: anything in the repo gets git history for free; anything in user space does not. For solo devs this is fine; for teams, it pushes the question of "do we have a shared memory" into the open.

This project currently breaks the recommended split — its `MEMORY.md` and memory files live in user space (`~/.claude/projects/...`), not in the repo. That was fine for early scaffolding but should change when the framework codifies its own structure.

---

## Cross-project user memory — practical structure

If the framework recommends Pattern B (user identity persists), we need rules for what's user-scoped vs project-scoped. Proposal:

**User-scoped (personal):**
- Identity facts: role, experience level, tools used most
- Communication preferences: terse/verbose, formal/casual, plain language
- Workflow preferences: cycles vs big-bang, review style, autonomy comfort

**Project-scoped:**
- Architecture decisions, tech stack choices
- Project-specific conventions
- People, deadlines, business context for this project
- Anything that depends on the project's domain

**Ambiguous (the hard ones):**
- "User prefers Go" — usually personal, but if the project is React-only, irrelevant
- "User wants 80%+ test coverage" — usually personal preference, but enforced project-wide
- "Don't refactor without asking" — usually project policy but might be a personal style across projects

**Resolution heuristic:** If the rule applies regardless of which project the user is in, it's personal. If it only applies to *this* project, it's project. When in doubt, the agent asks during Reflect.

---

## Privacy, security, and PII

Two concrete issues, both flagged by mem0 and Anthropic memory tool docs.

### Issue 1 — Secrets and credentials

mem0 explicit warning: "Avoid storing secrets or unredacted PII in user or org memories — Mem0 is retrievable by design."

Anthropic memory tool: "Claude will usually refuse to write down sensitive information in memory files. However, you may want to implement stricter validation that strips out potentially sensitive information."

**Framework rule:** Memory files must never contain credentials, API keys, tokens, or PII. The agent and the user share responsibility — agent refuses by default, user reviews during Reflect.

For database-backed memory (sub-category 6): row-level security and encryption-at-rest become design requirements rather than nice-to-haves.

### Issue 2 — Cross-user / cross-project leakage

If user-scoped memory holds "Adam works at Acme Corp," and Adam later opens an open-source contribution project, the agent shouldn't volunteer that detail. Personal facts that are *true* aren't always *appropriate* in every project context.

**Mitigation:** The framework should distinguish "user identity facts" (always loaded — communication style, role) from "user life facts" (loaded conditionally — employer, location, project history). The latter belongs in a separate memory tier or scope.

This is a v2 concern for the framework's current audience (solo devs) but worth flagging now so the boundary structure supports it later.

---

## Multi-agent shared memory (preview of v2)

The framework's audience uses multiple agents (Claude/Gemini/Codex) and may eventually use multiple specialized agents within one project. Shared memory across agents has its own boundary problems:

- **Claude wrote a memory; Gemini reads it.** Format compatibility — does Gemini understand Claude's memory format?
- **Two agents write to memory simultaneously.** Conflict. Last-writer-wins or merge?
- **Agent A is told a secret; Agent B should not know.** Partition by agent identity.
- **Memorix MCP server pattern**: One central memory layer, multiple agents query via MCP. Solves format compatibility but adds infrastructure.

**For v1:** Frame the framework's memory as agent-portable in *format* (plain markdown, descriptive filenames, simple frontmatter) but agent-scoped in *practice*. Different agents on the same project use the same memory files.

**For v2:** Multi-agent coordination, MCP-served memory, conflict resolution. Out of scope today.

---

## Token cost

Scope decisions affect token cost only indirectly — the cost is determined by how much of each scope gets loaded.

| Scope | Typical core-loaded size | Loaded when |
|-------|--------------------------|-------------|
| Personal | Small (1-3 KB) — identity + style | Always loaded |
| Project | Moderate (5-20 KB) — but only the index in core | Always for index; on-demand for files |
| Team | Variable | Conditionally loaded when relevant |

The framework should explicitly budget for personal scope being always-loaded core. Discipline in keeping it small (identity + 3-5 communication preferences) means it doesn't crowd out project memory.

---

## Patterns to borrow for our framework

1. **Project-local v1 memory.** TALL v1 is installed as a `.agent-loop` folder inside each project. A new project starts with a fresh `.agent-loop`; cross-project preference carryover is future CLI/shared-memory work.

2. **Project memory lives in the repo.** Project decisions, architecture, status, and conventions should live under the project-owned framework area and be versioned by git when git is present.

3. **Project-local personalization is explicit.** Preferences and taste notes inside `.agent-loop` use `scope: project` plus `kind: personalization`, not `scope: personal`.

4. **Two personalization tiers.** Always-loaded personalization should be tiny: identity, communication style, and workflow preferences relevant to this project. Broader personal history/life facts are conditional/on-demand.

5. **Team scope is reserved, not implemented.** `scope: team` may exist as a future schema value, but v1 does not provide shared/team memory.

6. **Reflect resolves uncertainty.** For ambiguous memory, use the project-local heuristic: generally reusable preference vs project-only fact. If uncertain or sensitive, ask during Reflect.

7. **No secrets, no PII, no credentials.** Hard rule. Both agent-side refusal and Reflect-time human review.

8. **Private memory gets generated ignores.** Bootstrap should add `.agent-loop/memory/private/` and `*.private.md` to `.gitignore`.

9. **Format-portable, agent-scoped.** Memory files use plain markdown with frontmatter so any agent can read them. Coordinated multi-agent/team writing is v2.

10. **Local MCP is optional advanced v1.** It can bridge cross-agent local recall for users who need it, but it is not an onboarding default.

---

## Re-grill decisions applied

The final v1 boundary differs from the early Pattern B research direction. Cross-project user memory is not part of v1 because `.agent-loop` is project-local. Project-local personalization remains useful, but the schema must not imply automatic carryover between projects.

---

## Sources

Direct reads:
- (Cross-references from sub-categories 1, 2, 4)
- [Anthropic memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) — security recommendations
- [Databricks — Memory Scaling for AI Agents](https://www.databricks.com/blog/memory-scaling-ai-agents) — personal vs organizational scope
- [Atlan — Types of AI Agent Memory](https://atlan.com/know/types-of-ai-agent-memory/) — governance state extension

Search-surfaced:
- [GitHub blog — How Squad runs coordinated AI agents](https://github.blog/ai-and-ml/github-copilot/how-squad-runs-coordinated-ai-agents-inside-your-repository/) — `.squad/` folder versioned with code; "onboarded AI team on clone"
- [DEV — Memorix: Shared Persistent Project Memory](https://dev.to/_2340687267e5cacfe32da1/memorix-give-your-ai-coding-agents-shared-persistent-project-memory-1pk2) — MCP-based cross-agent project memory
- [DEV — Multichannel AI Agent: Shared Memory Across Messaging Platforms](https://dev.to/aws/multichannel-ai-agent-shared-memory-across-messaging-platforms-56j4) — channel-spanning memory architecture
- [DEV — Designing Memory for 20 AI Agents Across 9 Nodes](https://dev.to/linou518/designing-memory-for-20-ai-agents-across-9-nodes-multi-agent-memory-architecture-4nhe) — hierarchical scope tree
- [CrewAI Memory docs](https://docs.crewai.com/en/concepts/memory) — short-term/long-term/entity scopes
- [mem0 — security guidance](https://docs.mem0.ai/core-concepts/memory-types) — secret/PII warning

New sources discovered:
- [Anthropic — Multi-repository support feature request](https://github.com/anthropics/claude-code/issues/23627)
- [Augment Code — AI Coding Assistants for Large Codebases](https://www.augmentcode.com/tools/ai-coding-assistants-for-large-codebases-a-complete-guide)
