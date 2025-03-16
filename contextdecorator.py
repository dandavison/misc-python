from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")


class my_span:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapped(*args: Any, **kwargs: Any) -> T:
            with self:
                res = func(*args, **kwargs)
                print(f"span {self.name} result: {res}")
                return res

        return wrapped

    def __enter__(self):
        print(f"Starting span {self.name}")
        return self

    def __exit__(self, *exc):
        print(f"Ending span {self.name}")
        return None


# Use as decorator
@my_span("test")
def some_function(x: int) -> int:
    print("In function")
    return x + 7


# Use as context manager
with my_span("test"):
    print("In context")

print("\n\n")
some_function(1)
