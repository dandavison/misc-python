from __future__ import annotations

from typing import Type


def my_class_decorator(cls: Type) -> int:
    return 7


@my_class_decorator
class X:
    pass


print(X)


class Y:
    def f(self) -> Y:
        return self


print(Y().f())


def x_method(fn: Callable[[Any], None]) -> Callable[[X, Any], None]:
    def wrapper(self: X, arg: Any) -> None:
        return fn(arg)

    return wrapper


class X:
    @x_method
    def foo(arg: int) -> None:
        pass
