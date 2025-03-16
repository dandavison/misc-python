from typing import Type


def my_class_decorator(cls: Type) -> int:
    return 7


@my_class_decorator
class X:
    pass


print(X)
