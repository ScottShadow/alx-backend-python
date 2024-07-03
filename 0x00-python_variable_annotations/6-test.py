#!/usr/bin/env python3
import unittest
from typing import List, Union
sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list


class TestSumMixedList(unittest.TestCase):
    def test_empty_list(self):
        """
        Test that the sum of an empty list is 0.
        """
        input_list = []
        expected_sum = 0
        self.assertEqual(sum_mixed_list(input_list), expected_sum)

    def test_list_of_integers(self):
        """
        Test that the sum of a list of integers is correct.
        """
        input_list = [1, 2, 3, 4, 5]
        expected_sum = 15
        self.assertEqual(sum_mixed_list(input_list), expected_sum)

    def test_list_of_floats(self):
        """
        Test that the sum of a list of floats is correct.
        """
        input_list = [1.5, 2.5, 3.5, 4.5, 5.5]
        expected_sum = 17.5
        self.assertEqual(sum_mixed_list(input_list), expected_sum)

    def test_list_of_mixed_types(self):
        """
        Test that the sum of a list of mixed types is correct.
        """
        input_list = [1, 2.5, 3, 4.5, 5]
        expected_sum = 16
        self.assertEqual(sum_mixed_list(input_list), expected_sum)


if __name__ == '__main__':
    unittest.main()
