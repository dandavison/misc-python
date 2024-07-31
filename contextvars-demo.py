import asyncio
import contextvars
from asyncio import Future, Handle


# from collections import deque
# from dataclasses import dataclass, field
from typing import Callable, Optional

condition_info = contextvars.ContextVar("condition_info")


# @dataclass
# class EventLoop:
#     conditions: list[tuple[Callable, Future, Optional[Handle]]] = field(
#         default_factory=list
#     )

#     _ready: deque[Handle] = field(default_factory=deque)

#     async def wait_condition(self, fn: Callable):
#         fut = Future[bool]()
#         info = (fn, fut, None)
#         condition_info.set(info)
#         self.conditions.append(info)
#         self.call_later(lambda: fut.set_result(True))

#     def call_later(self, fn: Callable):
#         handle = Handle(fn, [], asyncio.AbstractEventLoop())
#         if info := condition_info.get(None):
#             setattr(info[1], "_handle", handle)
#         self._ready.append(handle)


async def foo() -> tuple[Callable, Future, Optional[Handle]]:
    fut = Future[bool]()
    info = (lambda: True, fut, None)
    condition_info.set(info)
    bar()
    return info


def bar():
    setattr(condition_info.get()[1], "_tmp", "hello")


async def main():
    info = await foo()
    print(getattr(info[1], "_tmp"))


asyncio.run(main())
