#!/usr/bin/env python3
"""
    Calculate the sum of all the elements in the input list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all the elements in the input list.

    Parameters:
        input_list (List[float]): The list of floats to be summed.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return float(sum(input_list))
