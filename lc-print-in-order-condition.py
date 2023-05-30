# https://leetcode.com/problems/print-in-order-condition


from threading import Lock
from typing import Callable


class Foo:
    def __init__(self):
        self.lock_2 = Lock()
        self.lock_3 = Lock()
        self.lock_2.acquire()
        self.lock_3.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock_2.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.lock_2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock_3.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.lock_3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
