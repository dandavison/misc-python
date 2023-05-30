# https://leetcode.com/problems/regular-expression-matching/submissions/
#
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


class Solution:
    def isMatch(self, s: str, p: str, indent=0) -> bool:
        if not p:
            return not s

        star = len(p) >= 2 and p[1] == "*"

        first_char_match = s and (p[0] == "." or s[0] == p[0])

        if star:
            # p[0] may match, 0, 1, or >1 times
            return (
                # star matches zero copies; continue matching pattern beyond start
                self.isMatch(s, p[2:])
                # star matches at least once, match with star at next string
                # position
                or first_char_match
                and self.isMatch(s[1:], p)
            )
        else:
            return first_char_match and self.isMatch(s[1:], p[1:])
