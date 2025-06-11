def f():
    raise RuntimeError("foo")


def main():
    try:
        f()
    except Exception:
        raise ValueError("bar")
