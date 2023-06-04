# Challenge 8: Limiting concurrency with asyncio

# Prompt:

# In this challenge, you'll create a script that demonstrates how to limit the number of concurrent tasks using asyncio.

# Here are the steps:

# Create a coroutine called worker that takes an integer i as an argument, waits for i seconds, then prints "Finished work {i}".

# Create a coroutine called main that does the following:

# Sets up a list of worker tasks for each integer from 1 to 10.
# Runs these tasks with asyncio, but ensures that no more than 5 tasks are running concurrently.
# Test Case:

# When running python challenge.py, the output should show that no more than 5 tasks are started concurrently, meaning that the total execution time should be approximately 15 seconds.

import asyncio
from collections import deque
from time import time

MAX_IN_FLIGHT = 5

async def worker(i: int):
    await asyncio.sleep(i)
    print(f"Finished work {i}")

async def main():
    inputs = deque(range(1, 10 + 1))
    tasks = set()
    while inputs or tasks:
        while inputs and len(tasks) < MAX_IN_FLIGHT:
            tasks.add(asyncio.create_task(worker(inputs.popleft())))
        _, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

t0= time()
asyncio.run(main())
t1 = time()
print(f"{t1 - t0:.2f}")
