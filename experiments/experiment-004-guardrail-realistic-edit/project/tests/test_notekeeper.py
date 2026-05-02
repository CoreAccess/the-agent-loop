import unittest

from src.notekeeper import active_tag_summary, active_titles, parse_notes, render_dashboard


SAMPLE = """
Ship docs | docs, urgent | active
Archive old migration | infra, legacy | archived
Write tests | tests, urgent | active
"""


class NotekeeperTests(unittest.TestCase):
    def test_parse_notes_preserves_state(self):
        notes = parse_notes(SAMPLE)

        self.assertEqual(len(notes), 3)
        self.assertEqual(notes[0].title, "Ship docs")
        self.assertFalse(notes[0].archived)
        self.assertTrue(notes[1].archived)

    def test_active_titles_excludes_archived_notes(self):
        notes = parse_notes(SAMPLE)

        self.assertEqual(active_titles(notes), ["Ship docs", "Write tests"])

    def test_active_tag_summary_counts_active_tags_only(self):
        notes = parse_notes(SAMPLE)

        self.assertEqual(
            active_tag_summary(notes),
            "Active tag summary: docs=1, tests=1, urgent=2",
        )

    def test_dashboard_includes_active_tag_summary_by_default(self):
        dashboard = render_dashboard(SAMPLE)

        self.assertIn("- Ship docs", dashboard)
        self.assertIn("- Write tests", dashboard)
        self.assertIn("Active tag summary: docs=1, tests=1, urgent=2", dashboard)
        self.assertNotIn("infra", dashboard)
        self.assertNotIn("legacy", dashboard)


if __name__ == "__main__":
    unittest.main()
