def f():
    raise RuntimeError("foo")


try:
    f()
except Exception:
    raise ValueError("bar")
