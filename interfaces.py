from abc import ABC, abstractmethod
from typing import Protocol

# Interfaces


class MyABCInterface(ABC):
    @abstractmethod
    def foo(self) -> int: ...


class MyProtocolInterface(Protocol):
    def foo(self) -> int: ...


# Implementations


class MyImpl1(MyABCInterface):
    def foo(self, a: str) -> int:  # signature does not match interface
        return 7


class MyImpl2(MyProtocolInterface):
    def foo(self, a: str) -> int:  # signature does not match interface
        return 7
