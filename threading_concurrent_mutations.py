import sys

from threading import Thread
from time import sleep

d = {}


def mutate():
    d["a"] = 1
    sleep(0.1)
    d["b"] = 2
    sleep(0.1)
    d.pop("a", None)
    sleep(0.1)
    d.pop("b", None)
    print(len(d), flush=True)
    sleep(0.1)


(n,) = map(int, sys.argv[1:])
for _ in range(n):
    Thread(target=mutate).start()
