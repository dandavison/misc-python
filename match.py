# from enum import Enum

# from dataclass import dataclass

if False:

    class E(Enum):
        A = 1
        B = 2

    match E.A:
        case E.A:
            print("Got E.A")

    @dataclass
    class X:
        a: int

    class Y:
        pass

    match X(7):
        case X(a):
            print("got X")
        case Y():
            print("got Y")
        case _:
            print("no match")

    class X:
        def __init__(self, a: int):
            self.a = a

    match X(7):
        case X():
            print(f"Matched X()")


match x := [1, 2, 3]:
    case (1, *args):
        print(f"got it: {args}")
