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
    proc = subprocess.Popen(
        ["bash"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert proc.stdin and proc.stdout and proc.stderr

    while True:
        write("\n> ")
        try:
            input = read().strip()
            if input == "exit":
                break
            proc.stdin.write(input + "\n")
            proc.stdin.flush()

            # Read stdout
            while True:
                output = proc.stdout.readline()
                if output == "" and proc.poll() is not None:
                    break
                if output:
                    write(output)

            # Read stderr
            while True:
                error = proc.stderr.readline()
                if error == "" and proc.poll() is not None:
                    break
                if error:
                    write(f"stderr: {error}")

        except Exception as err:
            write(f"error: {err}")
            write(traceback.format_exc())


if __name__ == "__main__":
    import sys

    address, port = sys.argv[1:]
    netrepl(address, int(port))
