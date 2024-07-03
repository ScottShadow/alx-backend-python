#!/usr/bin/env python3
"""
Blind Typing
"""
# The types of the elements of the input are not know
from typing import List, Optional, TypeVar

T = TypeVar('T')  # Define a generic type variable


def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    A function that safely returns the first element of a list or None if the list is empty.

    Args:
        lst (List[T]): A list of elements of any type.

    Returns:
        Optional[T]: The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
