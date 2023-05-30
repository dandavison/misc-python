# https://leetcode.com/problems/3sum-smaller/

# Given an array of n integers nums and an integer target, find the number of
# index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
# nums[i] + nums[j] + nums[k] < target.

# Example 1:

# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
# Example 2:

# Input: nums = [], target = 0
# Output: 0
# Example 3:

# Input: nums = [0], target = 0
# Output: 0


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n < 3:
            return 0
        count = 0
        for left in range(n - 2):
            mid, right = left + 1, n - 1
            while mid < right:
                if nums[left] + nums[mid] + nums[right] < target:
                    count += right - mid
                    mid += 1
                else:
                    right -= 1
        return count
