from typing import Generic, TypeVar

ParamT = TypeVar("ParamT")


class ParamSuperType:
    pass


class ParamSubType(ParamSuperType):
    pass


class SuperType(Generic[ParamT]):
    def f(self, param: ParamT):
        print(param)


class SubType(SuperType):
    def f(self, param: ParamSubType):
        print(param)
