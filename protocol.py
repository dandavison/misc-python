from typing import Protocol


class P(Protocol):
    def f(self):
        print("f")


if __name__ == "__main__":
    p = P()
