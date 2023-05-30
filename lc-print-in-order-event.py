# https://leetcode.com/problems/print-in-order-event


from threading import Lock
from threading import Event
from typing import Callable


class Foo:
    def __init__(self):
        self.events = [Event(), Event()]

    def first(self, printFirst):
        printFirst()
        self.events[0].set()

    def second(self, printSecond):
        self.events[0].wait()
        printSecond()
        self.events[1].set()

    def third(self, printThird):
        self.events[1].wait()
        printThird()
