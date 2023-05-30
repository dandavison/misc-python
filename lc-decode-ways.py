# https://leetcode.com/problems/decode-ways


from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        codes = [str(i) for i in range(1, 26 + 1)]

        @cache
        def n_decodings(s):
            if not s:
                return 1
            else:
                return sum(n_decodings(s[len(code):])
                          for code in codes
                          if s.startswith(code))
            
        return n_decodings(s)
