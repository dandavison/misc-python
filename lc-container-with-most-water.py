# https://leetcode.com/problems/container-with-most-water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            hi = height[i]
            for j in range(i, n):
                max_area = max(max_area, (j - i) * min(hi, height[j]))
        return max_area
