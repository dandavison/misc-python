# https://leetcode.com/problems/4sum


# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(set(nums))
        print(f"4sum({nums}, {target}) = ...")
        quads = set()
        for n1 in nums:
            for triplet in self.threeSum([n for n in nums if n != n1], target - n1):
                quads.add(tuple(sorted((n1,) + triplet)))
        print(f"4sum({nums}, {target}) = {quads}")
        return list(map(list, quads))

    def threeSum(self, nums, target):
        print(f"    3sum({nums}, {target}) = ...")
        triplets = []
        for n1 in nums:
            for pair in self.pairSum([n for n in nums if n != n1], target - n1):
                triplets.append((n1,) + pair)
        print(f"    3sum({nums}, {target}) = {triplets}")
        return triplets

    def pairSum(self, nums, target):
        seen = set()
        pairs = []
        for n1 in nums:
            if target - n1 in seen:
                pairs.append((target - n1, n1))
            seen.add(n1)
        print(f"        2sum({nums}, {target}) = {pairs}")
        return pairs


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(Solution().threeSum([0, -1, 0, -2, 2], -1))
