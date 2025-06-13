from typing import Callable, TypeVar

ParamT = TypeVar("ParamT")


class ParamSuperType:
    pass


class ParamSubType(ParamSuperType):
    pass


def decorator(f: Callable[[ParamSuperType], None]) -> Callable[[ParamSubType], None]:
    def wrapper(param: ParamSuperType) -> None:
        f(param)

    return wrapper


@decorator
def f(param: ParamSuperType) -> None:
    pass


@decorator
def g(param: ParamSubType) -> None:
    pass
