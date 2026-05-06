# Agentic Engineering - Brendan O'Leary

Date captured: 2026-04-29
Status: compact supporting note; practitioner evidence only

## Required Context

This practitioner talk reinforced several directions already present in the research:

- Treat agents like fast junior engineers: useful, energetic, and broad, but missing local judgment and history.
- Engineer context deliberately. More context can cost more, preserve stale assumptions, and lower quality.
- Use a research-plan-implement loop for non-trivial work.
- Keep `AGENTS.md` for always-on project rules and skills for task-specific playbooks.
- Tune agent permissions by task and revisit them as trust changes.
- Review agent output like pull-request work, with local diffs and verification.

## Applied Implications

- The Agent Loop should load project context just in time, not dump the whole repo or docs tree.
- Non-trivial work benefits from a short research artifact before a plan and implementation.
- Plans should include files likely to change, ordered steps, verification commands, in/out-of-scope boundaries, and stop conditions.
- MCPs and external APIs should be loaded only when relevant; markdown specs or reference URLs may be simpler.
- Parallel agents, worktrees, and tool-specific mode names are advanced/future patterns, not default v0.2 behavior.

## Source Basis

- Video: "Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary"
- URL: https://www.youtube.com/watch?v=BEKc4P87XKo
- Channel: AI Engineer

## Revisit Triggers

- Category 5 skill design.
- Category 7 verification-loop design.
- Category 9 context-loading rules.
- Category 11 agentic-pattern decisions.
- Category 12 progress-log and observable-development work.
