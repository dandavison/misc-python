#!/usr/bin/env python3
from time import sleep

import threading


class Thread2(threading.Thread):
    def run(self):
        print("thread 2 spawned and about to sleep")
        sleep(999999)


class Thread1(threading.Thread):
    def run(self):
        print("thread 1")
        thread = Thread2()
        thread.start()
        print("thread 1 about to exit")


thread = Thread1()
thread.start()
thread.join()
print("Thread 1 finished")
