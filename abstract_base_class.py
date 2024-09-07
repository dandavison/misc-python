from abc import ABC, abstractmethod
from typing import AsyncGenerator


class Base(ABC):
    @abstractmethod
    async def async_gen(self) -> AsyncGenerator[int, None]: ...

    async def impl(self):
        async for i in self.async_gen():
            print(i)


# pyright: reportIncompatibleMethodOverride=true


class X(ABC):
    @abstractmethod
    def foo(self) -> int: ...


class Y(X):
    def foo(self) -> str:
        return "4"
