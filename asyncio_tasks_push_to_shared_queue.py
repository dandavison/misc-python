import asyncio

queue = asyncio.Queue()

async def run_worker(id: str):
    for item in [1, 2, 3, 4, 5]:
        await asyncio.sleep(0.5)
        await queue.put((id, item))
    await queue.put((id, None))

async def merge_worker_output_streams():
    workers = ["a", "b", "c"]
    async with asyncio.TaskGroup() as tg:
        for id in workers:
            tg.create_task(run_worker(id))

        done = 0
        while True:
            worker, item  = await queue.get()
            if item is None:
                done += 1
                if done == len(workers):
                    break
            else:
                yield (worker, item)

def async_to_sync_generator(async_gen):
    loop = asyncio.new_event_loop()
    while True:
        try:
            yield loop.run_until_complete(async_gen.__anext__())
        except StopAsyncIteration:
            break


for worker, item in async_to_sync_generator(merge_worker_output_streams()):
    print(worker, item)
