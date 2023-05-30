# https://leetcode.com/problems/unique-paths-iii/
from typing import List

VISITING = -2


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        Return the number of 4-directional walks from the starting square
        to the ending square, that walk over every non-obstacle square exactly once.
        """
        # time: O(3^N) since 3 possible directions at each step
        # space: O(N) for grid, and O(N) for call stack

        moves = [1j ** k for k in range(4)]
        start, end, cells, n_nodes = initialize(grid)

        n_paths = 0

        def dfs(cell, path):
            nonlocal n_paths
            if cell == end and len(path) == n_nodes:
                n_paths += 1
                return
            val = cells[cell]
            cells[cell] = VISITING
            for move in moves:
                neighbor = cell + move
                if neighbor in cells and cells[neighbor] != VISITING:
                    dfs(neighbor, path + [neighbor])
            cells[cell] = val

        dfs(start, [start])
        return n_paths


def initialize(grid):
    start = end = None
    n_nodes = 0
    cells = {}
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            z = x + y * 1j
            if val >= 0:
                cells[z] = val
                n_nodes += 1
            if val == 1:
                start = z
            elif val == 2:
                end = z

    return start, end, cells, n_nodes
