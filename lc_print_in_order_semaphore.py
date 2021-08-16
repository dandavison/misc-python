# Passes tests; fast
from threading import Semaphore
from typing import Callable


class Foo:
    def __init__(self):
        self.sema_2 = Semaphore(0)
        self.sema_3 = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.sema_2.release()

    def second(self, printSecond):
        self.sema_2.acquire()
        printSecond()
        self.sema_3.release()

    def third(self, printThird):
        self.sema_3.acquire()
        printThird()
        self.sema_3.release()
