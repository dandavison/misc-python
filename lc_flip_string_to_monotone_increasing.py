# 93 / 93 test cases passed.
# Status: Accepted
# Runtime: 936 ms
# Memory Usage: 19.2 MB

from typing import List


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cum = partial_sums(s)
        tot = cum[-1]
        min_flips = n
        for i in range(n + 1):
            # Compute min flips if inflection point is to the left of s[i]

            # All 1s to the left must be flipped to 0s
            flips_left = cum[i]

            # All 0s to the right must be flipped to 1s
            elements_to_right = n - i
            ones_to_right = tot - cum[i]
            flips_right = elements_to_right - ones_to_right
            flips = flips_left + flips_right
            print(flips_left, flips_right)
            # flips = 2 * cum[i] + n - i - 1 - tot
            min_flips = min(min_flips, flips)
        return min_flips


def partial_sums(s: str) -> List[int]:
    cum = [0]
    for i in range(len(s)):
        cum.append(cum[i] + int(s[i]))
    return cum
