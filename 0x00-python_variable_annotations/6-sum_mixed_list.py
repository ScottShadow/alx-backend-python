#!/usr/bin/env python3

"""
This module defines a function named `sum_mixed_list` tht calculates the sum of
elements in a list, where the list can contain both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of elements in a list.

    Args:
        mxd_lst  (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all the elements in the list.
    """
    return (float(sum(map(float, mxd_lst))))
