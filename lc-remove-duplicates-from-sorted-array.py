# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/953634257/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = 0
        write_pos, read_pos = 0, 0
        curr = None
        for read_pos in range(len(nums)):
            read = nums[read_pos]
            if read == curr:
                continue
            else:
                uniques += 1
                if read_pos != write_pos:
                    nums[write_pos] = read
                write_pos += 1
                curr = read
        return uniques
