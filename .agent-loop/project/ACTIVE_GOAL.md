# Active Goal

Status: completed

Owner approval: accepted in chat on 2026-05-06.

## Parent

- Intent: Self-apply The Agent Loop v0.2 to build v0.3.
- System: Research And Evidence; Release Packages.
- Milestone: v0.2 self-application follow-up cleanup.

## Outcome

Clean up release ZIP tracking and add a navigable docs structure that matches the v0.2 research/evidence model.

## Done When

- [x] `.gitignore` ignores generated release ZIP files.
- [x] Tracked release ZIP files are removed from git while release source folders remain.
- [x] Project state no longer treats ZIP files as tracked release package source.
- [x] `docs/` has an entry-point README and indexes for research and case studies.
- [x] Category research folders that already exist have lightweight indexes.
- [x] Handoff/log state is updated for the next v0.3 planning step.

## Scope

In scope:

- `.gitignore`
- `README.md`
- `.agent-loop/project/`
- `docs/`
- Removing tracked `releases/**/*.zip`

Out of scope:

- Editing frozen release source folders under `releases/v0.1/.agent-loop/` or `releases/v0.2/.agent-loop/`.
- Rewriting source-backed research content.
- Publishing GitHub Releases or uploading replacement ZIP assets.

## Stop Conditions

- A docs move would break useful source references without a clear replacement.
- A cleanup would alter frozen release source folders.
- Git shows unrelated user changes.

## Verification

```text
git status -sb
git diff --check
git ls-files "releases/*.zip" "releases/**/*.zip"
Get-ChildItem -Recurse -Filter *.zip releases
rg -n "v0[.]2[.]zip|v0[.]1[.]zip" README.md .agent-loop docs
```
