# https://leetcode.com/problems/longest-common-prefix


import itertools


class Solution:
    def longestCommonPrefix(self, s):
        s = sorted(s)
        s1, s2 = s[0], s[-1]
        i = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return s1[:i]
            i +=1
        return s1


print(Solution().longestCommonPrefix(["aa", "abb", "aaz"]))
