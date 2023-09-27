"""
E.g.

In a terminal: `nc -l 7777`

In Python: `netread("127.0.0.1", 7777)`  # blocks

In the terminal: `hello <Enter>`

In Python:                               # returns "hello\n"
"""
import os
import socket
import subprocess
import tempfile


def netrepl(address: str, port: int, globals: dict, locals: dict):
    from repl import repl

    sock = socket.socket()
    sock.connect((address, port))

    def read():
        return sock.recv(0xFFFF).decode("utf-8")

    def write(s: str):
        sock.send(s.encode("utf-8"))

    repl(read, write, globals, locals)


def netread(address: str, port: int, python=True):
    if python:
        return _netread_python(address, port)
    else:
        return _netread_os_system(address, port)


def _netread_python(address: str, port: int):
    sock = socket.socket()
    sock.connect((address, port))
    return sock.recv(0xFFFF).decode("utf-8")


def netwrite(s: str, address: str, port: int, python=True):
    if python:
        _netwrite_python(s, address, port)
    else:
        _netwrite_os_system(s, address, port)


def _netwrite_python(s: str, address: str, port: int):
    sock = socket.socket()
    sock.connect((address, port))
    sock.send(s.encode("utf-8"))


def _netread_netcat(address: str, port: int):
    return subprocess.check_output(["nc", address, str(port)]).decode("utf-8")


def _netread_os_system(address: str, port: int):
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        temp_file = tf.name
    try:
        os.system(f"nc {address} {port} > {temp_file}")
        with open(temp_file, "r") as f:
            output = f.read()
    finally:
        os.remove(temp_file)
    return output


def _netwrite_netcat(s: str, address: str, port: int):
    subprocess.run(["nc", address, str(port)], input=s.encode("utf-8"), check=True)


def _netwrite_os_system(s: str, address: str, port: int):
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        temp_file = tf.name
    try:
        with open(temp_file, "w") as f:
            f.write(s)
        os.system(f"nc {address} {port} < {temp_file}")
    finally:
        os.remove(temp_file)


if __name__ == "__main__":
    foo = 7
    netrepl("127.0.0.1", 7777, globals(), locals())
