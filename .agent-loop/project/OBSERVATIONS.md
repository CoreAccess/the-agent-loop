# Project Observations

Status: initialized

## Active

- Local shell is PowerShell on Windows.
- Before recursive delete or move operations, verify resolved absolute target paths are inside `C:\Users\adamd\Downloads\Programming\the-agent-loop`.
- Git remote `origin` points to `https://github.com/CoreAccess/the-agent-loop.git`; `main` tracks `origin/main`.
- `gh` was not installed during the v0.2 README publish flow, so direct git push was used instead of a GitHub CLI PR workflow.
- v0.3 is locked as the finished active release source in `releases/v0.3/.agent-loop/`. Do not edit or change it unless the owner explicitly unlocks that release source.
- Future scaffold/product changes should target the mutable root `.agent-loop/` workspace unless the owner explicitly approves a critical release packaging correction.
- Release ZIP assets should be generated/uploaded outside git. If a ZIP is built for release, it should contain only `.agent-loop/` entries.

## Resolved

- v0.1 remains frozen as a historical baseline.
- Root `AGENTS.md` is now a small adapter that loads `.agent-loop/START.md`.
