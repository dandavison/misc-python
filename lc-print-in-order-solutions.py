# https://leetcode.com/problems/print-in-order-solutions


# Runtime: 3472 ms, faster than 7.46% of Python3 online submissions for Print in Order.
# Memory Usage: 14.8 MB, less than 33.85% of Python3 online submissions for Print in Order.


class Foo:
    def __init__(self):
        self.done_first = False
        self.done_second = False

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done_first = True

    def second(self, printSecond: "Callable[[], None]") -> None:

        while not self.done_first:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.done_second = True

    def third(self, printThird: "Callable[[], None]") -> None:

        while not self.done_second:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# Runtime: 44 ms, faster than 54.97% of Python3 online submissions for Print in Order.
# Memory Usage: 14.7 MB, less than 33.85% of Python3 online submissions for Print in Order.
from threading import Barrier


class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird):
        self.second_barrier.wait()
        printThird()


# Runtime: 44 ms, faster than 54.97% of Python3 online submissions for Print in Order.
# Memory Usage: 14.7 MB, less than 65.53% of Python3 online submissions for Print in Order.

from threading import Event


class Foo:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self, printFirst):
        printFirst()
        self.done[0].set()

    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()

    def third(self, printThird):
        self.done[1].wait()
        printThird()


# Runtime: 36 ms, faster than 86.23% of Python3 online submissions for Print in Order.
# Memory Usage: 14.6 MB, less than 65.53% of Python3 online submissions for Print in Order.

from threading import Semaphore


class Foo:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst):
        printFirst()
        self.gates[0].release()

    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird):
        with self.gates[1]:
            printThird()


# Runtime: 44 ms, faster than 54.97% of Python3 online submissions for Print in Order.
# Memory Usage: 14.8 MB, less than 33.85% of Python3 online submissions for Print in Order.
from threading import Condition


class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()


# Runtime: 44 ms, faster than 54.97% of Python3 online submissions for Print in Order.
# Memory Usage: 14.6 MB, less than 88.41% of Python3 online submissions for Print in Order.

from threading import Lock


class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        printFirst()
        self.locks[0].release()

    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        with self.locks[1]:
            printThird()
