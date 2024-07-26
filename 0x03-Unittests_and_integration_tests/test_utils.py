#!/usr/bin/env python3
"""
Parameterize Unit testing
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TESTING UTILS"""
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


if __name__ == "__main__":
    unittest.main()
