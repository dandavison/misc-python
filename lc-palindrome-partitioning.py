# https://leetcode.com/problems/palindrome-partitioning


# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.

import functools
from typing import List


class Solution:
    @functools.cache
    def partition(self, s: str, indent=0) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        elif len(s) == 1:
            return [[s]]
        result = set()
        for i, j in find_palindromes(s):
            # print("\t" * indent, i, j, s[i:j], s[:i], s[j:])
            # a palindrome starts at i and ends at j-1
            for left_substrings in self.partition(s[:i], indent + 1):
                for right_substrings in self.partition(s[j:], indent + 1):
                    result.add(tuple(left_substrings + [s[i:j]] + right_substrings))
        return list(map(list, result))


def find_palindromes(s):
    for i in range(len(s)):
        yield from odd_palindrome_coords_around(i, s)
        yield from even_palindrome_coords_right_of(i, s)


def odd_palindrome_coords_around(i, s):
    j = 0
    while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
        yield i - j, i + j + 1
        j += 1


def even_palindrome_coords_right_of(i, s):
    j = 0
    while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
        yield i - j, i + j + 2
        j += 1
