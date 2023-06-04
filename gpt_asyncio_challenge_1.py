# Create a coroutine named async_hello_world that will print "Hello, World!" after a delay of 2 seconds.

# Create a coroutine named async_bye_world that will print "Bye, World!" after a delay of 1 second.

# Create a main function named main, which will be your entry point. In this function, use asyncio to run both async_hello_world and async_bye_world concurrently. Ensure that they both finish before main ends.
import asyncio

async def async_hello_world():
    await asyncio.sleep(2)
    print("Hello, World!")

async def async_bye_world():
    await asyncio.sleep(1)
    print("Bye, World!")


async def main():
    await asyncio.gather(async_hello_world(), async_bye_world())
    # For educational purposes, note that you could omit the await, and sleep afterwards,
    # and the stuff will be printed out:
    # asyncio.gather(async_hello_world(), async_bye_world())
    # asyncio.sleep(3)

asyncio.run(main())
