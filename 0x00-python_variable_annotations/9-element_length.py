#!/usr/bin/env python3
"""
    Calculate the length of each element in the given iterable.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given iterable.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples, where each tuple contains a sequence and its length.
    """
    # Use a list comprehension to iterate over the elements in the iterable.
    # For each element, create a tuple with the element itself and its length.
    return [(i, len(i)) for i in lst]
