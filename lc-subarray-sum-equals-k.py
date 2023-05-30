# https://leetcode.com/problems/subarray-sum-equals-k


from collections import Counter
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot, count = 0, 0
        seen = Counter({tot: 1})
        for n in nums:
            tot += n
            count += seen[tot - k]
            seen[tot] += 1

        return count
