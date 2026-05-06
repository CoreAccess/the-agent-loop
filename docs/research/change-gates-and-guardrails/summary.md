# Category 8 - Change Gates And Guardrails

Date: 2026-05-02
Status: deep research complete; adopted into v0.1 and carried into v0.2

## Required Context

Category 8 defines when agents may act autonomously, when they must ask, and when they must refuse. The core rule is consequence-based:

> Agents may work autonomously inside the project workspace for clear local changes, but must stop before irreversible, external, privileged, broad, ambiguous, or contradiction-heavy actions.

This is separate from Category 1. Category 1 owns the authority contract; Category 8 owns enforcement boundaries.

## Applied Implications

- Default posture is Local Build: read/edit inside workspace and run known project-local checks for clear tasks.
- Ask before dependency changes, external network/API effects, deploys, pushes, PRs, comments, database writes, broad deletion, writes outside workspace, auth/security/privacy/infra/CI/migration changes, git history changes, broad refactors, or continuing through project-state contradictions.
- Never store secrets/credentials/PII, silently delete or revert user work, run destructive commands outside the intended workspace, bypass gates by editing gate files, or claim completion without evidence.
- Before significant edits, inspect dirty state and keep user work distinguishable from agent work.
- Cleanup is required when removing or replacing behavior, but deletion needs usage evidence, reference search, and appropriate verification.
- Sandboxing is recommended for high-autonomy, untrusted, dependency-install, migration, or broad automation work; it is not required for normal Local Build work.

## Source Basis

- Claude Code, Continue, and Cline permission models: permissions are layered by mode, tool, path, command, and environment.
- OWASP LLM06 Excessive Agency: excessive functionality, permissions, and autonomy are distinct risks.
- OpenAI prompt-injection and agent-safety guidance: untrusted content plus tool access increases risk.
- GitHub Copilot cloud-agent firewall: external access is its own risk surface.
- Google small-CL guidance and Fowler refactoring/branch-by-abstraction: large changes should be reviewable and often incremental.
- OpenRewrite: automated cleanup needs semantic evidence.
- Aider and Gemini CLI: git/checkpoints are practical rollback layers.
- Developer pain reports: approval fatigue creates demand for middle permission layers, not no guardrails.
- Experiment 004: realistic guardrail edit scored 23/24; the main promoted fix was explicit dirty-state/checkpoint wording.

## Revisit Triggers

- Defining v0.3 guardrail wording.
- Creating reusable cleanup, dependency-change, deploy, or refactor-plan skills.
- Adding sandbox/checkpoint recommendations for specific agents.
- Designing observable-development limits for cost, parallelism, and long-running loops.
