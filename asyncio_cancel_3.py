# https://sailor.li/asyncio
import asyncio

event = asyncio.Event()


async def fn():
    try:
        event.set()
        await asyncio.sleep(60)
    except:
        print("Caught exception")


async def main():
    task = asyncio.create_task(fn())
    await event.wait()
    task.cancel()
    print("requested cancel; sleeping")
    await asyncio.sleep(1)


asyncio.run(main())
