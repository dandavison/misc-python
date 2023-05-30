# https://leetcode.com/problems/two-sum-less-than-k


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        best = -1
        while left < right:
            curr = nums[left] + nums[right]
            if curr >= k:
                right -= 1
            else:
                best = max(best, curr)                
                left += 1
        return best
