# Challenge 9: Distributed Counter with asyncio

# Prompt:

# In this challenge, let's design a distributed system where each node in the system has to fetch a unique integer that was never fetched before.

# Let's keep it simple by simulating the distributed system on a single machine. We'll use asyncio to simulate multiple nodes working concurrently. Here's what you'll do:

# Create an AtomicCounter class with the following methods:

# __init__(self): Initialize the counter to 0.
# increment_and_get(self): Atomically increment the counter by 1 and return the new value.
# Create an async function node_work that simulates the work of a node in the distributed system:

# Each node should use the AtomicCounter to fetch a unique integer.
# To simulate work, the node should sleep for a random time between 0 and 2 seconds before fetching the unique integer.
# The function should print the node name and the fetched integer.
# In your main function, create an instance of AtomicCounter and simulate 100 nodes working concurrently.

# Test Case:

# When running python challenge.py, the output should show 100 lines, each line showing a node name and a unique integer. The integers should be from 1 to 100, each appearing exactly once.

import asyncio
from random import random

class AtomicInteger:
    def __init__(self) -> None:
        self.val = 0
        self.mutex = asyncio.Lock()

    async def increment_and_get(self) -> int:
       async with self.mutex:
            self.val += 1
            return self.val

atomic_integer = AtomicInteger()

async def node_work(label: int):
    await asyncio.sleep(random() * 2)
    val = await atomic_integer.increment_and_get()
    print(f"Node {label}: {val}")

async def main():
    await asyncio.gather(*(node_work(i) for i in range(100)))

asyncio.run(main())
