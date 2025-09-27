import sys
from pprint import pprint
from typing import Generic, TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class Operation(Generic[InputT, OutputT]):
    pass


class A1:
    a: Operation[int, int]


class A2(A1):
    b: Operation[int, int]


print(sys.version, end="\n\n")
print("child class with class attribute type annotations only")
print("\n__annotations__")
pprint(A2.__annotations__)
print("\n__dict__")
pprint(A2.__dict__)


# https://docs.python.org/3/howto/annotations.html#accessing-the-annotations-dict-of-an-object-in-python-3-9-and-older


class B1:
    a: Operation[int, int] = Operation[int, int]()


class B2(B1):
    b: Operation[int, int] = Operation[int, int]()


print("\n\nchild class with class attribute type annotations with values")
print("\n__annotations__")
pprint(B2.__annotations__)
print("\n__dict__")
pprint(B2.__dict__)


class C1:
    a: Operation[int, int] = Operation[int, int]()
    b: Operation[int, int] = Operation[int, int]()


class C2(C1):
    pass


print("\n\nchild class with class attribute type annotations with values")
print("\n__annotations__")
pprint(C2.__annotations__)
print("\n__dict__")
pprint(C2.__dict__)


# ops = {name: nexusrpc.Operation[int, int] for name in op_names}
# service_cls = nexusrpc.service(type("ServiceContract", (), ops))


class D1:
    a: Operation[int, int]


d2_ops = {name: Operation[int, int] for name in ["b"]}

D2 = type("ServiceContract", (D1,), d2_ops)

print("\n\nchild class synthesized from class attribute type annotations only")
print("\n__annotations__")
pprint(D2.__annotations__)
print("\n__dict__")
pprint(D2.__dict__)
