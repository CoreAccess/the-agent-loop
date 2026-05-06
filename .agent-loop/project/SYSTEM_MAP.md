# Project System Map

Status: accepted

## Purpose

Map the active systems in this repository so future work can load only the context needed for the current goal.

## Systems

### Project Operations

Function:

- Run this repository through The Agent Loop v0.2 while building v0.3.
- Own active intent, roadmap, active goal, observations, logs, and handoff.

Details:

- `.agent-loop/START.md`
- `.agent-loop/project/INTENT.md`
- `.agent-loop/project/ACTIVE_GOAL.md`
- `.agent-loop/project/ROADMAP.md`
- `.agent-loop/project/OBSERVATIONS.md`
- `.agent-loop/project/systems/project-operations.md`

### Release Packages

Function:

- Store frozen release source folders used to build uploaded GitHub Release assets.

Details:

- `releases/v0.1/`
- `releases/v0.2/`
- `.agent-loop/project/systems/release-packages.md`

### Research And Evidence

Function:

- Preserve source-backed research, case studies, and distilled validation lessons that inform framework decisions.

Details:

- `docs/research/`
- `docs/case-studies/`
- `.agent-loop/project/systems/research-and-evidence.md`

### Public Surface

Function:

- Explain the project and current install path to users.

Details:

- `README.md`
- GitHub Releases
- `.agent-loop/project/systems/public-surface.md`

### Local Agent Configuration

Function:

- Hold ignored local agent skills and settings for this checkout.

Details:

- `.agents/`
- `.gitignore`

## Current Constraints

- v0.2 release artifacts are frozen as the current finished release.
- v0.1 release artifacts are frozen as historical baseline.
- Generated release ZIP files should not be tracked in git.
- Root state files from the pre-v0.2 model should not be recreated.
- Raw experiment capsules should stay out of the active repo after their lessons are distilled.
