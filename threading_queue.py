import time
from collections import deque
from threading import Thread
from queue import Queue

class QueueX:
    def __init__(self) -> None:
        self.queue = deque([])

    def put(self, msg):
        self.queue.append(msg)

    def get(self):
        return self.queue.popleft()

q = Queue()

def make_thread_A():
    def f():
        q.put("hello from A")
        time.sleep(1)
        q.put("bye from A")
    return Thread(target=f)

def make_thread_B():
    def f():
        print(q.get())
        print(q.get())
    return Thread(target=f)

threads = [make_thread_A(), make_thread_B()]

for t in threads:
    t.start()

for t in threads:
    t.join()
