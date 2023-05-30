# https://leetcode.com/problems/group-anagrams


from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_key(s):
            return tuple(sorted(Counter(s).items()))

        groups = defaultdict(list)
        for s in strs:
            groups[make_key(s)].append(s)
        return list(groups.values())
