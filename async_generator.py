import asyncio
from abc import ABC, abstractmethod
from typing import AsyncGenerator


class Base(ABC):
    @abstractmethod
    async def async_gen(self) -> AsyncGenerator[int, None]: ...

    async def impl(self):
        async for i in self.async_gen():
            print(i)


async def g():
    for i in [1, 2, 3]:
        yield i


async def h():
    xxx = [i async for i in g()]
    print(xxx)


asyncio.run(h())
