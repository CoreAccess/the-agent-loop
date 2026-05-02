# Category 8 - Permission Models and Autonomy

Date: 2026-05-02

## Purpose

Research how AI coding tools handle autonomy, approvals, permission modes, and user control. This doc focuses on the Q6 tension: agents need enough freedom to work, but users need hard stops for high-risk actions.

## Sources Reviewed

- Claude Code permission modes: https://code.claude.com/docs/en/permission-modes
- Continue CLI tool permissions: https://docs.continue.dev/cli/tool-permissions
- Cline Auto Approve and YOLO Mode: https://docs.cline.bot/features/auto-approve
- OWASP LLM06:2025 Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- OpenAI agent safety guidance: https://platform.openai.com/docs/guides/agent-builder-safety
- Search Engine Land, "How to build SEO agent skills that actually work": https://searchengineland.com/build-seo-agent-skills-476252

## Key Findings

### Permission models are layered, not binary

The strongest tools separate permission concerns into layers:

- mode: read-only, normal, auto, locked-down, bypass;
- tool category: read, write, shell, browser, MCP, external API;
- path scope: workspace, additional directories, protected paths, outside workspace;
- rule type: allow, ask, deny, exclude;
- environment: local machine, container, VM, remote sandbox, CI;
- review point: before each tool call, before high-impact action, after a batch, before merge.

Claude Code, Continue, and Cline all expose some form of this. The pattern argues against a single "agent autonomy" switch in The Agent Loop.

### Default autonomy should probably be workspace-local, not system-wide

The user's initial instinct was broad autonomy inside the codebase. Research supports that direction if "inside the codebase" is treated as a hard boundary:

- workspace file edits can usually be allowed when the task is clear and the user will inspect the diff;
- reads should usually be broad inside the project;
- writes outside the project, protected files, shell commands, browser actions, MCP tools, and external APIs need separate treatment.

The risky jump is not "agent edits code"; it is "agent can do anything the host user can do."

### Deny rules and protected paths matter

Claude Code documents protected paths and deny rules. Continue supports `allow`, `ask`, and `exclude`. OWASP recommends minimizing tool functionality and downstream permissions.

Pattern to borrow: The Agent Loop should describe deny/never rules as higher authority than convenience settings. A permissive profile should not override hard bans such as secrets, production deletion, force-push, or writes outside declared workspace scope.

### Model-classified safety is useful but insufficient

Claude Code's auto mode uses a classifier. Cline's docs say commands are classified as safe or approval-required by the model. GitHub Copilot cloud agent uses a firewall for internet access.

These are useful, but they do not replace project policy. Cline's own docs warn that full auto approval should be used only in controlled settings. OWASP's framing is stronger: excessive functionality, permissions, and autonomy are separate risk roots.

### Prompt-injection risk grows with autonomy

OpenAI and OWASP both emphasize that agents acting on untrusted content create higher risk. The risk rises when a model reads web pages, repo files, emails, MCP output, or other external content and then has enough tool access to act on it.

Pattern to borrow: high-autonomy modes need both narrower tools and stronger environment isolation. "Trust the model" is not a guardrail.

## Permission Profiles for The Agent Loop

### 1. Research / Read-Only

Allowed:

- read files in workspace;
- search files;
- inspect git status/diff;
- browse or fetch sources when explicitly part of research.

Ask:

- writing files;
- installing dependencies;
- running tests that modify state;
- external API calls.

Use for:

- codebase exploration;
- research;
- planning;
- review.

### 2. Local Build

Allowed:

- read project files;
- edit files inside workspace;
- run known project-local test/build commands;
- create new files under existing directories.

Ask:

- dependency changes;
- network calls;
- destructive file operations;
- changes outside workspace;
- schema migrations;
- deploys.

Use for:

- normal feature work;
- bug fixes;
- scaffold edits.

This is the decided v0.1 default.

### 3. Trusted Iteration

Allowed:

- workspace edits;
- repeated build/test/lint loops;
- non-destructive filesystem commands in workspace.

Ask:

- deletion of non-generated files unless cleanup scope is explicit;
- external side effects;
- permission or config changes;
- broad refactors.

Use for:

- sessions where the user is reviewing diffs after the fact and wants fewer approval prompts.

### 4. Isolated Sprint

Allowed:

- broader command execution;
- package installation;
- experiments;
- larger generated changes.

Required environment:

- container, VM, dev container, remote sandbox, or disposable worktree;
- clean git checkpoint before work starts;
- no production credentials;
- no mounted sensitive directories outside the project.

Use for:

- high-speed experiments;
- risky migrations;
- unfamiliar generated code.

### 5. Locked-Down Automation

Allowed:

- only pre-approved tools and commands;
- no interactive prompts.

Use for:

- CI;
- scripted checks;
- repeatable maintenance jobs.

## Decided v0.1 Rule

The v0.1 default should be:

> Agents may work autonomously inside the project workspace for clear local code changes, but must stop before irreversible, external, privileged, broad, or ambiguous actions.

This keeps the user's preferred freedom as the default while drawing the actual boundary around blast radius, not around arbitrary task size.

## Applied Decisions

- v0.1 default permission posture is **Local Build**.
- Agents may autonomously read/edit inside the project workspace and run known local project commands such as tests, lint, build, format, and focused scripts.
- Agents must ask before dependency changes, network/API calls, deploys, destructive operations, writes outside workspace, permission changes, auth/security/data/infrastructure changes, or broad refactors.
- Dependency installation is always ask in v0.1, including greenfield projects, unless dependency work is explicitly requested.
- Deploys and account/project API calls are default-ask in v0.1. Project-configurable automation is deferred until later.
- Mapping these profiles to Codex, Claude Code, Gemini CLI, Cursor, and other agents remains future implementation work.
