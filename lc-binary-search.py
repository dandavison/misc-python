"""
https://leetcode.com/problems/binary-search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from bisect import bisect

class Solution0:
    def search(self, nums: List[int], target: int) -> int:
        closest = bisect(nums, target) - 1
        return closest if nums[closest] == target else -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
            
        return -1

    def search_recursive(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid_idx = len(nums) // 2
        mid_num = nums[mid_idx]
        if target < mid_num:
            return self.search_recursive(nums[:mid_idx], target)
        elif mid_num == target:
            return mid_idx
        else:
            idx = self.search_recursive(nums[mid_idx+1:], target)
            if idx == -1:
                return -1
            else:
                return mid_idx + 1 + idx

