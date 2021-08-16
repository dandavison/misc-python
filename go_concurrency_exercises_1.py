import random
import time
from itertools import count
from threading import Thread
from queue import Queue


def stream():
    counter = count()
    while True:
        yield f"msg {next(counter)}"
        time.sleep(random.random())


def make_producer_thread(queue):
    def closure():
        for msg in stream():
            queue.put(msg)

    return Thread(target=closure)


def make_consumer_thread(queue):
    def closure():
        while True:
            print(queue.get())

    return Thread(target=closure)


q = Queue()
threads = [make_producer_thread(q), make_consumer_thread(q)]

for t in threads:
    t.start()

for t in threads:
    t.join()
