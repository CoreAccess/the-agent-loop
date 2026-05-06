# Release Packages System

Status: accepted

## Function

Store the framework release source folders that are packaged into GitHub Release ZIP assets.

## Owned Files

- `releases/v0.1/.agent-loop/`
- `releases/v0.2/.agent-loop/`
- Future release candidates under `releases/v0.3/.agent-loop/` when intentionally created.

## Rules

- v0.1 is frozen as historical baseline.
- v0.2 is frozen as the current finished release.
- Root `.agent-loop/` is the live v0.3 development workspace for this repository. It may be edited while building v0.3 because the frozen v0.2 baseline lives under `releases/v0.2/.agent-loop/`.
- Do not create `releases/v0.3/` as the day-to-day working copy. Create it only when packaging a v0.3 release candidate by copying/sanitizing the accepted root `.agent-loop/` scaffold.
- Never mutate `releases/v0.2/.agent-loop/` for normal v0.3 work.
- Generated release ZIP files should not be tracked in git.
- Uploaded release ZIP assets should contain only `.agent-loop/` entries, not this repository's source archive, docs, raw experiments, memory, or root files.
