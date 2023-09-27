import traceback
from typing import Callable


def repl(
    read: Callable[[], str], write: Callable[[str], None], globals: dict, locals: dict
):
    while True:
        write("\n🐍 ")
        try:
            write(str(eval(read(), globals, locals)))
        except Exception:
            write(traceback.format_exc())
