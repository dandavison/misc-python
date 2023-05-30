# https://leetcode.com/problems/print-in-order-lock


# Passes tests; fast
from threading import Lock
from typing import Callable


class Foo:
    def __init__(self):
        self.lock_2 = Lock()
        self.lock_3 = Lock()
        self.lock_2.acquire()
        self.lock_3.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock_2.release()

    def second(self, printSecond):
        self.lock_2.acquire()
        printSecond()
        self.lock_3.release()

    def third(self, printThird):
        self.lock_3.acquire()
        printThird()
