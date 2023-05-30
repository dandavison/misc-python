# https://leetcode.com/problems/word-search/
import functools
from typing import List

VISITING = "VISITING"


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board = tuple(map(tuple, board))
        nrows, ncols = len(board), len(board[0])
        for i in range(nrows):
            for j in range(ncols):
                if _exist(word, i, j, board):
                    return True
        return False


def _exist(word, i, j, board):
    if not word:
        return True
    nrows, ncols = len(board), len(board[0])
    if not ((0 <= i < nrows) and (0 <= j < ncols)):
        return False
    if board[i][j] == VISITING:
        return False
    if board[i][j] != word[0]:
        return False
    else:
        # print(word, i, j, board[i][j])
        val = board[i][j]
        board[i][j] = VISITING
        exists = (
            _exist(word[1:], i + 1, j, board)
            or _exist(word[1:], i - 1, j, board)
            or _exist(word[1:], i, j + 1, board)
            or _exist(word[1:], i, j - 1, board)
        )
        board[i][j] = val
        return exists


if False:
    f = Solution().exist
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    for row in board:
        print(row)
    print(f(board, word))
