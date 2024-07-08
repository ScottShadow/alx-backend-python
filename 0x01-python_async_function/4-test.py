#! /usr/bin/env python3
import asyncio


async def coro1():
    print("Coro1: Start")
    asyncio.sleep(3)
    print("Coro1: End")


async def coro2():
    print("Coro2: Start")
    asyncio.sleep(1)
    print("Coro2: End")


async def main():
    task1 = asyncio.create_task(coro1())
    task2 = asyncio.create_task(coro2())

    await task1
    await task2

asyncio.run(main())
