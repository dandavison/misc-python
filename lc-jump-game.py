# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.

# Return true if you can reach the last index, or false otherwise.
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # passes
        # Note we always jump right
        n = len(nums)
        can = [False] * n
        can[-1] = True
        for i in reversed(range(0, n - 1)):
            can[i] = any(can[j] for j in range(i, i + nums[i] + 1))
        return can[0]        

    def __init__(self):
        self.cache = {}
    
    def canJump_2(self, nums: List[int]) -> bool:
        # times out
        if not nums or nums == [0]:
            return True
        else:
            key = tuple(nums)
            if key not in self.cache:
                self.cache[key] = any(self.canJump_2(nums[i:]) for i in range(1, nums[0] + 1))
            return self.cache[key]
