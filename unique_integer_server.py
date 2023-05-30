# Users can send a request to a service and receive an integer
# that has never been sent in any other response. The service comprises
# multiple nodes.
import asyncio
import random
from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Thread
from typing import List, Tuple

CHUNK_SIZE = 3


SEEN = set()

def record(val):
    assert val not in SEEN, (val, SEEN)
    SEEN.add(val)


def log(msg):
    if 0:
        print(msg, flush=True)

class MasterService:
    def __init__(self) -> None:
        self.next_chunk_start = 0
        self.chunk_size = CHUNK_SIZE
        self.mutex = Lock()

    def get_chunk(self) -> Tuple[int, int]:
        with self.mutex:
            chunk_start = self.next_chunk_start
            self.next_chunk_start += CHUNK_SIZE
            return (chunk_start, self.next_chunk_start)

    async def get_chunk_async(self) -> Tuple[int, int]:
        chunk_start = self.next_chunk_start
        self.next_chunk_start += CHUNK_SIZE
        return (chunk_start, self.next_chunk_start)


class IntService:

    def __init__(self, id: str, master: MasterService) -> None:
        self.id = id
        self.master = master
        self.chunk_curr = 0
        self.chunk_end = 0
        self.mutex = Lock()

    def get(self):
        with self.mutex:
            if self.chunk_curr == self.chunk_end:
                self.chunk_curr, self.chunk_end = self.master.get_chunk()
                log(f"{self.id}: allocated chunk: {(self.chunk_curr, self.chunk_end)}")
            val = self.chunk_curr
            self.chunk_curr += 1
            record(val)
            log(f"{self.id}, {val}")
            return val

    async def get_async(self):
        if self.chunk_curr == self.chunk_end:
            self.chunk_curr, self.chunk_end = await self.master.get_chunk_async()
            log(f"{self.id}: allocated chunk: {(self.chunk_curr, self.chunk_end)}")
        val = self.chunk_curr
        self.chunk_curr += 1
        record(val)
        log(f"{self.id}, {val}")
        return val


master = MasterService()
int_services = [IntService(id, master) for id in ["a", "b", "c"]]

use_threads = False
if use_threads:
    with ThreadPoolExecutor(max_workers=64) as executor:
        for client in range(1000):
            service = random.choice(int_services)
            executor.submit(service.get)
else:
    async def run_tasks():
        async with asyncio.TaskGroup() as tg:
            for client in range(1000):
                service = random.choice(int_services)
                tg.create_task(service.get_async())

    asyncio.run(run_tasks())
