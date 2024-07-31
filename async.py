from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Iterator

AsyncFn = Iterator


@dataclass
class Scheduler:
    _ready: deque[Callable] = field(default_factory=deque)

    def run_forever(self, async_fn: AsyncFn):
        pass

    def call_soon(self, callback: Callable):
        self._ready.append(callback)

    def run(self, *async_fns: AsyncFn):
        while self._ready:
            fn = self._ready.popleft()
            try:
                fn()
            except StopIteration:
                raise


if __name__ == "__main__":

    def my_async_fn():
        print("hello")
        yield
        print("bye")

    Scheduler().run_forever(my_async_fn())
