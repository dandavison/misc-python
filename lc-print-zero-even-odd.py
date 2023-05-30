# https://leetcode.com/problems/print-zero-even-odd


"""
You have a function printNumber that can be called with an integer parameter and
prints it to the console.

You are given an instance of the class ZeroEvenOdd that has three functions:
zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three
different threads:

Thread A: calls zero() that should only output 0's.

Thread B: calls even() that should only output even numbers.

Thread C: calls odd() that should only output odd numbers.

Modify the given class to output the series "010203040506..." where the length
of the series must be 2n.

Implement the ZeroEvenOdd class:

ZeroEvenOdd(int n) Initializes the object with the number n that represents the
numbers that should be printed.

void zero(printNumber) Calls printNumber to output one zero.

void even(printNumber) Calls printNumber to output one even number.

void odd(printNumber) Calls printNumber to output one odd number.


Example 1:

Input: n = 2 Output: "0102" Explanation: There are three threads being fired
asynchronously. One of them calls zero(), the other calls even(), and the last
one calls odd(). "0102" is the correct output.

Example 2:

Input: n = 5 Output: "0102030405"
"""
from itertools import count
from threading import Lock, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.evens = (2 * (i + 1) for i in count())
        self.odds = (2 * i + 1 for i in count())
        self.count_zeros = 0
        self.last_was_zero = Lock()
        self.last_was_non_zero = Lock()
        self.last_non_zero_was_odd = Lock()
        self.last_non_zero_was_even = Lock()
        self.last_was_zero.acquire()  # non-zeros (odds and evens) are blocked initially
        self.last_non_zero_was_odd.acquire()  # evens are blocked after the first zero

    def zero(self, printNumber):
        while True:
            # print("* zero 0")
            self.last_was_non_zero.acquire()
            printNumber(0)
            self.count_zeros += 1
            if self.count_zeros == self.n:
                break
            self.last_was_zero.release()
            # print("* zero done")
            if self.count_zeros == self.n:
                break

    def odd(self, printNumber):
        while True:
            if self.count_zeros == self.n:
                break
            # print("* odd 0")
            self.last_non_zero_was_even.acquire()
            # print("* odd 1")
            if self.count_zeros == self.n:
                break
            self.last_was_zero.acquire()
            printNumber(next(self.odds))
            self.last_was_non_zero.release()
            self.last_non_zero_was_odd.release()

    def even(self, printNumber):
        while True:
            if self.count_zeros == self.n:
                break
            # print("* even 0")
            self.last_non_zero_was_odd.acquire()
            # print("* even 1")
            if self.count_zeros == self.n:
                break
            self.last_was_zero.acquire()
            printNumber(next(self.evens))
            self.last_was_non_zero.release()
            self.last_non_zero_was_even.release()


def printNumber(n):
    print(n)


z = ZeroEvenOdd(5)
threads = [
    Thread(target=lambda: z.zero(printNumber)),
    Thread(target=lambda: z.even(printNumber)),
    Thread(target=lambda: z.odd(printNumber)),
]
for t in threads:
    t.start()

for t in threads:
    t.join()
