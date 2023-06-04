# Challenge 6: Combining CPU-bound tasks with asyncio (Modified)

# Prompt:

# Asyncio is generally used for I/O-bound tasks, but it can also be used to run CPU-bound tasks concurrently by offloading them to a thread or process pool. Let's see how you can do this.

# Create a script named challenge.py that accomplishes the following tasks:

# Create a function named compute that accepts an argument n (an integer). This function should not be a coroutine—it will be a normal, blocking function. The function should compute and return the nth Fibonacci number using a simple recursive algorithm.

# Please note that this algorithm is very inefficient (exponential time complexity) and will keep your CPU busy for considerable time when n is large.

# Create a coroutine named async_compute that accepts the same argument n. This coroutine should run the compute function using the run_in_executor method of the asyncio event loop, which will offload the computation to a separate thread.

# Create a main function named main, which will be your entry point. In this function, use asyncio to run three instances of async_compute concurrently, with n equal to 30, 32, and 34. The main function should print the results of the coroutines as they arrive, each one formatted as "Fibonacci result: <result>" (replace <result> with the actual Fibonacci number).
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor as Executor

def compute(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return compute(n - 1) + compute(n - 2)

async def async_compute(n: int, block: bool) -> int:
    executor = Executor()
    loop = asyncio.get_event_loop()
    if block:
        return compute(n)
    else:
        return await loop.run_in_executor(executor, compute, n)

async def main():
    nn = [32, 33, 34]
    t0 = time.time()
    await asyncio.gather(*(async_compute(n, False) for n in nn))
    t1 = time.time()
    print(f"Non-blocking: {t1 - t0:.2f}")

    t0 = time.time()
    await asyncio.gather(*(async_compute(n, True) for n in nn))
    t1 = time.time()
    print(f"Blocking: {t1 - t0:.2f}")

asyncio.run(main())
