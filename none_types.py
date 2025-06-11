import typing


def f(a: None) -> None:
    pass


annots = typing.get_type_hints(f)
print(annots)
print(annots["a"] is None)
print(annots["return"] is None)
