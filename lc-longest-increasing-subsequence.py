# https://leetcode.com/problems/longest-increasing-subsequence/submissions/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Implement longest increasing subsequence.
        """
        #  [ 0, 1, 2, 3, 4, 5,   6,  7]
        #  [10, 9, 2, 5, 3, 7, 101, 18]
        #  [ 1, 1, 4, 3, 3, 2,   1,  1]
        n = len(nums)  # n= 8
        lis = [1] * n  #
        longest = 1
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
            longest = max(lis[i], longest)
        return longest


if False:
    f = Solution().lengthOfLIS
    f([10, 9, 2, 5, 3, 4, 101, 18])
