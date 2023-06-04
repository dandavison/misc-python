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
