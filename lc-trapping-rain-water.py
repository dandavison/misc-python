# https://leetcode.com/problems/trapping-rain-water


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        unresolved = {}
        for i, block_height in enumerate(height):
            for level in range(block_height):
                if level in unresolved:
                    volume += i - unresolved[level] - 1
                unresolved[level] = i
        return volume
