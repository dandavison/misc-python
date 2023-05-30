# https://leetcode.com/problems/range-sum-query-2d-mutable/submissions/

# Passes all tests
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.areas = {}
        self.fillAreas(0, 0)        

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.fillAreas(row, col)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.areas.get((row2, col2), 0)
            - self.areas.get((row2, col1 - 1), 0)
            - self.areas.get((row1 - 1, col2), 0)
            + self.areas.get((row1 - 1, col1 - 1), 0)
        )
        
    def fillAreas(self, row, col):
        for i in range(row, len(self.matrix)):
            for j in range(col, len(self.matrix[0])):
                self.areas[i, j] = (
                    self.matrix[i][j]
                    + self.areas.get((i, j - 1), 0)
                    + self.areas.get((i - 1, j), 0)
                    - self.areas.get((i - 1, j - 1), 0)                     
                )
