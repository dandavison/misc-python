# Prompt:

# Create a script named challenge.py that accomplishes the following tasks:

# Create a coroutine named countdown that accepts two arguments: name (a string) and delay (an integer). The coroutine should enter a loop that runs delay number of times. In each iteration, it should print <name> count: <iteration> (replace <name> with the name argument and <iteration> with the current loop count, starting from 1), and then sleep for 1 second. When the loop completes, it should print <name> Done.

# Create a main function named main, which will be your entry point. In this function, create two tasks that run countdown concurrently, with arguments ("Task A", 5) and ("Task B", 3). Then, wait for 4 seconds, and cancel the remaining task (which should be "Task A").

import asyncio

async def countdown(name: str, delay: int):
    i = 1
    while i <= delay:
        print(f"{name} count: {i}")
        i += 1
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            print(f"{name} was canceled!")
            return
    print(f"{name} Done")


async def main():
    tasks = [asyncio.create_task(countdown(name, delay), name=name)
             for name, delay in [("Task A", 5), ("Task B", 3)]]
    await asyncio.sleep(4)
    [remaining_task] = [task for task in tasks if not task.done()]
    remaining_task.cancel()

asyncio.run(main())
