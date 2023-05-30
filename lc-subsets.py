# https://leetcode.com/problems/subsets


from typing import List

_cache = {}

class Solution:
    # LC solution. This passes and is much faster than mine.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

    # My solution
    def subsets_me(self, nums: List[int]) -> List[List[int]]:
        key = tuple(nums)
        if key in _cache:
            return _cache[key]

        # Let P denote powerset. P(nums) is formed as follows:
        # 1. Initialize P(nums) to {emptyset, nums}
        # 2. For each element n of nums:
        #    a. Add {n} to P(nums)
        #    b. Add every element of P(nums \ {n}) to P(nums)
        subsets = [[]]
        if not nums:
            # Powerset of empty set is a set containing just emptyset
            return subsets

        for i in range(len(nums)):
            singleton = [nums[i]]
            rest = nums[:i] + nums[i+1:]
            subsets.append(singleton)
            subsets.extend(self.subsets_me(rest))

        subsets.append(nums)
        subsets = list(map(list, {tuple(s) for s in subsets}))

        _cache[key] = subsets
        return subsets
