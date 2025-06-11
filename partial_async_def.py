import asyncio
import functools
import inspect
from functools import partial
from typing import Any


async def f(a, b):
    print("f", a, b)
    await asyncio.sleep(1)
    print("f done")


class ff_cls:
    async def __call__(self, a, b):
        print("ff", a, b)
        await asyncio.sleep(1)
        print("ff done")


ff = ff_cls()

g = partial(ff, a=1)


def is_async_callable(obj: Any) -> bool:
    while isinstance(obj, functools.partial):
        obj = obj.func

    return inspect.iscoroutinefunction(obj) or (
        callable(obj) and inspect.iscoroutinefunction(getattr(obj, "__call__", None))
    )


print(inspect.iscoroutinefunction(g))
print(is_async_callable(g))


async def main():
    await g(b=2)


asyncio.run(main())
