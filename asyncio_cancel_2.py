#!/usr/bin/env uv run

import asyncio


async def f():
    task = asyncio.create_task(asyncio.sleep(7777))
    task.cancel()
    await task


asyncio.run(f())
