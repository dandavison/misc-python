# https://leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        n_paths = {}
        if obstacleGrid[m - 1][n - 1] == 0:
            n_paths[m, n - 1] = 1  # artificial, so that n_paths[m-1, n-1] = 1
        
        for i in reversed(range(m)):
            row = obstacleGrid[i]
            for j in reversed(range(n)):
                if row[j] == 0:
                    n_paths[i, j] = n_paths.get((i + 1, j), 0) + n_paths.get((i, j + 1), 0)
        return n_paths.get((0, 0), 0)
    


class Solution_2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return dp_table(obstacleGrid)


# https://leetcode.com/problems/unique-paths-ii/


# The graph-traversal solutions time out
def enumerate_paths_in_graph(obstacleGrid):
    m = len(obstacleGrid)
    if m == 0:
        return 0
    n = len(obstacleGrid[0])
    if n == 0:
        return 0
    if obstacleGrid[0][0]:
        return 0
    graph = _make_adjacency_list(m, n, obstacleGrid)
    return sum(1 for _ in _enumerate_paths_dfs_recursive(graph, (0, 0), (m - 1, n - 1)))


def _enumerate_paths_dfs_recursive(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for neighbor in graph[start] - set(path):
        yield from _enumerate_paths_dfs_recursive(
            graph, neighbor, end, path + [neighbor]
        )


def _make_adjacency_list(m, n, grid):
    adj_list = {}
    for i in range(m):
        for j in range(n):
            adj_list[(i, j)] = moves = set()
            # right
            if i + 1 < m and not grid[i + 1][j]:
                moves.add((i + 1, j))
            # down
            if j + 1 < n and not grid[i][j + 1]:
                moves.add((i, j + 1))
    return adj_list


def dp_table(obstacleGrid):
    # m rows, n columns
    m = len(obstacleGrid)
    if m == 0:
        return 0
    n = len(obstacleGrid[0])
    if n == 0:
        return 0

    # initialize DP array
    n_paths = []
    for i in range(m):
        n_paths.append([0] * n)
    n_paths[m - 1][n - 1] = 1 - obstacleGrid[m - 1][n - 1]

    # print_rect(n_paths)
    # Fill the DP array
    i = m - 2
    j = n - 1
    while j >= 0:
        _fill_upwards(i, j, m, n, n_paths, obstacleGrid)
        # print_rect(n_paths)
        i = m - 1
        j -= 1
    return n_paths[0][0]


def _fill_upwards(
    i: int,
    j: int,
    m: int,
    n: int,
    n_paths: List[List[int]],
    obstacleGrid: List[List[int]],
):
    while i >= 0:
        if obstacleGrid[i][j]:
            # obstacle
            pass
        else:
            if i + 1 < m:
                # down
                n_paths[i][j] += n_paths[i + 1][j]
            if j + 1 < n:
                # right
                n_paths[i][j] += n_paths[i][j + 1]
        i -= 1


if False:

    def print_rect(rect):
        for row in rect:
            print(row)
        print()

    f = Solution().uniquePathsWithObstacles
    f([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
