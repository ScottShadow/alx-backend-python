#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of executing
concurrent coroutines
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total runtime of calling wait_n n times
    with max_delay
    Args:
        n (int): The number of times to call wait_n
        max_delay (int): The maximum delay for each coroutine
    Returns:
        float: The average runtime per call
    """
    start_time = time.time()
    # time_array = asyncio.run(wait_n(n, max_delay))
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    # real_time = sum(time_array)
    total_time = end_time - start_time
    # print(real_time)
    return total_time / n
