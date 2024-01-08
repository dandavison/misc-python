import asyncio


async def gen():
    for i in [1, 2, 3]:
        yield i


async def consume():
    async for i in gen():
        print(i)


async def first():
    print(await anext(gen()))


asyncio.run(first())
