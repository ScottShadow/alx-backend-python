#!/usr/bin/python3
"""
Parameterized Unit testing
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
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


if __name__ == "__main__":
    unittest.main()
