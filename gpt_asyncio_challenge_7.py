# Challenge 7: Graceful shutdown with asyncio

# Prompt:

# In real-world applications, it's often necessary to perform some cleanup tasks when your program is about to exit. This could be closing connections, saving data, freeing resources, etc. When you're using asyncio, you often have to stop your coroutines, too. But simply stopping the event loop can leave tasks in an unfinished state. That's why asyncio provides a way to cancel all tasks and then run them until they have finished cleaning up.

# Create a script named challenge.py that accomplishes the following tasks:

# Create a coroutine named long_running_task that sleeps for 5 seconds and then prints "Task finished".

# Create a main function named main, which will be your entry point. In this function, use asyncio to create and run an instance of long_running_task.

# In your main function, also add a mechanism to stop the event loop and cancel all tasks when it receives a SIGINT signal (which is sent when you press Ctrl+C). Before the program exits, it should print "Cleaning up".

# Test Case:

# You should be able to run this script from the command line using python challenge.py. The script should start running long_running_task, and if you let it run for 5 seconds, it should print "Task finished" and then exit.

# However, if you press Ctrl+C before the 5 seconds are up, the program should print "Cleaning up" and then exit. The "Task finished" message should not be printed if you cancel the program before the task has a chance to finish.
import asyncio

async def long_running_task():
    try:
        await asyncio.sleep(5)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task cancelled")

async def main():
    task = asyncio.create_task(long_running_task())
    res = await task
    print(res)
    print("Cleaning up")

asyncio.run(main())
