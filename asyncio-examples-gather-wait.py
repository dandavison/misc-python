import asyncio

async def coro(i: int) -> int:
    return i


async def main():
    res0 = await coro(0)
    res1 = await coro(1)
    return [res0, res1]


async def main_gather():
    coro0 = coro(0)
    coro1 = coro(1)

    print(await asyncio.gather(*[coro0, coro1]))

async def main_wait():
    coro0 = coro(0)
    coro1 = coro(1)

    done, pending = await asyncio.wait([asyncio.create_task(coro0),
                                        asyncio.create_task(coro1)])

    for task in done:
        print(task.result())

# gather
asyncio.run(main_gather())

# wait
asyncio.run(main_wait())
