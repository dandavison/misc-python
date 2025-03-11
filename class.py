class X:
    def __new__(cls, *args, **kwargs):
        print(f"__new__({cls}, {args}, {kwargs})")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print(f"__init__({self}, {args}, {kwargs})")


x = X(1)
