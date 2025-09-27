import typing


class A:
    class B:
        def __call__(self):
            pass

    print(typing.get_type_hints(B().__call__))
