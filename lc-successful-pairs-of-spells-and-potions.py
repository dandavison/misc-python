# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength
# of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the
# product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form
# a successful pair with the ith spell.

from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # pairs[i] := len(1 for j in range(m) if spells[i] * potions[j] >= success)

        potions_sorted = sorted(potions)
        n, m = len(spells), len(potions)
        pairs = [0] * n
        cache = {}
        for i, spell in enumerate(spells):
            if spell not in cache:
                idx = bisect_left(potions_sorted, success / spell)
                cache[spell] = m - idx
            pairs[i] = cache[spell]
        return pairs
