from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Note:
    title: str
    tags: tuple[str, ...]
    archived: bool = False


def parse_notes(raw: str) -> list[Note]:
    notes: list[Note] = []

    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 3:
            raise ValueError(f"Invalid note line: {line}")

        title, raw_tags, raw_state = parts
        tags = tuple(tag.strip() for tag in raw_tags.split(",") if tag.strip())
        archived = raw_state.lower() == "archived"
        notes.append(Note(title=title, tags=tags, archived=archived))

    return notes


def active_titles(notes: list[Note]) -> list[str]:
    return [note.title for note in notes if not note.archived]


def active_tag_summary(notes: list[Note]) -> str:
    counts = Counter(
        tag
        for note in notes
        if not note.archived
        for tag in note.tags
    )
    if not counts:
        return "Active tag summary: none"
    rendered = ", ".join(f"{tag}={counts[tag]}" for tag in sorted(counts))
    return f"Active tag summary: {rendered}"


def render_dashboard(raw: str) -> str:
    notes = parse_notes(raw)
    lines = ["Active notes:"]

    for title in active_titles(notes):
        lines.append(f"- {title}")

    lines.append(active_tag_summary(notes))

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a Notekeeper dashboard.")
    parser.add_argument("notes_file", help="Path to a pipe-delimited notes file.")
    args = parser.parse_args(argv)

    raw = Path(args.notes_file).read_text(encoding="utf-8")
    print(render_dashboard(raw))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
