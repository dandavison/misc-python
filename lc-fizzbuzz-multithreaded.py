# https://leetcode.com/problems/fizzbuzz-multithreaded


from threading import Condition, Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 0
        self.cond = Condition()
        self.mutex = Lock()

    def advance(self):
        with self.mutex:
            self.i += 1
        self.cond.notify_all()

    def fizz(self, printFizz):
        # i % 3 == 0
        while self.i < 15:
            with self.cond:
                # block until i % 3 == 0 and i % 5 != 0
                self.cond.wait_for(
                    lambda: self.i % 3 == 0 and self.i % 5 != 0 or self.i >= 15
                )
                printFizz()
                self.advance()

    def buzz(self, printBuzz):
        # i % 5 == 0
        while self.i < 15:
            with self.cond:
                # block until i % 5 == 0 and i % 3 != 0
                self.cond.wait_for(
                    lambda: self.i % 3 != 0 and self.i % 5 == 0 or self.i >= 15
                )
                printBuzz()
                self.advance()

    def fizzbuzz(self, printFizzBuzz):
        # i % 3 == 0 and i % 5 == 0
        while self.i < 15:
            with self.cond:
                # block until i % 3 == 0 and i % 5 == 0
                self.cond.wait_for(
                    lambda: self.i % 3 == 0 and self.i % 5 == 0 or self.i >= 15
                )
                printFizzBuzz()
                self.advance()

    def number(self, printNumber):
        # otherwise
        while self.i < 15:
            with self.cond:
                # block until i % 3 != 0 and i % 5 != 0
                self.cond.wait_for(
                    lambda: self.i % 3 != 0 and self.i % 5 != 0 or self.i >= 15
                )
                printNumber(next(self.counter))
                self.advance()
