#!/usr/bin/env python3
"""
Parameterized Unit testing
"""
import unittest
from unittest.mock import patch, PropertyMock
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
        myurl = f"https://api.github.com/orgs/{test_org}"

        client = GithubOrgClient(test_org)
        client.org()
        mock_get.assert_called_once_with(myurl)

    @parameterized.expand([
        # Test case where the org "google" is used
        # and the payload has a key "repos_url"
        ("google", {"repos_url": "https://api.github.com/orgs/"}),
        # Test case where the org "random_url" is used
        # and the payload has a key "repos_url"
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, test_org, payload, mock_org):
        """
        Test the public repos url property of the GithubOrgClient class.

        This test case checks if the public repos url property of
        GithubOrgClient class returns the correct value based on the
        payload returned from the org property.

        Args:
            test_org (str): The name of the organization.
            payload (dict): A dictionary containing test data.
            mock_org (PropertyMock): A mock object for the org property.

        Returns:
            None
        """
        # Set the return value of the mock_org object to the payload
        mock_org.return_value = payload

        # Create an instance of GithubOrgClient class with the test org
        client = GithubOrgClient(test_org)
        # Get the value of the public repos url property
        res = client._public_repos_url

        # Assert that the value of the public repos url property is
        # equal to the value of the "repos_url" key in the payload
        self.assertEqual(res, payload.get("repos_url"))
        # Assert that the org property was called once
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
