# Category 8 - Developer Pain and Reference Implementations

Date: 2026-05-02

## Purpose

Capture non-vendor signals from GitHub issues/discussions, Reddit, and reference implementations. These are not authoritative on their own, but they show what breaks in practice.

## Sources Checked

- Cline discussion, "Command Auto-Approval Rules": https://github.com/cline/cline/discussions/2253
- Cline issue, "Auto-approve Settings UI State Management Bug": https://github.com/cline/cline/issues/4138
- Reddit, "Railguard - A safer --dangerously-skip-permissions for Claude Code": https://www.reddit.com/r/ClaudeCode/comments/1rwdaq3/railguard_a_safer_dangerouslyskippermissions_for/
- Reddit, "My firejail --dangerously-skip-permissions wrapper": https://www.reddit.com/r/ClaudeCode/comments/1rytubz/my_firejail_dangerouslyskippermissions_wrapper/
- Reddit, "F'd around, found out --dangerously-skip-permissions": https://www.reddit.com/r/ClaudeCode/comments/1slcowg/fd_around_found_out_dangerouslyskippermissions/
- Reddit, "Claude Code with --dangerously-skip-permissions is a real attack surface": https://www.reddit.com/r/ClaudeAI/comments/1s2qdh0/claude_code_with_dangerouslyskippermissions_is_a/
- OpenHands Docker sandbox: https://docs.openhands.dev/sdk/guides/agent-server/docker-sandbox
- Aider git integration: https://aider.chat/docs/git.html
- Gemini CLI checkpointing: https://google-gemini.github.io/gemini-cli/docs/cli/checkpointing.html

## Pain Signals

### Approval fatigue is real

Developer discussions consistently show that repeated approval prompts interrupt flow. This is why users reach for broad auto-approval or dangerous modes.

Framework implication: The Agent Loop should not default to nagging. It should reduce low-value prompts through clear workspace-local permissions and known safe commands.

### All-or-nothing dangerous modes create a demand for middle layers

Multiple developer threads are about making dangerous modes safer with hooks, wrappers, firejail, containers, or custom allow/deny logic. The demand is not "no guardrails." The demand is "less friction without removing every guardrail."

Framework implication: The Agent Loop should recommend a middle path:

- auto-allow routine local work;
- ask for high-impact actions;
- use sandboxing for broad autonomy;
- keep audit logs and rollback points.

### Command safety is context-dependent

Cline's command auto-approval discussion highlights the problem with model-only command safety: a command like `cat` or `rm` depends heavily on path and intent. A read inside the project may be fine; the same read against user secrets is not.

Framework implication: The Agent Loop should define gates by command + target + consequence, not by command string alone.

### Permission UI/state clarity matters

Cline issues around auto-approval setting state show that confusing permission interfaces are themselves a guardrail failure. If users cannot tell what is enabled, they cannot reason about risk.

Framework implication: The Agent Loop's generated rules should be explicit and inspectable in plain language.

### Community reference implementations converge on sandboxing

Developer-built solutions such as firejail wrappers, sandboxed pods, and hook-based monitors point toward the same answer as official tools: isolate the agent, scope filesystem access, limit secrets, and keep project work in a controlled workspace.

Framework implication: v0.1 can document sandboxing as an advanced profile even if it does not provide its own sandbox runner.

### Cost and resource burn are also guardrail issues

One Reddit report about dangerous mode described unexpected parallel research and rapid credit burn. Even without filesystem damage, unbounded autonomy can waste money and time.

Framework implication: Category 8 should include consumption boundaries:

- avoid unbounded parallelism in v1;
- ask before launching many agents or long-running loops;
- log long-running commands;
- stop when search/retrieval limits are reached.

## Reference Implementation Patterns

### Aider: git as rollback and separation

Aider's git integration auto-commits AI edits and preserves dirty user work separately. Pattern to borrow: keep user edits distinguishable from agent edits and make undo/review cheap.

### Gemini CLI: checkpoint before file modification

Gemini CLI checkpointing creates a restorable snapshot before file-modifying tools. Pattern to borrow: checkpoint before risky edits, even if implementation differs by agent.

### OpenHands: Docker sandbox

OpenHands uses Docker as its recommended local sandbox provider. Pattern to borrow: high autonomy belongs in a bounded execution environment.

### Cline: auto-approval categories

Cline exposes separate toggles for read files, edit files, commands, browser, and MCP. Pattern to borrow: permissions should map to capability categories, not one global yes/no.

## Applied Decisions

- v0.1 should include plain-language always-on guardrail rules in `AGENTS.md`.
- Task-specific permission exceptions and allowed commands belong in `Goal`.
- Blocked approvals, dirty state, checkpoint status, skipped verification, and unresolved cleanup belong in `STATUS.md` / handoff.
- Reusable procedures such as cleanup, deploy, dependency-change, and refactor-plan checklists belong in skills.
- v0.1 should describe the desired sandbox boundary rather than provide its own sandbox runner.
- Cost/parallelism stop rules remain relevant but likely belong in Category 12 Observable Development unless they directly create guardrail risk.
