#!/usr/bin/env python3
"""
This module contains a function that creates a task for a coroutine
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates a task for a coroutine
    Args:
        max_delay (int): The maximum delay for the coroutine
    Returns:
        asyncio.Task: The task for the coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
