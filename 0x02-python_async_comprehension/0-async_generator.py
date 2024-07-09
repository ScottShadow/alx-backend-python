#!/usr/bin/env python3
"""
    This module contains the async_generator function
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        This function returns a generator of 10 random numbers
    Args:
        None
    Returns:
        Generator[float, None, None]: A generator of 10 random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
