import warnings


def test():
    warnings.warn(RuntimeWarning("I am a warning"))
    print("I am in the test")
