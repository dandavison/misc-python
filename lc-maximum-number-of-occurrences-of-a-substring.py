# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring


from collections import defaultdict, Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)
        n = len(s)
        for i in range(len(s)):
            for j in range(min(i + minSize, n), min(i + maxSize + 1, n + 1)):
                if minSize <= j - i <= maxSize + 1:
                    substr = s[i:j]
                    if len(set(substr)) <= maxLetters:
                        counts[substr] += 1
        return max(counts.values())


class Solution_2:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter()
        left = 0
        while True:
            right = left + minSize
            if right > len(s):
                break
            while right - left <= maxSize and right <= len(s):
                window = s[left:right]
                if len(set(window)) <= maxLetters:
                    counts[window] += 1
                right += 1
            left += 1
                
        return max(counts.values()) if counts else 0