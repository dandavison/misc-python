import traceback


def f():
    g()


def g():
    try:
        raise ValueError
    except Exception:
        print("caught exception", "\n".join(traceback.format_stack()))


f()
