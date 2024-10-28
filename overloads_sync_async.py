import asyncio
from typing import Any, Coroutine, Literal, Union, overload


@overload
async def f(a: int) -> tuple[int, str]: ...


@overload
def f(a: int, *, lazy: Literal[True]) -> tuple[int, str]: ...


def f(
    a: int, lazy: bool = False
) -> Union[tuple[int, str], Coroutine[Any, Any, tuple[int, str]]]:
    if lazy:
        return f_fn(a)
    else:
        return f_coro(a)


def f_fn(a: int) -> tuple[int, str]:
    return (a, "fn")


async def f_coro(a: int) -> tuple[int, str]:
    return (a, "coro")


if __name__ == "__main__":
    print("should be (1, coro)")
    print(asyncio.run(f(1)))

    print("should be (1, fn)")
    print(f(1, lazy=True))
