from typing import Tuple, overload


@overload
def f(a: int, *, c: int = 2) -> Tuple[int, int, int]: ...


@overload
def f(a: int, b: int, *, c: int = 2) -> Tuple[int, int, int]: ...


def f(a: int, b: int = 1, c: int = 2) -> Tuple[int, int, int]:
    return a, b, c


if __name__ == "__main__":
    print(f(0))
    print(f(0))
