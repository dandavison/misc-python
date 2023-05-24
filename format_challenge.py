from collections.abc import Iterator


# class X(dict):
#     def __mod__(self, _):
#         return ("Dan", 77)

# def __getattribute__(self, _name):
#     return "Dan"

# def __getitem__(self, _key):
#     return 7

# def __iter__(self) -> Iterator:
#     return iter([7, 7])

# def __len__(self) -> int:
#     return 2


class X(dict):
    def __getitem__(self, key):
        if key == "name":
            return "Dan"

    def __lmod__(self, _):
        return ("Dan", 7)


print("Hello, %(name)s. You are %d years old." % X())

# print("Hello, %s. You are %d years old." % ("Dan", 77))  # noqa
