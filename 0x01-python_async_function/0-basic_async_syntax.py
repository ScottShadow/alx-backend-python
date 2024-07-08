#!/usr/bin/env python3
"""
This module contains a function that waits for a random amount of time
between 0 and max_delay and returns the time elapsed
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random amount of time between 0 and max_delay
    and returns the time elapsed
    Args:
        max_delay (int): The maximum delay in seconds
    Returns:
        float: The time elapsed
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
