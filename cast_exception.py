from typing import cast

try:
    raise cast(BaseException, Exception("i am Exception"))
    raise Exception("i am Exception")
except Exception as e:
    print(f"got Exception: {e.__class__.__name__}: {isinstance(e, BaseException)}")
