import asyncio


async def foo():
    task = asyncio.current_task()
    assert task
    print(f"in foo task = {task.get_name()}")
    await bar()


async def bar():
    task = asyncio.current_task()
    assert task
    print(f"in bar before yield task = {task.get_name()}")
    await asyncio.sleep(1)
    task = asyncio.current_task()
    assert task
    print(f"in bar after yield task = {task.get_name()}")


asyncio.run(foo())
