import asyncio
from datetime import datetime


start_time = datetime.now()

def start_clock():
    global start_time
    start_time = datetime.now()
    log("start")

def log(msg: str):
    time = (datetime.now() - start_time).total_seconds()
    print(f"{time:.1f} {msg}")

async def say_after(seconds: float, what: str):
    await asyncio.sleep(seconds)
    log(what)

async def sequential_execution_of_coroutines():
    start_clock()
    await say_after(1, "after 1 sec")
    await say_after(2, "after 2 sec")

async def concurrent_execution_of_tasks():
    start_clock()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "after 1 sec"))
        tg.create_task(say_after(2, "after 2 sec"))

async def main():
    await sequential_execution_of_coroutines()
    print()
    await concurrent_execution_of_tasks()

asyncio.run(main())
