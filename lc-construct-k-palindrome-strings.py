# https://leetcode.com/problems/construct-k-palindrome-strings/

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        # A palindrome can be formed iff there is an even count of all letters, except for optionally one odd count.
        
        # So
        # (1) there must be <=k letters with odd counts and the rest of the counts must all be even.
        # (2) The max number of palindromes we can make is len(s)
        
        counts = Counter(s).values() # a: 2, n: 2, b: 1, e: 2, l: 2
        n_odd = sum(1 for n in counts if n % 2 == 1)
        
        return n_odd <= k and len(s) >= k
