import asyncio


async def afn(name: str, leaf: bool):
    if not leaf:
        asyncio.create_task(afn("leaf", leaf=True))

    print(f"name: {name} before sleep")
    try:
        await asyncio.sleep(0.2)
    except asyncio.CancelledError:
        print(f"name: {name} caught CancelledError; re-raising")
        raise
    finally:
        print(f"name: {name} exiting")


async def main():
    task = asyncio.create_task(afn("primary", leaf=False))

    await asyncio.sleep(0.1)

    task.cancel()
    # task.get_coro().throw(asyncio.CancelledError("I cancelled it via lower level API"))
    await asyncio.sleep(777)
    try:
        await task
    except asyncio.CancelledError as exc:
        print(f"main(): task cancelled: {exc}")
    else:
        print("main(): task not cancelled")


asyncio.run(main())
