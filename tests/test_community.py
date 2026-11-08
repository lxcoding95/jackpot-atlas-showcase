"""Guard the public onboarding content without YAML or network dependencies."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = "lxcoding95/jackpot-atlas-showcase"


class CommunityDocumentationTests(unittest.TestCase):
    def test_wiki_entry_links_to_canonical_public_pages(self):
        text = (ROOT / "docs/WIKI_HOME.md").read_text(encoding="utf-8")
        self.assertIn("Engineering Showcase Wiki", text)
        self.assertIn(f"https://github.com/{OWNER}/actions", text)
        self.assertIn("github.com/lxcoding95/jackpot-atlas-showcase/blob/main/docs/AUTOMATION_OPERATING_MODEL.md", text)
        self.assertIn("private lottery research", text.lower())

    def test_discussion_forms_exist_and_have_a_required_input(self):
        for category in ("general", "ideas"):
            body = (ROOT / f".github/DISCUSSION_TEMPLATE/{category}.yml").read_text(encoding="utf-8")
            self.assertIn("body:", body)
            self.assertIn("type: textarea", body)
            self.assertIn("required: true", body)
            self.assertNotIn("lotteryresultsfeed", body.lower())

    def test_public_issue_chooser_routes_security_and_questions(self):
        chooser = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
        self.assertIn("blank_issues_enabled: false", chooser)
        self.assertIn(f"https://github.com/{OWNER}/discussions", chooser)
        self.assertIn(f"https://github.com/{OWNER}/security/policy", chooser)

    def test_docs_do_not_claim_placeholder_release_or_sponsors(self):
        text = (ROOT / "docs/AUTOMATION_OPERATING_MODEL.md").read_text(encoding="utf-8")
        self.assertIn("after **60 days**", text)
        self.assertIn("empty tabs are deliberate", text)
        self.assertIn("not** an independent human code review", text)
        funding = (ROOT / "docs/COMMUNITY_AND_SPONSORING.md").read_text(encoding="utf-8")
        self.assertIn("owner-verified", (text + funding).lower())
        self.assertFalse((ROOT / ".github/FUNDING.yml").exists(),
                         "Do not publish a guessed sponsor account before verification")

    def test_all_new_public_files_are_allowlisted(self):
        paths = set(json.loads((ROOT / "public-scope.json").read_text(encoding="utf-8"))["allowed_tracked_files"])
        for candidate in (".github/DISCUSSION_TEMPLATE/general.yml", ".github/DISCUSSION_TEMPLATE/ideas.yml",
                          ".github/ISSUE_TEMPLATE/config.yml", "docs/WIKI_HOME.md",
                          "docs/AUTOMATION_OPERATING_MODEL.md", "docs/COMMUNITY_AND_SPONSORING.md",
                          "docs/API_SOURCES_REVIEW_2026.md", "tests/test_community.py"):
            self.assertIn(candidate, paths)


if __name__ == "__main__":
    unittest.main()
