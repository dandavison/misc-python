# https://leetcode.com/problems/minimum-knight-moves/solution/
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        moves = [1+2j, 2+1j, 2-1j, 1-2j, -1-2j, -2-1j, -2+1j, -1+2j]
        target = x + y * 1j

        # BFS
        queue = deque([(0+0j, 0)]) # (position, n_moves)
        visited = set()

        while queue:
            pos, n_moves = queue.popleft()
            if pos == target:
                return n_moves
            else:
                for move in moves:
                    next_pos = pos + move
                    if next_pos not in visited:
                        queue.append((next_pos, n_moves + 1))
                        visited.add(next_pos)

        assert False, "Impossible"
