# Project Roadmap

Status: accepted

Owner approval: accepted in chat on 2026-05-06.

## Vision Goal

The Agent Loop becomes a practical, portable framework for AI-assisted software development across Codex/ChatGPT, Claude Code, Gemini, and similar coding agents.

It should help experienced AI-assisted developers run projects through a repeatable loop: clarify intent, load the right context, work inside explicit boundaries, verify outcomes, reflect, and preserve useful learning without bloating every future session.

## Milestones

- Done: Broad research sweep across the original category list.
- Done: Category 2 Project Bootstrap and Onboarding deep research and re-grill.
- Done: Category 6 Memory Systems deep research and re-grill.
- Done: Category 8 Change Gates and Guardrails deep research, re-grill, and adoption into the scaffold.
- Done: v0.1 frozen as the historical baseline release.
- Done: v0.2 locked as the active scaffold release with layered `.agent-loop/project/` state.
- Done: Self-applied v0.2 inside this repository and cleaned legacy root state.
- Done: Cleaned release ZIP tracking and added docs indexes for selective research loading.
- Next: Use v0.2 to define the first v0.3 improvement goal.

## Future Goals

- Validate v0.2 self-application behavior after the root adapter is active: startup loading, second-prompt behavior, and handoff quality.
- Identify v0.3 improvements from using v0.2 in this repo.
- Research remaining categories when they directly inform v0.3:
  - Category 1: Agent Contract.
  - Category 3: Planning and Architecture Docs.
  - Category 5: Skills and Reusable Capabilities.
  - Category 4: Spec-Driven Development.
  - Category 7: Testing and Verification Loops.
  - Category 9: Context Loading and Management.
  - Category 10: Error Handling and Recovery.
  - Category 11: Agentic Patterns.
  - Category 12: Observable Development.
- Replace placeholder GitHub Releases wording with exact v0.2 release asset links after the release is published.
- Create a v0.3 validation path that tests behavior in a real or isolated repo without reintroducing a bulky raw `experiments/` tree into this repo.
- Build the onboarding skill and public documentation after the core repo workflow stabilizes.

## Parking Lot

- Consider a separate starter repo only if release ZIP install friction remains high.
- Consider CLI tooling after the markdown framework proves stable.
- Consider cross-project personalization only when there is a real user-level memory mechanism.
- Consider multi-agent orchestration after the single-agent loop is strong.
- Consider an external evaluation lab or benchmark repo so validation artifacts do not bloat this source repo.
