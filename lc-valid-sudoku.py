# https://leetcode.com/problems/valid-sudoku
from collections import defaultdict
from typing import List

BLANK = "."

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        subsquares, rows, columns = defaultdict(set), defaultdict(set), defaultdict(set)
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == BLANK:
                    continue
                subsquare_key = (i // 3, j // 3)
                for _set in [subsquares[subsquare_key], rows[i], columns[j]]:
                    if val in _set:
                        return False
                    _set.add(val)
        return True
