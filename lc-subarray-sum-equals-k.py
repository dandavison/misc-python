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

from collections import Counter
from typing import List

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsums_to_left = Counter([0]) # There's a cumulative sum of zero at the start
        cumsum, n_subarrays = 0, 0
        for n in nums:
            cumsum += n
            n_subarrays += cumsums_to_left[cumsum - k]
            cumsums_to_left[cumsum] += 1

        return n_subarrays
