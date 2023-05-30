# https://leetcode.com/problems/word-search-ii


import functools
from typing import List

VISITING = "VISITING"


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        return [w for w in words if self.exists(w)]

    def exists(self, word):
        return any(
            self.exists_at(word, i, j)
            for i in range(len(self.board))
            for j in range(len(self.board[0]))
        )

    @functools.cache
    def exists_at(self, word, i, j):
        board = self.board
        if not word:
            return True
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
        if board[i][j] == VISITING:
            return False
        head, tail = word[0], word[1:]
        if board[i][j] == head:
            board[i][j] = VISITING
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if self.exists_at(tail, ii, jj):
                    board[i][j] = head
                    return True
            board[i][j] = head
        return False
