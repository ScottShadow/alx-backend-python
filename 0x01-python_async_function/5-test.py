#!/usr/bin/env python3
"""
This module contains a function that tests the execution of coroutines
"""
import asyncio


async def main():
    """
    This function tests the execution of coroutines
    """
    loop = asyncio.get_running_loop()
    print(loop)

asyncio.run(main())
