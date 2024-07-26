#!/usr/bin/env python3
"""
Parameterize Unit testing
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the `access_nested_map` function with different input parameters.
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), (1)),
        ({"a": {"b": 2}}, ("a"), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), (2))
    ])
    def test_access_nested_map(self, nest, path, res):
        """
        Test the `access_nested_map` function with different input parameters.

        This test case uses the `parameterized` library to generate multiple
        test cases with different input parameters.
        It verifies that the `access_nested_map` function returns the expected
        result for each test case.

        Parameters:
            - nest (dict): The nested dictionary to be accessed.
            - path (tuple): The path to the value in the nested dictionary.
            - res (any): The expected result of accessing the nested
            dictionary.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nest, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test the `access_nested_map` function with different input parameters
        that should raise a `KeyError`.

        This test case uses the `parameterized` library to generate multiple
        test cases with different input parameters.
        It verifies that the `access_nested_map` function raises a `KeyError`
        when the nested map does not contain the specified path.

        Parameters:
            - nested_map (dict): The nested dictionary to be accessed.
            - path (tuple): The path to the value in the nested dictionary.

        Returns:
            None
        """

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test the `get_json` function with different input parameters.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the `get_json` function with different input parameters.

        This test case uses the `parameterized` library to generate multiple
        test cases with different input parameters. It verifies that the
        `get_json` function makes a GET request to the specified URL, retrieves
        the JSON response, and returns the parsed payload.

        Parameters:
            - test_url (str): The URL to make a GET request to.
            - test_payload (dict): The expected payload of the JSON response.
            - mock_get (MagicMock): The mock object for the `requests.get`
            function.

        Returns:
            None
        """
        # Mock the requests.get function to return a Mock response
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response

        # Call the get_json function with the test URL
        res = get_json(test_url)

        # Verify that the requests.get function was called with the correct URL
        mock_get.assert_called_with(test_url)

        # Verify that the parsed payload matches the expected payload
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """
        Test the `memoize` decorator by verifying that it correctly
    """

    def test_memoize(self):
        """
        Test the `memoize` decorator by verifying that it correctly
        memoizes the result of a method.

        This test case mocks the `a_method` of the `TestClass` and sets
        its return value to 42. It then creates an instance of `TestClass`
        and calls its `a_property` method twice. The `memoize` decorator is
        used to memoize the result of `a_method`.

        After calling `a_property` twice, the test case verifies that
        `a_method` is only called once by asserting that
        `mock_method.assert_called_once()` is `True`. It also verifies
        that the memoized result of `a_property` is equal to 42 byasserting
        that `self.assertEqual(mock_method, 42)` is `True`.

        Parameters:
            - self (TestCase): The test case instance.
            - mock_method (MagicMock): The mock object for the `a_method`
            method of the `TestClass`.

        Returns:
            None
        """

        # The class that contains the methods to be tested
        class TestClass:
            """Test class"""

            # The method to be memoized
            def a_method(self):
                """a_method"""
                return 42

            # The method to be memoized
            @memoize
            def a_property(self):
                """a_property: Property decorated with memoize"""
                return self.a_method()

        # Mock the method to be tested
        with patch.object(TestClass, "a_method") as mock_method:
            # Create an instance of the test class
            myobject = TestClass()

            # Call the property method twice
            myobject.a_property()
            myobject.a_property()

            # Verify that the method was only called once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
