# https://leetcode.com/problems/spiral-order


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        grid = {x - y * 1j: val
                for y, row in enumerate(matrix)
                for x, val in enumerate(row)}
        delta = 1
        cell = 0
        output = []
        while cell in grid:
            val = grid.pop(cell)
            output.append(val)
            if cell + delta not in grid:
                delta *= -1j                
            cell += delta

        return output


if False:
    f = Solution().spiralOrder
    print(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
