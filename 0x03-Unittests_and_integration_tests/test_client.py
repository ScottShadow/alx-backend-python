#!/usr/bin/python3
"""
Parameterized Unit testing
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, test_org, mock_get):
        """Test org"""
        ORG_URL = f"https://api.github.com/orgs/{test_org}"

        myobj = GithubOrgClient(test_org)
        myobj.org()
        mock_get.assert_called_once_with(ORG_URL)

    def test_public_repos_url(self):
        pass


if __name__ == "__main__":
    unittest.main()
