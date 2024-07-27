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

    @parameterized.expand([
        # Test case where the org "google" is used
        # and the payload is "GOOGLE(list)"
        ("google", ["GOOGLE"],
         [{"name": "GOOGLE"}]),
        # Test case where the org "random_url" is used
        # and the payload is "RANDO(list)"
        ('random_url', ["RANDO"],
         [{"name": "RANDO"}])
    ])
    @patch("client.get_json")
    def test_public_repos(self, test_org, payload, json_payload, mock_get):
        """
        Test the public repos method of the GithubOrgClient class.

        This test case checks if the public repos method of
        GithubOrgClient class returns the correct value based on the
        payload returned from the _public_repos_url property and
        the get_json function.

        Args:
            test_org (str): The name of the organization.
            payload (list): A list containing the expected payload.
            json_payload (list): A list containing the JSON payload.
            mock_get (MagicMock): A mock object for the get_json function.

        Returns:
            None
        """
        # Mock the _public_repos_url property
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_pr:
            mock_pr.return_value = payload
            # Mock the get_json function
            mock_get.return_value = json_payload

            # Call the public_repos method
            res = GithubOrgClient(test_org).public_repos()
            # Assert that the returned value is equal to the payload
            self.assertEqual(res, payload)
            # Assert that the _public_repos_url property was called once
            mock_pr.assert_called_once()
            # Assert that the get_json function was called once
            mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
