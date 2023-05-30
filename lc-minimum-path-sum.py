# https://leetcode.com/problems/minimum-path-sum


# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.


from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        # Initialize
        # sums[i][j] = min sum of all paths starting at (i, j)
        sums = []
        for i in range(m):
            sums.append([None] * n)

        sums[m-1][n-1] = grid[m-1][n-1]

        # Fill up columns
        i = m - 2
        j = n - 1
        while j >= 0:
            while i >= 0:
                candidates = []
                if i + 1 < m:
                    # down
                    candidates.append(grid[i][j] + sums[i + 1][j])
                if j + 1 < n:
                    # right
                    candidates.append(grid[i][j] + sums[i][j + 1])
                sums[i][j] = min(candidates)
                i -= 1
            j -= 1
            i = m - 1
        return sums[0][0]

