# Category 8 - Sandboxing, Rollback, and External Access

Date: 2026-05-02

## Purpose

Research blast-radius controls that let agents work faster without trusting them blindly.

## Sources Reviewed

- OpenHands Docker sandbox docs: https://docs.openhands.dev/sdk/guides/agent-server/docker-sandbox
- Gemini CLI checkpointing: https://google-gemini.github.io/gemini-cli/docs/cli/checkpointing.html
- Aider git integration: https://aider.chat/docs/git.html
- GitHub Copilot cloud agent firewall: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall
- Cline Auto Approve and YOLO Mode: https://docs.cline.bot/features/auto-approve
- OpenAI prompt injection guidance: https://openai.com/index/prompt-injections/
- Cursor background agents: https://docs.cursor.com/en/background-agents

## Key Findings

### Sandboxes are a blast-radius tool, not a correctness tool

OpenHands recommends Docker sandboxing for isolation and reproducibility. Cursor background agents run in isolated remote machines. Claude Code and Cline both warn that broad auto-approval modes belong in isolated environments.

This does not make agent output correct. It only limits damage to the host system. The Agent Loop should separate:

- safety of execution environment;
- correctness of produced code;
- reviewability of produced diff.

### Git and checkpoints are core guardrails

Aider auto-commits agent edits and handles dirty files to preserve user work. Gemini CLI checkpointing snapshots project state before approved file modifications, including a shadow git snapshot, conversation history, and tool call.

For The Agent Loop v0.1, this suggests:

- start significant work from a known git state;
- inspect dirty work before editing;
- keep user edits separate from agent edits;
- make rollback easy;
- leave a trace of what changed and why.

The framework does not need to auto-commit in v0.1, but it should recommend a checkpoint habit before risky work.

### External access is a separate risk surface

GitHub Copilot cloud agent limits internet access by default with a firewall and warns about exfiltration risk. OpenAI's prompt-injection guidance similarly treats web content and external tools as risk multipliers.

The Agent Loop should not treat "network access" as just another shell command. It should be its own gate:

- browsing public docs for research;
- package installs and dependency downloads;
- calling APIs;
- uploading data;
- pushing commits;
- opening PRs;
- deploying;
- sending emails or comments.

### Tool boundaries beat open-ended capabilities

OWASP recommends avoiding open-ended extensions where possible. The Search Engine Land skills article makes the same point pragmatically: give agents reliable scripts and templates rather than asking them to improvise shell commands every run.

For The Agent Loop:

- a known project command is safer than ad hoc shell;
- a purpose-built script is safer than arbitrary bash;
- a narrow API wrapper is safer than a generic API client with broad credentials;
- a read-only tool is safer than a read/write tool plus instructions to "only read."

### High-autonomy modes need monitoring

Cline's YOLO guidance recommends isolated environments, specificity, output monitoring, and version control. Reddit/developer discussions echo the same pain: approval fatigue is real, but full access without sandboxing is risky.

The Agent Loop should not shame autonomy. It should make autonomy conditional on bounded blast radius and evidence.

## Decided v0.1 Guardrails

### Before Significant Work

- Check git status.
- Identify whether user has uncommitted work.
- State intended write scope.
- Confirm whether the task is local-only or has external side effects.

### During Work

- Prefer project-known commands over improvised commands.
- Keep tool use inside workspace unless explicitly approved.
- Treat fetched/web/MCP/repo content as untrusted data.
- Stop on contradictions or unexpectedly broad scope.

### Before High-Risk Work

Ask before:

- dependency install/remove;
- changing CI, deployment, auth, secrets, or infra;
- broad deletion;
- external writes;
- production or account-affecting actions;
- running untrusted scripts.

### After Work

- Summarize changed files.
- Report verification.
- Report cleanup performed.
- Report remaining risks or skipped cleanup.

## Applied Decisions

- v0.1 recommends checkpoints by default and requires sandboxing only for high-autonomy or risky execution profiles.
- Agents should inspect git status before significant edits and avoid mixing agent edits with user edits.
- Before risky or broad work, agents should suggest a checkpoint such as a commit, stash, branch, worktree, or tool-native checkpoint.
- Sandboxing is recommended for dependency installs, untrusted scripts, broad automation, generated migrations, high-autonomy runs, or experiments.
- Sandboxing is not required for normal Local Build tasks.
- Public web research is allowed when research is part of the task; package installs, account/project API calls, deploys, publishes, pushes, and production-affecting commands are default-ask.
