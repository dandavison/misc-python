# https://leetcode.com/problems/partition-array


# Given an array nums, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

# Example 1:

# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:

# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # Every time we hit a new max, that's a candidate partition point.
        # We don't change that candidate unless we go below it; in that case
        # we cancel the candidate and continue until finding something that's
        # above the canceled candidate again and set that to be the candidate.
        part = 0
        have_candidate = True
        for i in range(1, len(nums)):
            if nums[i] < nums[part]:
                have_candidate = False
            elif nums[i] > nums[part] and not have_candidate:
                part = i - 1
                have_candidate = True
        assert have_candidate
        return part + 1
