from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fb, self.f, self.b, self.main = (
            Lock(),
            Lock(),
            Lock(),
            Lock(),
        )
        self.fb.acquire()
        self.f.acquire()
        self.b.acquire()
        # main is the only one available initially
        self.done = False

    def fizz(self, printFizz):
        # i % 3 == 0
        while True:
            self.f.acquire()
            if self.done:
                return
            printFizz()
            self.main.release()

    def buzz(self, printBuzz):
        # i % 5 == 0
        while True:
            self.b.acquire()
            if self.done:
                return
            printBuzz()
            self.main.release()

    def fizzbuzz(self, printFizzBuzz):
        # i % 3 == 0 and i % 5 == 0
        while True:
            self.fb.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.main.release()

    def number(self, printNumber):
        # otherwise
        for i in range(1, self.n + 1):
            self.main.acquire()
            if self.done:
                return
            if i % 3 == 0 and i % 5 == 0:
                self.fb.release()
            elif i % 3 == 0 and i % 5 != 0:
                self.f.release()
            elif i % 3 != 0 and i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release()

        self.main.acquire()
        self.done = True
        self.f.release()
        self.b.release()
        self.fb.release()
