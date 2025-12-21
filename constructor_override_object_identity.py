class A:
    def __init__(self, a):
        self.a = a


class B(A):
    # def __init__(self, a):
    #     super().__init__(a)
    #     self.b = a + 1

    def method(self):
        # BROKEN: This doesn't work because self.__init__ is a bound method
        # if self.__init__ is not A.__init__:
        #     print("__init__ is overridden")
        # else:
        #     print("__init__ is not overridden")

        # SOLUTION 1: Check if __init__ is in the class's own __dict__
        if "__init__" in self.__class__.__dict__:
            print("__init__ is overridden")
        else:
            print("__init__ is not overridden")

        # Alternative SOLUTION 2: Compare class methods directly
        # if self.__class__.__init__ is not A.__init__:
        #     print("__init__ is overridden")
        # else:
        #     print("__init__ is not overridden")

        # Alternative SOLUTION 3: Use __func__ to get the underlying function
        # if self.__init__.__func__ is not A.__init__:
        #     print("__init__ is overridden")
        # else:
        #     print("__init__ is not overridden")


b = B(1)
b.method()
