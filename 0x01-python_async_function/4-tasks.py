#!/usr/bin/env python3
"""
This module contains a function that creates a list of tasks for a coroutine
"""
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function creates a list of tasks for a coroutine
    Args:
        n (int): The number of times to call wait_random
        max_delay (int): The maximum delay for each coroutine
    Returns:
        List[float]: The list of delays
    """
    array = []
    for _ in range(n):
        array.append(await task_wait_random(max_delay))
    array.sort()
    return array
