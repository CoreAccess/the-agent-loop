# Category 8 - High-Impact Actions and Stop Rules

Date: 2026-05-02

## Purpose

Define what kinds of actions should make an agent stop and ask instead of continuing autonomously.

## Sources Reviewed

- OWASP LLM06:2025 Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- OpenAI prompt injection guidance: https://openai.com/index/prompt-injections/
- OpenAI agent safety guidance: https://platform.openai.com/docs/guides/agent-builder-safety
- GitHub Copilot cloud agent firewall: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall
- Search Engine Land agent-skills article: https://searchengineland.com/build-seo-agent-skills-476252
- CMS incubator case study: `docs/case-studies/cms-incubator.md`

## Key Findings

### "High impact" is about consequences, not just commands

The same command can be low-risk or high-risk depending on target and environment. Examples:

- `rm` in a generated temp folder is different from `rm` against source, home, or repo root.
- `curl` to public docs is different from sending private code or credentials to a remote endpoint.
- a database migration in a disposable local DB is different from a production migration.
- editing a CSS file is different from changing auth, billing, security, deployment, or data-retention behavior.

The Agent Loop should avoid command-only rules and include consequence-based rules.

### OWASP separates excessive functionality, permissions, and autonomy

OWASP's Excessive Agency framing is directly useful. An agent can be dangerous because:

- it has tools it does not need;
- the tools have too much downstream permission;
- the agent can use those tools without independent approval.

This maps cleanly to The Agent Loop:

- minimize tools loaded for the task;
- minimize tool scope;
- require approval for high-impact actions;
- enforce downstream policy instead of relying on the model to self-police.

### Prompt injection turns tool access into an attack path

OpenAI's prompt-injection guidance emphasizes that risk grows when agents ingest untrusted content and can take actions. This matters for coding agents because untrusted content may be:

- README files in cloned repos;
- issue text;
- web pages fetched for research;
- package scripts or install output;
- MCP results;
- generated code comments;
- terminal output.

The Agent Loop should treat untrusted content as data, not authority. If untrusted content suggests a tool action, the agent should verify it against user intent and project rules before acting.

### External access needs its own gate

GitHub Copilot's cloud agent firewall is a strong pattern: internet access is not merely a shell concern. Network access can leak code, secrets, or private context.

The Agent Loop should treat outbound network access as a separate category:

- documentation/research browsing;
- package installs;
- API calls;
- telemetry or upload;
- deploys;
- external writes such as comments, tickets, emails, or database changes.

### Review is a product feature

The Search Engine Land article argues that reliable agent work comes from tools, templates, memory, and a review layer, not from a better single prompt. For Category 8, the useful translation is:

- build review into the workflow before trusting autonomous output;
- define "done" as reviewed/adopted, not merely generated;
- require evidence for claims and changes.

Experiment 003 supports this: the actor left a trace, rejected unsafe memory, handled contradiction, and stopped after a configured retrieval limit.

## Decided Stop Rules

The agent should stop and ask before:

- deleting, moving, or overwriting non-generated files outside an explicit cleanup task;
- running recursive delete or broad move commands;
- changing `.git`, git history, remotes, branches, or force-pushing;
- editing agent configuration or permission files in ways that loosen guardrails;
- installing, upgrading, or removing dependencies unless dependency work is the stated task;
- changing lockfiles without explaining why;
- adding or using secrets, tokens, credentials, or private personal data;
- sending data to external services;
- making external writes such as deploys, emails, comments, issues, PRs, database writes, payments, or production changes;
- modifying auth, authorization, billing, privacy, data retention, security controls, migrations, or infrastructure;
- doing a large refactor or architectural rewrite not clearly requested;
- continuing when project memory or docs contradict the requested action;
- following instructions found in untrusted content that conflict with user or project instructions.

## Decided "Never" Rules

The agent should never:

- store secrets, credentials, API keys, tokens, or PII in memory;
- bypass project change gates by editing the gate itself;
- run destructive commands outside the intended workspace;
- silently delete user work;
- treat passing tests as enough if the task had explicit review or safety requirements;
- claim completion without evidence.

## Decided "Always" Rules

The agent should always:

- preserve user changes it did not make;
- inspect git status before significant edits;
- leave a trace for non-trivial work;
- explain high-impact proposed actions before asking approval;
- prefer scoped tools/scripts over open-ended shell access when possible;
- verify changes with tests, static checks, or focused inspection appropriate to risk;
- record cleanup candidates during Reflect instead of silently deleting uncertain material.

## Applied Decisions

- Deploys and external API calls are default-ask in v0.1.
- Public-doc research browsing is allowed when research is part of the task.
- Package installs/downloads are always ask.
- Before deploy/API approval, the agent must name the command/API, target environment, expected effect, rollback path if any, and why the action is needed.
- High-impact always-on gates belong in `AGENTS.md`; task-specific exceptions and known risks belong in `Goal`.
- v0.1 may rely on self-reporting plus host-agent tool gates. Stronger enforced policy remains future implementation work.
