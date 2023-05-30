# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together


from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        window_count = 0
        for i in range(window_size):
            window_count += data[i]
        max_window_count = window_count
        for i in range(window_size, len(data)):
            window_count += data[i]
            window_count -= data[i - window_size]
            max_window_count = max(window_count, max_window_count)
        return window_size - max_window_count
