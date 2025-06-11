from typing import Awaitable, Union


class X:
    def foo(self) -> Union[int, Awaitable[int]]:
        raise NotImplementedError


class Y(X):
    async def foo(self) -> int:
        return 8
