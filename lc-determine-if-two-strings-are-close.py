# https://leetcode.com/problems/determine-if-two-strings-are-close


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # op 1: this means order doesn't matter
        # op 2: this means char identities don't matter
        return key(word1) == key(word2)

    

def key(word):
    return set(word), sorted(Counter(word).values())
