# https://leetcode.com/problems/random-pick-with-weight


from random import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        cum = 0.0
        self.dist = []
        for i, weight in enumerate(w):
            cum += weight / total
            self.dist.append((i, cum))
        

    def pickIndex(self) -> int:
        r = random()  # in [0, 1)
        for i, cum in self.dist:
            if r <= cum:
                return i
        assert False, "impossible"
