# Create a script named challenge.py that accomplishes the following tasks:

# Create a coroutine named raise_error_after that accepts an argument delay (an integer). The coroutine should sleep for delay seconds, then raise a RuntimeError with the message "An error has occurred after <delay> seconds!" (replace <delay> with the actual delay).

# Create a main function named main, which will be your entry point. In this function, use asyncio to run three instances of raise_error_after concurrently, with delays of 1, 2, and 3 seconds. Use asyncio.gather and set return_exceptions=True to ensure that all coroutines run even if some of them raise exceptions.

# The main function should print the exceptions raised by the coroutines, each one formatted as "Exception caught: <exception>" (replace <exception> with the actual exception).
import asyncio

async def raise_error_after(delay: int):
    await asyncio.sleep(delay)
    raise RuntimeError(f"An error has occurred after {delay} seconds!")

async def main():
    exceptions = await asyncio.gather(raise_error_after(1),
                                 raise_error_after(2),
                                 raise_error_after(3),
                                 return_exceptions=True)
    for exc in exceptions:
        print(f"Exception caught: {exc}")

asyncio.run(main())
