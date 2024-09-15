#!/usr/bin/env python
"""
1. Run ngrok on your local machine, e.g. `ngrok tcp 7777` and note the ngrok IP and port

2. Add a line like this to a GitHub Actions YAML job definition:
   ```
   ./oss-cicd/internal/github/netrepl <ngrok-ip> <ngrok-port>
   ```

3. Run `nc -l 7777` on your local machine, and then run the GitHub workflow
"""

import fcntl
import os
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

    # Set stdout and stderr to non-blocking
    fd_stdout = proc.stdout.fileno()
    fd_stderr = proc.stderr.fileno()
    fl_stdout = fcntl.fcntl(fd_stdout, fcntl.F_GETFL)
    fl_stderr = fcntl.fcntl(fd_stderr, fcntl.F_GETFL)
    fcntl.fcntl(fd_stdout, fcntl.F_SETFL, fl_stdout | os.O_NONBLOCK)
    fcntl.fcntl(fd_stderr, fcntl.F_SETFL, fl_stderr | os.O_NONBLOCK)

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
                try:
                    output = proc.stdout.read()
                    if output:
                        write(output)
                    else:
                        break
                except BlockingIOError:
                    break

            # Read stderr
            while True:
                try:
                    error = proc.stderr.read()
                    if error:
                        write(f"stderr: {error}")
                    else:
                        break
                except BlockingIOError:
                    break

        except Exception as err:
            write(f"error: {err}")
            write(traceback.format_exc())


if __name__ == "__main__":
    import sys

    address, port = sys.argv[1:]
    netrepl(address, int(port))
