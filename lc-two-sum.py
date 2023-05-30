# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            try:
                return [i, seen[target - n]]
            except KeyError:
                seen[n] = i
