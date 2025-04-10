from typing import Callable, TypeVar, Union, overload

from typing_extensions import Concatenate, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def add_c_param(f: Callable[P, R]) -> Callable[Concatenate[int, P], R]: ...


@overload
@add_c_param
def f(a: int) -> int: ...


_ = f


@overload
def f(a: int, b: int) -> str: ...


def f(a: int, b: int = 0, c: int = 0) -> Union[int, str]:
    if b > 0:
        return "hello"
    else:
        return 0
