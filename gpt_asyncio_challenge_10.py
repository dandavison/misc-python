# Challenge 10: Producer/Consumer with asyncio

# Prompt:

# In this challenge, you're going to implement a producer/consumer system using asyncio.

# Here's what you'll do:

# Create an asyncio Queue with a maximum size of 5. This will be used to store the items produced by the producer. The maximum size implies that the producer has to wait if the queue is full.

# Create a producer coroutine which will produce items and put them in the queue. The producer will produce a total of 20 items. Each item is simply an integer (starting from 1). After producing an item, the producer should sleep for 1 second to simulate the time it takes to produce the item.

# Create a consumer coroutine which will consume items from the queue. The consumer will consume items as long as the producer is still producing or there are items left in the queue. After consuming an item, the consumer should sleep for 2 seconds to simulate the time it takes to consume the item. The consumer should print the item it consumed.

# In the main function, create a task for the producer and a task for the consumer, and run them concurrently.

# Test Case:

# When running python challenge.py, the output should show the consumer consuming 20 items, one at a time. Since the consumer sleeps for 2 seconds after consuming an item and the producer sleeps for 1 second after producing an item, you should see that the producer is waiting when the queue is full and the consumer is waiting when the queue is empty.
import asyncio

DONE_SENTINEL = None

async def producer(queue: asyncio.Queue):
    for item in range(1, 20 + 1):
        await queue.put(item)
        print(f"Put: {item}")
        await asyncio.sleep(1)
    await queue.put(DONE_SENTINEL)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item == DONE_SENTINEL:
            return
        print(f"Consumed: {item}")


async def main():
    queue = asyncio.Queue(maxsize=5)
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await producer_task
    await consumer_task

asyncio.run(main())
