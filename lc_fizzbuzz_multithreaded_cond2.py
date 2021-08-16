import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur = 1
        self.condition = threading.Condition()

    def fizz(self, printFizz):
        self._execute(printFizz, lambda cur: cur % 3 == 0 and cur % 5 != 0)

    def buzz(self, printBuzz):
        self._execute(printBuzz, lambda cur: cur % 3 != 0 and cur % 5 == 0)

    def fizzbuzz(self, printFizzBuzz):
        self._execute(printFizzBuzz, lambda cur: cur % 3 == 0 and cur % 5 == 0)

    def number(self, printNumber):
        self._execute(
            lambda: printNumber(self.cur), lambda cur: cur % 3 != 0 and cur % 5 != 0
        )

    def _execute(self, func, condition_func):
        while True:
            with self.condition:
                self.condition.wait_for(
                    lambda: condition_func(self.cur) or self.cur > self.n
                )

                if self.cur > self.n:
                    return
                else:
                    func()
                    self.cur += 1
                    self.condition.notify_all()
