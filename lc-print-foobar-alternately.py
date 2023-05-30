# https://leetcode.com/problems/print-foobar-alternately


# Runtime: 64 ms, faster than 20.73% of Python3 online submissions for Print FooBar Alternately.
# Memory Usage: 15 MB, less than 5.32% of Python3 online submissions for Print FooBar Alternately.

# The same instance of FooBar will be passed to two different threads:

# thread A will call foo(), while
# thread B will call bar().
# Modify the given program to output "foobar" n times.
from enum import Enum
from threading import Condition


class Turn(Enum):
    FOO = 0
    BAR = 1


class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        # foo permitted; bar blocked
        self.turn = Turn.FOO

    def foo(self, printFoo):
        # foo permitted; bar blocked
        for i in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.turn == Turn.FOO)
                printFoo()
                # transition to foo blocked; bar permitted
                self.turn = Turn.BAR
                self.cond.notify(1)

    def bar(self, printBar):
        # foo permitted; bar blocked
        for i in range(self.n):
            with self.cond:

                # TODO: Isn't there a risk that we will enter here first, and
                # then deadlock because we are waiting forever for turn == BAR?

                # transition to foo blocked; bar permitted
                self.cond.wait_for(lambda: self.turn == Turn.BAR)
                printBar()
                # transition to foo permitted; bar blocked
                self.turn = Turn.FOO
                self.cond.notify(1)
