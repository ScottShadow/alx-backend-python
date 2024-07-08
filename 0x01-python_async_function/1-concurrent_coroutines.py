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
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)


async def wait_n1(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
