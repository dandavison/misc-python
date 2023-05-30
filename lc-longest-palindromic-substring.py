# https://leetcode.com/problems/longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            candidate1 = expand_odd(s, i)
            candidate2 = expand_even(s, i)
            longest = max(longest, candidate1, candidate2, key=len)
        return longest


def expand_odd(s, i):
    substr = s[i]
    delta = 1
    while i - delta >= 0 and i + delta < len(s) and s[i - delta] == s[i + delta]:
        substr = s[i - delta : i + delta + 1]
        delta += 1
    return substr


def expand_even(s, i):
    substr = ""
    delta = 1
    while i - delta >= 0 and i + delta <= len(s) and s[i - delta] == s[i + delta - 1]:
        substr = s[i - delta : i + delta]
        delta += 1
    return substr


# times out
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            substr = s[i:]
            if len(longest) > len(substr):
                break
            longest_here = _longest_palindrome_fixed_start(substr)
            if len(longest_here) > len(longest):
                longest = longest_here
        return longest


def _longest_palindrome_fixed_start(s: str) -> str:
    for k in reversed(range(len(s))):
        substr = s[: k + 1]
        if is_palindrome(substr):
            return substr
    assert False, "impossible"


def is_palindrome(s: str) -> bool:
    if not s:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])
