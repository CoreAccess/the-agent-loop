# Agentic Engineering - Brendan O'Leary

Status: out-of-cycle research note. Supporting evidence only; not core truth.
Date captured: 2026-04-29

Source:
- Video: "Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary"
- URL: https://www.youtube.com/watch?v=BEKc4P87XKo
- Channel: AI Engineer
- Transcript source: distilled into this note; local root transcript was removed after capture.

## Evidence Weight

This is a practitioner talk, not a formal study. Treat it as useful evidence about how experienced AI-assisted developers are describing current workflows, failure modes, and tool configuration patterns.

The strongest value for The Agent Loop is not any single factual claim. The value is that the talk independently reinforces several framework directions already present in the research: deliberate context loading, explicit lifecycle phases, AGENTS.md as always-loaded project guidance, skills as on-demand workflow guidance, agent permissions, and PR-like review of agent work.

## Core Takeaways

### From tool use to collaborative workflow

The talk frames modern AI coding agents as something beyond autocomplete: they can inspect files, plan changes, edit code, run tests, and prepare pull-request-like work. The speaker's recommended mental model is close to "very fast junior engineer": useful, high-energy, broadly knowledgeable, but missing local judgment, business context, and awareness of past architectural reasons.

Framework implication: The Agent Loop should teach users to direct agent work, not merely accept generated code. The human's highest-leverage work is deciding what to hand off, what to keep, and what judgment the agent lacks.

Relevant categories:
- 1 - Agent Contract
- 2 - Project Bootstrap & Onboarding
- 8 - Change Gates & Guardrails
- 11 - Agentic Patterns

### Context engineering is a first-class skill

The talk emphasizes that context is not automatically good. Extra context increases cost, can reduce quality, and can preserve bad assumptions from a failed path. Bad or stale context can continue influencing the agent after the user believes they have corrected course.

Recommended practices from the talk:
- Persist durable information outside the active context window.
- Pull in only context relevant to the current step.
- Summarize, trim, and compress after long discovery or debugging phases.
- Start a fresh session when the work has gone down the wrong path.
- Isolate unrelated tasks into separate sessions or agents.
- Disable unused MCP servers/tools when they add prompt overhead or irrelevant capability descriptions.

Framework implication: The Agent Loop's just-in-time memory loading decision is strongly reinforced. Category 9 should treat context loading as active engineering work, not as a passive "load everything" step.

Relevant categories:
- 6 - Memory Systems
- 9 - Context Loading & Management
- 12 - Observable Development

### Research, plan, then implement

The talk recommends a research-plan-implement loop as a practical response to common agent mistakes. The research phase should understand the existing system, relevant files, data flow, local patterns, and edge cases before code changes begin. The plan phase should define files to change, verification steps, tests, and explicit in-scope/out-of-scope boundaries. Only after that should implementation start.

The talk also recommends using separate modes or sessions:
- Research/ask mode: understand the system without writing code.
- Architect/plan mode: produce explicit implementation instructions.
- Code mode: execute the plan in a clean, narrow context.

Framework implication: this strongly supports an explicit work loop with Research before implementation.

Relevant categories:
- 2 - Project Bootstrap & Onboarding
- 3 - Planning & Architecture Docs
- 7 - Testing & Verification Loops
- 11 - Agentic Patterns

### Plans should be executable and reviewable

The talk treats a plan as a real artifact, not a vague summary. A useful plan includes specific file changes, verification commands, test additions, and scope boundaries. The plan should be reviewed by the human before implementation begins.

Framework implication: The Agent Loop planning docs should not only say what the agent intends to do. They should include enough structure that a smaller or cheaper implementation model could execute the plan, and enough verification detail that the human can catch missing tests before code is written.

Relevant categories:
- 3 - Planning & Architecture Docs
- 4 - Spec-Driven Development
- 7 - Testing & Verification Loops

### AGENTS.md and skills have different jobs

The talk describes `AGENTS.md` as the place for always-on project rules: conventions, build/test commands, requirements, and repository-specific guidance. Skills are presented as reusable on-demand playbooks for specific workflows.

Framework implication: this independently supports the Category 6 decision already made for The Agent Loop: mandatory procedural behavior belongs in root agent instructions, while task-specific procedures belong in skills and should load only when relevant.

Relevant categories:
- 1 - Agent Contract
- 5 - Skills & Reusable Capabilities
- 6 - Memory Systems
- 9 - Context Loading & Management

### Agent permissions should be tuned and revisited

The talk calls out the practical question of what agents can do autonomously: read files, run tests, modify code, use worktrees, run multiple agents, or require approvals. It frames these settings as something developers should tune as they gain experience.

Framework implication: Category 8 should probably avoid a single universal permission preset. The Agent Loop may need a small set of permission profiles, plus instructions for when to loosen or tighten them based on project risk, user trust, and task type.

Relevant categories:
- 8 - Change Gates & Guardrails
- 11 - Agentic Patterns

### MCPs and external APIs need context discipline

The talk treats MCPs as useful but potentially costly context providers. It also describes a practical ladder for internal APIs: use an OpenAPI/Swagger spec when available; convert stable API docs into markdown when useful; use reference URLs for frequently changing docs; build a custom MCP server only when workflows are complex enough to justify it.

Framework implication: The Agent Loop should not present MCP as the default answer for every integration. MCP is a powerful option, but markdown specs, reference docs, and JIT retrieval may be simpler and safer for many projects.

Relevant categories:
- 5 - Skills & Reusable Capabilities
- 6 - Memory Systems
- 9 - Context Loading & Management

### Review agent work like junior-engineer work

The talk recommends isolating the agent's work and reviewing it like a pull request. Local Git becomes a first review layer before pushing work to a team PR.

Framework implication: The Agent Loop's change gates should include local review habits: inspect diffs, commit frequently when stable, keep agent work isolated when possible, and treat passing tests as necessary but not sufficient.

Relevant categories:
- 7 - Testing & Verification Loops
- 8 - Change Gates & Guardrails
- 12 - Observable Development

## Candidate Patterns To Borrow

### One task per session

Use a session for one coherent goal. If the task changes materially or the context becomes polluted by a failed path, summarize the useful state and restart with a clean context.

Open design question: should The Agent Loop make this a default rule, a recommendation, or a threshold-based gate?

### Human-reviewed handoff summaries

Before restarting or handing work to another session/agent, ask the current agent to summarize the state. The human reviews the summary before it becomes the next session's prompt.

This fits The Agent Loop's memory discipline because it separates candidate memory from accepted memory.

### Research artifact before plan artifact

For non-trivial work, the agent should first produce a short research artifact covering:
- how the system currently works
- relevant files
- local patterns to follow
- data/control flow
- edge cases
- unknowns

Only after human review should it produce the implementation plan.

### Plan artifact with verification commands

A useful plan should include:
- files likely to change
- ordered steps
- tests or checks to add
- commands to run
- in-scope and out-of-scope boundaries
- rollback or stop conditions for risky changes

### JIT MCP/tool loading

Agents should avoid always enabling unrelated MCP servers or tool bundles. Tool context should be loaded when it is relevant to the active task and removed/disabled when it is not.

## Questions To Carry Forward

- Category 8: What permission profiles should The Agent Loop recommend for read-only research, local implementation, refactors, external API calls, deploys, and destructive actions?
- Category 8: What exactly counts as a "large rework" that should stop for user approval?
- Category 9: Should The Agent Loop include an explicit context meter rule, and if so should it use percentages, symptoms, or a softer "restart when polluted" heuristic?
- Category 9: How should The Agent Loop express one-task-per-session without creating annoying ceremony for small fixes?
- Category 5: How should cross-agent skills represent modes like Ask, Architect, and Code when each agent exposes different primitives?
- Category 7: How do we test that the agent followed the research-plan-implement policy rather than merely producing a plan artifact and ignoring it?
- Category 12: What should a lightweight progress log capture during long-running agentic work?

## Do Not Treat As Decided Yet

- The claimed context-quality threshold needs independent validation before becoming a hard rule.
- The exact mode names are tool-specific and should not be copied directly into The Agent Loop unless they map cleanly across Codex, Claude Code, Gemini, and other target agents.
- Parallel agents and worktrees are promising but should remain advanced or v2 until Category 11 deep research confirms the right launch scope.
