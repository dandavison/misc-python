"""
You have an input stream looking like
1, 2,   False
5, 6,   False
3, 100, True   # end of first group
77, 2,  False
46, 2,  False
7, 77,  True   # end of second group

For each group in order, emit the maximum product within the group,
using multiple cores to compute products in parallel.

(The idea is that computing a product represents a lengthier CPU-bound computation)
"""
from collections import deque
from concurrent.futures import ProcessPoolExecutor, wait, Future
from typing import Deque, Tuple, Iterable

class GroupMaximaCalculator:
    def __init__(self) -> None:
        self.executor = ProcessPoolExecutor()
        self.current_max = 0
        self.futures: Deque[Future] = deque([])

    def emit_maxima(self, input_stream: Iterable[Tuple[int, int, bool]]):
        for args in input_stream:
            self.process_pair(*args)

            while self.futures:
                fut = self.futures[0]
                if fut.done():
                    self.futures.popleft()
                    self.handle_result(*fut.result())
                else:
                    break

        _ = wait(self.futures)
        for fut in self.futures:
            self.handle_result(*fut.result())
        self.executor.shutdown()

    def handle_result(self, result: int, last_in_group: bool):
        self.current_max = max(self.current_max, result)
        if last_in_group:
            print(self.current_max)
            self.current_max = 0

    def process_pair(self, a: int, b: int, last_in_group: bool):
        self.futures.append(self.executor.submit(job, a, b, last_in_group))

def job(a: int, b: int, last_in_group: bool) -> Tuple[int, bool]:
    return (a * b, last_in_group)
