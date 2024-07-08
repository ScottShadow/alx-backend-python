#!/usr/bin/env python3
"""
This module contains a function that executes coroutines concurrently
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function waits for a random amount of time between 0 and max_delay
    and returns the time elapsed
    Args:
        n: number of times to call wait_random
        max_delay: max delay for wait_random
    Returns:
        list of delays
    """

    array = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        array.append(await task)
    array.sort()
    return array
