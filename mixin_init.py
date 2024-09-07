#!/usr/bin/env python3

class Mixin:
    def __init__(self) -> None:
        print("Mixin.__init__")

class Base(Mixin):
    def __init__(self) -> None:
        print("Base.__init__")


Base()