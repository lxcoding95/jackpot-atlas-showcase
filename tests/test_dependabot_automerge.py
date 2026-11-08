import unittest

from tools.enable_dependabot_patch_automerge import eligible


def pr(title, **overrides):
    value = {
        "author": {"login": "dependabot[bot]"},
        "baseRefName": "main",
        "headRefName": "dependabot/github_actions/actions/checkout-7.0.2",
        "isDraft": False,
        "title": title,
    }
    value.update(overrides)
    return value


class DependabotAutoMergeTests(unittest.TestCase):
    def test_accepts_patch_only_version_update(self):
        self.assertTrue(eligible(pr("Bump actions/checkout from 7.0.1 to 7.0.2")))

    def test_rejects_minor_major_sha_and_untrusted_prs(self):
        cases = [
            pr("Bump actions/checkout from 7.0.1 to 7.1.0"),
            pr("Bump actions/checkout from 7.0.1 to 8.0.0"),
            pr("Bump actions/checkout from abc123 to def456"),
            pr("Bump actions/checkout from 7.0.1 to 7.0.2", author={"login": "attacker"}),
            pr("Bump actions/checkout from 7.0.1 to 7.0.2", baseRefName="feature"),
            pr("Bump actions/checkout from 7.0.1 to 7.0.2", isDraft=True),
            pr("Bump actions/checkout from 7.0.2 to 7.0.1"),
        ]
        self.assertTrue(all(not eligible(item) for item in cases))


if __name__ == "__main__":
    unittest.main()
