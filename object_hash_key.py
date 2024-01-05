class X:
    def __hash__(self) -> int:
        return 7


class Y:
    def __hash__(self) -> int:
        return 7


print({X(), Y()})
