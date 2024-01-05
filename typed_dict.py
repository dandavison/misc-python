from typing import Optional, TypedDict


class D(TypedDict):
    foo: Optional[int]
    bar: Optional[str]


d = D({"foo": None, "bar": None})
d = D({"foo": 1, "bar": "a"})

print(D.__annotations__)
