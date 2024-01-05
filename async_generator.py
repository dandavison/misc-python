import asyncio


async def g():
    for i in [1, 2, 3]:
        yield i


async def h():
    xxx = [i async for i in g()]
    print(xxx)


asyncio.run(h())
