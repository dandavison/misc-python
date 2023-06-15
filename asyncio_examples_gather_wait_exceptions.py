import asyncio

async def coro(i: int) -> int:
    assert i, "deliberate error"
    return i


async def main():
    res0 = await coro(0)
    res1 = await coro(1)
    return [res0, res1]


async def main_gather():
    coro0 = coro(0)
    coro1 = coro(1)

    # results = await asyncio.gather(*[coro0, coro1])
    # raises:
    # AssertionError: deliberate error

    results = await asyncio.gather(*[coro0, coro1], return_exceptions=True)
    print(results)
    # [AssertionError('deliberate error'), 1]


async def main_wait():
    coro0 = coro(0)
    coro1 = coro(1)

    done, pending = await asyncio.wait([asyncio.create_task(coro0),
                                        asyncio.create_task(coro1)])

    assert not pending
    print([task.exception() for task in done])
    # [AssertionError('deliberate error'), None]

asyncio.run(main_wait())
# asyncio.run(main_gather())
