#!/usr/bin/env python3
"""
    This module contains the measure_runtime function
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        This function measures the runtime of the async_comprehension
        function
    Arguments:
        None
    Returns:
        float: The time it takes to generate a list of 4 lists of 10
        random numbers
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.time()
    return end - start
