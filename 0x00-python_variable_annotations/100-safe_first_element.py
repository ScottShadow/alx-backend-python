#!/usr/bin/env python3
"""
Blind Typing
"""
# The types of the elements of the input are not know
from typing import Any, List, Optional


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it is not empty, 
    otherwise returns None.

    Args:
        lst (List[Any]): The input list.

    Returns:
        Optional[Any]: The first element of the list if it is not 
        empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
