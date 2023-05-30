# https://leetcode.com/problems/maximal-square
from typing import List


class Solution:
    def maximalSquare_dp(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        d = [[0] * (n + 1)] * (m + 1)
        _max = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if int(matrix[i - 1][j - 1]):
                    d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j - 1], d[i - 1][j])
                    _max = max(_max, d[i][j])
        return _max ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_so_far = 0
        max_possible = min(len(matrix), len(matrix[0]))
        for i, row in enumerate(matrix):
            for j, el in enumerate(row):
                el = int(el)
                if el:
                    max_size_here = find_max_size(i, j, matrix, max_possible)
                    print(f"max_size = {max_size_here} at {i} {j}")
                    max_so_far = max(max_so_far, max_size_here)
        return max_so_far ** 2


def find_max_size(i, j, matrix, max_possible):
    for k in range(1, max_possible + 1):
        if not square_exists(i, j, matrix, k + 1):
            return k
    return max_possible


def square_exists(i, j, matrix, size):
    if i + size > len(matrix) or j + size > len(matrix[0]):
        return False
    for row in range(i, min(i + size, len(matrix))):
        if not all(map(int, matrix[row][j : j + size])):
            return False
    return True


if __name__ == "__main__":
    # print(
    #     Solution().maximalSquare(
    #         [
    #             ["1", "0", "1", "0", "0"],
    #             ["1", "0", "1", "1", "1"],
    #             ["1", "1", "1", "1", "1"],
    #             ["1", "0", "0", "1", "0"],
    #         ]
    #     )
    # )
    print(Solution().maximalSquare([["0", "1"], ["0", "1"]]))
