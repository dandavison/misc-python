# https://leetcode.com/problems/construct-quad-tree


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        vals = set(val for row in grid for val in row)
        if len(vals) == 1:
            isLeaf = True
            [val] = vals
        else:
            isLeaf = False
            val = False
        
        n = len(grid) // 2
        topLeft = self.construct([row[:n] for row in grid[:n]]) if not isLeaf else None
        topRight = self.construct([row[n:] for row in grid[:n]]) if not isLeaf else None
        bottomLeft = self.construct([row[:n] for row in grid[n:]]) if not isLeaf else None
        bottomRight = self.construct([row[n:] for row in grid[n:]]) if not isLeaf else None
        return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
