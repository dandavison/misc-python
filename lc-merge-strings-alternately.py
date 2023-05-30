# https://leetcode.com/problems/merge-strings-alternately


from itertools import chain, zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        else:
            return word1[0] + self.mergeAlternately(word2, word1[1:])

    def mergeAlternately_2(self, word1: str, word2: str) -> str:
        words = [iter(word1), iter(word2)]
        exhausted = [False, False]
        output = []
        while not all(exhausted):
            for i in [0, 1]:
                if not exhausted[i]:
                    try:
                        output.append(next(words[i]))
                    except StopIteration:
                        exhausted[i] = True
        return "".join(output)
    
    def mergeAlternately_3(self, word1: str, word2: str) -> str:
        return "".join(c for c in chain.from_iterable(zip_longest(word1, word2)) if c)
