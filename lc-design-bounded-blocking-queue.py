from threading import Condition, Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lock = Lock()
        self.is_not_empty = Condition(self.lock)
        self.is_not_full = Condition(self.lock)
        self.queue = []


    def enqueue(self, element: int) -> None:
        with self.lock:
            while len(self.queue) == self.capacity:
                self.is_not_full.wait()
            self.queue.append(element)
            self.is_not_empty.notify()

    def dequeue(self) -> int:
        with self.lock:
            while not self.queue:
                self.is_not_empty.wait()
            element, self.queue = self.queue[0], self.queue[1:]
            self.is_not_full.notify()
            return element


    def size(self) -> int:
        return len(self.queue)
