#!/usr/bin/env python3
"""
This module contains a function that creates a list of
 tasks for a coroutine
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function creates a list of tasks for a coroutine
    Args:
        n (int): The number of times to call wait_random
        max_delay (int): The maximum delay for each coroutine
    Returns:
        List[float]: The sorted list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    time_array = await asyncio.gather(*tasks)
    time_array.sort()
    return time_array
