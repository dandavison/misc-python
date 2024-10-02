import asyncio

lock = asyncio.Lock()


async def afn():
    print("before acquire")
    await asyncio.sleep(1)
    await lock.acquire()
    print("after acquire")


async def main():
    task = asyncio.create_task(afn())
    await lock.acquire()
    task.cancel()
    await task


asyncio.run(main())
