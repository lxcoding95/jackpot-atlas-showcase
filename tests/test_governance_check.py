import unittest
from unittest.mock import patch
from tools.check_governance import verify


class GovernanceCheckTests(unittest.TestCase):
    def test_checks_visible_controls_without_guessing_admin_only_settings(self):
        with patch("tools.check_governance.get", side_effect=[
            {"visibility": "public", "default_branch": "main", "has_issues": True, "allow_auto_merge": False, "delete_branch_on_merge": False, "archived": False}, []
        ]):
            problems = verify("owner/repo")
        self.assertNotIn("auto-merge is disabled", problems)
        self.assertNotIn("head-branch cleanup is disabled", problems)
        self.assertIn("main-governance ruleset is missing", problems)



    def test_community_surfaces_are_checked_when_github_explicitly_disables_them(self):
        with patch("tools.check_governance.get", side_effect=[
            {"visibility": "public", "default_branch": "main", "has_issues": True,
             "has_wiki": False, "has_discussions": False, "archived": False},
            []
        ]):
            problems = verify("owner/repo")
        self.assertIn("Wiki is disabled", problems)
        self.assertIn("Discussions are disabled", problems)

if __name__ == "__main__":
    unittest.main()
