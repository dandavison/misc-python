# Success
# Details 
# Runtime: 44 ms, faster than 41.10% of Python3 online submissions for Building H2O.
# Memory Usage: 14.9 MB, less than 72.15% of Python3 online submissions for Building H2O.

from threading import Lock


class H2O:
    def __init__(self):
        self.h_lock = Lock()
        self.o_lock = Lock()
        self.o_lock.acquire()
        self.n_h = 0

    def hydrogen(self, releaseHydrogen):
        self.h_lock.acquire()
        releaseHydrogen()
        self.n_h += 1
        if self.n_h == 2:
            self.o_lock.release()
        else:
            self.h_lock.release()

    def oxygen(self, releaseOxygen):
        self.o_lock.acquire()
        releaseOxygen()
        self.n_h = 0
        self.h_lock.release()
