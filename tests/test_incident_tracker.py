import unittest
from unittest.mock import patch
from tools.scan_recent_runs import reconcile


class IncidentTrackerTests(unittest.TestCase):
    def test_only_closes_on_success_for_current_main_sha(self):
        issue = {"title": "Automation incident: CI", "number": 7, "body": "failed"}
        with patch("tools.scan_recent_runs.api", side_effect=[
            {"default_branch": "main"}, {"sha": "current"},
            {"workflows": [{"name": name, "id": n, "state": "active"} for n, name in enumerate(("CI", "CodeQL", "Workflow security", "Governance drift", "Automation incident tracker"), 1)]},
            [issue],
            {"workflow_runs": [{"status": "completed", "conclusion": "success", "head_sha": "old", "html_url": "https://example.test/old"}]},
            *[{"workflow_runs": [{"status": "completed", "conclusion": "success", "head_sha": "current"}]} for _ in range(4)],
        ]) as mock_api:
            failures = reconcile("owner/repo")
        self.assertEqual([], failures)
        self.assertFalse(any(call.args[0] == "PATCH" for call in mock_api.call_args_list))


if __name__ == "__main__":
    unittest.main()
