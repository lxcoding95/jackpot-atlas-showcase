import unittest
from tools.check_public_scope import check_scope, expected_paths, tracked_paths


class PublicScopeTests(unittest.TestCase):
    def test_tracked_paths_match_allowlist(self):
        self.assertEqual(set(), set(check_scope()))

    def test_manifest_has_no_untracked_or_unlisted_paths(self):
        self.assertEqual(expected_paths(), tracked_paths())


if __name__ == "__main__":
    unittest.main()
