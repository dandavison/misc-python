# https://leetcode.com/problems/range-sum-query-2d-immutable


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.computeAreas(matrix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.area(row2, col2)
                - self.area(row2, col1 - 1)
                - self.area(row1 - 1, col2)
                + self.area(row1 - 1, col1 - 1))
    
    def area(self, row, col):
        return self.areas.get((row, col), 0)

    def computeAreas(self, matrix):
        self.areas = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                self.areas[i, j] = val + self.areas.get((i, j-1), 0) + self.areas.get((i-1, j), 0) - self.areas.get((i-1, j-1), 0)
