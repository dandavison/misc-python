# https://leetcode.com/problems/letter-combinations-of-a-phone-number


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # Suppose digits is 285
        # We think of this as a tree of height 3
        # The level 0 node (root) has children [a, b, c]
        # Each node at level 1 has children [d, e, f]
        # Rather than form this tree explicitly, we form it in the stack via recursion.
        # In other words, letterCombinations(digits) is formed by considering
        # all possibilities for the first, and all possibilities for the
        # remainder
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(digit_to_letters[digits[0]])
        else:
            combs = []
            for letter in digit_to_letters[digits[0]]:
                for comb in self.letterCombinations(digits[1:]):
                    combs.append(letter + comb)
            return combs
