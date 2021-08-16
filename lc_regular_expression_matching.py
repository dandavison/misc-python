# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4:
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

# Example 5:
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false


class Machine:
    def __init__(self, p: str):
        self.p = p

    def accepts(self, c: str) -> bool:
        if c == ".":
            self.advance()
            return True
        elif c == "*":
            



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        machine = Machine(p)
        for c in s:
            if not machine.accepts(c):
                return False
        return True