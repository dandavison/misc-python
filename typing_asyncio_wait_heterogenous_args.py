import asyncio
from typing import Any

from temporalio import workflow

fut = asyncio.Future[list[Any]]()


async def f() -> None:
    pass


task = asyncio.create_task(f())


async def g():
    done, _ = await workflow.wait([fut, task])
    for aw in done:
        await aw
