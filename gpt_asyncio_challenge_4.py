# Prompt:

# Create a script named challenge.py that accomplishes the following tasks:

# Create a coroutine named maybe_raise_error that accepts an argument delay (an integer). The coroutine should sleep for delay seconds, then if delay is divisible by 2, it should return the string "No error after <delay> seconds!". However, if delay is not divisible by 2, it should raise a RuntimeError with the message "An error has occurred after <delay> seconds!" (replace <delay> with the actual delay).

# Create a main function named main, which will be your entry point. In this function, use asyncio to run four instances of maybe_raise_error concurrently, with delays of 1, 2, 3, and 4 seconds. Use asyncio.gather and set return_exceptions=True to ensure that all coroutines run even if some of them raise exceptions.

# The main function should print the results of the coroutines. If a coroutine raised an exception, it should print "Exception caught: <exception>" (replace <exception> with the actual exception). If a coroutine returned a string, it should print "Coroutine returned: <result>" (replace <result> with the actual string).
import asyncio

async def maybe_raise_error(delay: int):
    await asyncio.sleep(delay)
    if delay % 2 == 0:
        return f"No error after {delay} seconds!"
    else:
        raise RuntimeError(f"An error has occurred after {delay} seconds!")

async def main():
    vals = await asyncio.gather(*(maybe_raise_error(t) for t in [1, 2, 3, 4]), return_exceptions=True)
    for val in vals:
        if type(val) == str:
            print(f"Coroutine returned: {val}")
        else:
            print(f"Exception caught: {val}")


asyncio.run(main())
