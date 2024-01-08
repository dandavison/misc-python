class X:
    my_cls = int

    def foo(self) -> my_cls:
        return 7


class Y(X):
    my_cls = bool

    def bar(self):
        x = self.my_cls()
        return True
