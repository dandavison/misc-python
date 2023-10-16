import socket
import traceback
from typing import Callable


def netrepl(address: str, port: int, globals: dict, locals: dict):
    from repl import repl

    sock = socket.socket()
    sock.connect((address, port))

    def read():
        return sock.recv(0xFFFF).decode("utf-8")

    def write(s: str):
        sock.send(s.encode("utf-8"))

    repl(read, write, globals, locals)


def repl(
    read: Callable[[], str], write: Callable[[str], None], globals: dict, locals: dict
):
    while True:
        write("\n🐍 ")
        try:
            write(str(eval(read(), globals, locals)))
        except Exception:
            write(traceback.format_exc())


if __name__ == "__main__":
    import sys

    address, port = sys.argv[1:]
    netrepl(address, int(port), globals(), locals())
