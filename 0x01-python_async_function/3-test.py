#!/usr/bin/env python3
import asyncio


async def set_after(future, delay, value):
    await asyncio.sleep(delay)
    future.set_result(value)


async def main():
    future = asyncio.Future()
    await set_after(future, 2, 'hello')
    print(future.result())

asyncio.run(main())
