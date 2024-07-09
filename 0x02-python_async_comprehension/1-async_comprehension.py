#!/usr/bin/env python3
"""
    This module contains the async_comprehension function
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        This function returns a list of 10 random numbers
        Async generator is used to generate the numbers
    Arguments:
        None
    Returns:
        list: A list of 10 random numbers
    """
    res = []
    async for i in async_generator():
        res.append(i)
    return res
