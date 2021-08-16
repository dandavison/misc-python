from threading import Thread
from typing import List
from queue import Queue


def select(*channels: List[Queue]):
    merged = Queue(maxsize=-1)

    def merge(c: Queue):
        while True:
            merged.put(c.get())

    for c in channels:
        t = Thread(target=merge, args=(c,))
        t.daemon = True
        t.start()

    while True:
        yield merged.get()


c1 = Queue()
c2 = Queue()

c1.put("11")
c1.put("12")
c2.put("21")
c2.put("22")

for msg in select(c1, c2):
    print(msg)
