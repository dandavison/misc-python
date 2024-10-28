#!/usr/bin/env python
"""
1. Run ngrok on your local machine, e.g. `ngrok tcp 7777` and note the ngrok IP and port

2. Temporarily commit the script and add a line like this to a GitHub Actions YAML job definition:
   ```
   python netrepl.py <ngrok-ip> <ngrok-port>
   ```

3. Run `nc -l 7777` on your local machine, and then run the GitHub workflow
"""

import socket
import subprocess
import traceback
from typing import Callable


def netrepl(address: str, port: int):
    sock = socket.socket()
    print(f"connecting to {address}:{port}")
    sock.connect((address, port))
    print("starting REPL")

    def read():
        return sock.recv(0xFFFF).decode("utf-8")

    def write(s: str):
        sock.send(s.encode("utf-8"))

    repl(read, write)


def repl(read: Callable[[], str], write: Callable[[str], None]):
    while True:
        write("\n> ")
        try:
            input = read().strip()
            if input == "exit":
                break
            proc = subprocess.run(["bash", "-c", input], capture_output=True)
            if proc.returncode != 0:
                write(f"exit code: {proc.returncode}\n")
            if proc.stderr:
                for line in proc.stderr.decode("utf-8").splitlines(keepends=True):
                    write(f"stderr: {line}")
            for line in proc.stdout.decode("utf-8").splitlines(keepends=True):
                write(line)
        except Exception as err:
            write(f"error: {err}")
            write(traceback.format_exc())


if __name__ == "__main__":
    import sys

    address, port = sys.argv[1:]
    netrepl(address, int(port))
