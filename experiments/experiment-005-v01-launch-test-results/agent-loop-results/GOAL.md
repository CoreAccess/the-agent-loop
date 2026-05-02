# Goal

Status: Draft for user approval
Last updated: 2026-05-02

## Objective

Initialize The Agent Loop for this workspace by recording the observed project state, safe operating posture, and approvals needed before any code implementation starts.

## Why

The workspace currently appears to contain only The Agent Loop v0.1 scaffold. A project-specific Goal and Status are needed so future work has clear scope, known commands, verification expectations, and stop conditions before code or app scaffolding begins.

## Scope

In scope:

- Preserve the existing `.agent-loop/` scaffold.
- Record the current repository inspection results.
- Establish the default Local Build permission posture for onboarding.
- Identify that the actual product, app, or code objective still needs user approval before implementation.
- Propose future root agent-instruction integration only after user approval.

Out of scope:

- Creating application/source files.
- Installing, upgrading, or removing dependencies.
- Initializing git or changing git history.
- Adding root instruction files or modifying non-`.agent-loop/` project files.
- Deploying, publishing, pushing, creating PRs, or performing external side effects.

## Acceptance Criteria

- `.agent-loop/GOAL.md` records this onboarding goal as a draft.
- `.agent-loop/STATUS.md` records the inspected workspace state and blocked approvals.
- No code, dependency, git, or root instruction changes are made before the user approves or edits this Goal.
- The next implementation task does not start until the user provides the actual project objective or approves a concrete scaffold/build plan.

## Allowed Commands

Known local commands the agent may run under Local Build:

```text
Get-Content -LiteralPath <path>
Get-ChildItem -Force
Get-ChildItem -LiteralPath <path> -Force
rg --files --hidden
rg -n <query> <path>
git status --short
```

## Constraints

- Work inside the project workspace.
- Use markdown project memory by default.
- Do not store secrets, credentials, API keys, tokens, or PII in memory or docs.
- Ask before dependency changes, external side effects, broad/deep refactors, and high-risk actions listed in `.agent-loop/AGENTS.md`.
- Do not make code changes until the user approves or edits this draft Goal.
- Do not initialize git, create app scaffolding, or add root instruction integration without explicit approval.

## Resources And Budgets

- Retrieval attempts before escalation: 2 failed memory lookup attempts.
- Durable memory candidates per Reflect pass before asking for prioritization: 3.
- Time or scope budget: onboarding documentation only until this draft is approved.

## Current Context

- Workspace path: `C:\Users\adamd\Downloads\Programming\AgentExperimentations`.
- Detected files are limited to `.agent-loop/` scaffold files.
- No application source directories, package manifests, build files, test files, root docs, or root agent instruction files were detected outside `.agent-loop/`.
- `git status --short` reports this workspace is not a Git repository.
- `.agent-loop/STATUS.md` and `.agent-loop/GOAL.md` were placeholder-style before onboarding.
- `.agent-loop/MEMORY.md` has no active indexed project memory records.

## Checklist

1. Read `.agent-loop/AGENTS.md`, `.agent-loop/STATUS.md`, `.agent-loop/GOAL.md`, and `.agent-loop/MEMORY.md`.
2. Select task-relevant memory from `.agent-loop/MEMORY.md`.
3. Inspect and record git/dirty state before significant edits.
4. Draft `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md` for approval.
5. Stop for user approval or edits before implementation.
6. After approval, build inside the accepted scope.
7. Log notable work.
8. Check the result with the allowed verification commands.
9. Reflect before finishing.
10. Ask before adopting durable memory or broad scaffold rule changes.

## Stop Conditions

Stop and ask before:

- changing scope beyond this Goal;
- dependency install/upgrade/remove or lockfile changes;
- deploys, pushes, publishes, PRs, issue/comment writes, API calls, or production/account-affecting actions;
- broad deletion, destructive moves, or writes outside the workspace;
- auth/security/data/infra/CI/permission changes;
- broad refactors or architecture changes;
- continuing through contradictions in project memory or docs.

## Escalation Triggers

- Retrieval misses memory that should exist after index lookup and keyword search.
- A candidate memory contains sensitive data.
- A candidate contradicts active memory or may supersede a project decision.
- The agent wants to add non-default storage, automation, multi-agent orchestration, or external side effects.
- More durable memory candidates appear than the Reflect budget allows.

## Verification Criteria

- For this onboarding draft, verification is review-based: the user approves or edits `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md`.
- For future implementation, verification commands must be added after the project stack is known.

## Memory Candidates

Use `.agent-loop/memory/proposed/` for durable candidates. Each candidate needs a source stamp, classification, rationale, risk, and human approval before becoming active durable memory.
