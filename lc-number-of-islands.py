# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid) -> int:

        grid = {
            (i, j): val
            for i, row in enumerate(grid)
            for j, val in enumerate(row)
        }
        
        def dfs(cell):
            grid[cell] = "0"
            for neighbor in get_neighbors(cell):
                if grid.get(neighbor) == "1":
                    dfs(neighbor)
        
        n_islands = 0
        
        for cell in grid:
            if grid[cell] == "1":
                dfs(cell)
                n_islands += 1
                
        return n_islands
    
def get_neighbors(cell):
    i, j = cell
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]


class Solution1:
    def numIslands(self, grid) -> int:
        moves = [1j ** k for k in [1, 2, 3, 4]]
        grid = {
            (x + y * 1j): int(grid[x][y])
            for x in range(len(grid))
            for y in range(len(grid[0]))
        }
        n = 0
        for cell in grid:
            if grid[cell]:
                dfs_rec(cell, grid, moves)
                n += 1
        return n


def dfs_rec(cell, grid, moves):
    if not grid.get(cell):
        return
    grid[cell] = 0
    for move in moves:
        dfs_rec(cell + move, grid, moves)


def dfs(cell, grid, moves):
    stack = [cell]
    while stack:
        cell = stack.pop()
        if not grid.get(cell):
            continue
        grid[cell] = 0
        stack.extend(cell + move for move in moves)

if False:
    f = Solution().numIslands
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    f(grid)
