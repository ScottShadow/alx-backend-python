#!/usr/bin/env python3
"""
Parameterized Unit testing
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
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
        # payload with Options
        payload = [{"name": "Google"}, {"name": "TT"}]
        # Mock the get_json function
        mock_get.return_value = payload
        # Mock the _public_repos_url property
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_pr:
            mock_pr.return_value = payload

            # Call the public_repos method
            res = GithubOrgClient("test_org").public_repos()
            # Assert that the returned value is equal to the payload
            self.assertEqual(res, ["Google", "TT"])
            # Assert that the _public_repos_url property was called once
            mock_pr.assert_called_once()
            # Assert that the get_json function was called once
            mock_get.assert_called_once()

    @parameterized.expand([
        # Test case where the repo has the license with key "my_license"
        # and the expected result is True
        ({"license": {"key": "my_license"}}, "my_license", True),
        # Test case where the repo does not have the license with key
        # "my_license"
        # and the expected result is False
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, path, key, status):
        """
        Test the has_license method of the GithubOrgClient class.

        This test case checks if the has_license method of GithubOrgClient
        class
        returns the correct value based on the license key provided.

        Args:
            path (dict): The nested dictionary containing the license
            information.
            key (str): The license key to check.
            status (bool): The expected result of the has_license method.

        Returns:
            None
        """
        # Call the has_license method with a dummy URL and the license key
        res = GithubOrgClient("url").has_license(path, key)
        # Assert that the returned value is equal to the expected result
        self.assertEqual(res, status)


@parameterized_class(["org_payload", "repos_payload", "expected_repos",
                      "apache2_repos"], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get", side_effect=[
                                cls.org_payload, cls.repos_payload])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos """

    def test_public_repos_with_license(self):
        """test public with license"""


if __name__ == "__main__":
    unittest.main()
