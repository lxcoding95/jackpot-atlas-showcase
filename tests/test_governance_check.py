import unittest
from unittest.mock import patch
from tools.check_governance import verify


class GovernanceCheckTests(unittest.TestCase):
    def test_detects_disabled_auto_merge_and_missing_ruleset(self):
        with patch("tools.check_governance.get", side_effect=[
            {"visibility": "public", "default_branch": "main", "has_issues": True, "allow_auto_merge": False, "delete_branch_on_merge": True, "archived": False}, []
        ]):
            problems = verify("owner/repo")
        self.assertIn("auto-merge is disabled", problems)
        self.assertIn("main-governance ruleset is missing", problems)


if __name__ == "__main__":
    unittest.main()
