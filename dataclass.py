from dataclasses import dataclass
from typing import Optional


@dataclass
class X:
    a: int
    c: int
    b: Optional[int] = None

    def __repr__(self):
        return f"X(a={self.a}, b={self.b}, c={self.c})"


if False:
    print(X(1, 2))  # TypeError: non-default argument 'c' follows default argument


@dataclass
class Node:
    line_num: Optional[bool]


@dataclass
class BinOp(Node):
    op: str
    left: int
    right: int


# Nested dataclass


@dataclass()
class Y:
    b: int


@dataclass()
class Z:
    a: int
    y: Y


print(Z(1,2))