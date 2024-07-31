from typing import AsyncGenerator, Generator


def contents():
    yield "shared 1"
    yield "shared 2"


async def agen() -> AsyncGenerator[str, None]:
    for i in [1, 2, 3]:
        for item in contents():
            yield item


def gen() -> Generator[str, None, None]:
    for i in [1, 2, 3]:
        for item in contents():
            yield item
