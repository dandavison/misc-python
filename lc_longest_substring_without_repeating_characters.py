# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return max(length_at(i, s) for i in range(len(s)))


def length_at(i: int, s: str) -> int:
    seen = set()
    n = 0
    for j in range(i, len(s)):
        c = s[j]
        if c in seen:
            break
        else:
            seen.add(c)
            n += 1
    return n
