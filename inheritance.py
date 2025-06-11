from dataclasses import dataclass
from pprint import pprint


class A:
    def meth_a1(self):
        pass


class B(A):
    def meth_b1(self):
        pass


@dataclass
class D1:
    a: int


@dataclass
class D2(D1):
    b: int


pprint(D2.__dict__)
