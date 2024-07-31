from dataclasses import dataclass


class Base:
    # def __new__(cls):
    #     super().__new__(cls)
    #     print(f"Base.__new__")

    def __init__(self, *args):
        super().__init__(*args)
        print(f"Base.__init__: {self}")


@dataclass
class A(Base):
    x: int

    if False:
        # If __init__ is present, there is no way to initialize the fields (?)
        # But if so, then wouldn't it be an error to define a dataclass and override __init__?
        def __init__(self, *args):
            super().__init__()
            print(f"A.__init__: {self}")

    # __post_init__ is not called if a custom __init__ exists.
    def __post_init__(self):
        print(f"A.__post_init__: {self}")


a = A(1)
