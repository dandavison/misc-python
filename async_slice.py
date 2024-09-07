import itertools
import asyncio
from typing import AsyncIterator


async def aslice(it: AsyncIterator, n: int):
    i = 0
    async for el in it:
        if i == n:
            raise StopAsyncIteration
        i+=1
        yield el

async def acount():
    for i in itertools.count():
        yield i


async def main():
    return [x async for x in aslice(acount(), 10)]


print(asyncio.run(main()))