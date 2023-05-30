# https://leetcode.com/problems/unique-paths/solution/

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return enumerate_paths_in_graph(m, n)


def enumerate_paths_in_graph(m, n):
    graph = _make_adjacency_list(m, n)

    # DFS
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


def _enumerate_paths_dfs(graph, start, end):
    if start == end:
        yield [start]
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        for neighbor in graph[node] - set(path):
            extended_path = path + [neighbor]
            if neighbor == end:
                yield extended_path
            else:
                stack.append((neighbor, extended_path))


def _make_adjacency_list(m, n):
    adj_list = {}
    for i in range(m):
        for j in range(n):
            adj_list[(i, j)] = moves = set()
            # right
            if i + 1 < m:
                moves.add((i + 1, j))
            # down
            if j + 1 < n:
                moves.add((i, j + 1))
    return adj_list


def combinatorics_efficient(m, n):
    # The robot must make (m - 1) down moves and (n - 1) right moves
    # Order doesn't matter
    # So answer is choose(m + n - 2, m - 1)
    # Recall that choose(n, k) = n(n-1)...(n-(k-1))/k!
    # check: choose(n, 2) should be n(n-1)/2
    # ... correct
    _n = m + n - 2
    _k = m - 1
    ans = 1
    while _k:
        ans *= _n / _k
        _n -= 1
        _k -= 1
    return round(ans)


def combinatorics(m, n):
    # The robot must make (m - 1) down moves and (n - 1) right moves
    # Order doesn't matter
    # So answer is choose(m + n - 2, m - 1)
    # Recall that choose(n, k) = n(n-1)...(n-(k-1))/k!
    # check: choose(n, 2) should be n(n-1)/2
    # ... correct
    _n = m + n - 2
    _k = m - 1
    return int(math.factorial(_n) / (math.factorial(_n - _k) * math.factorial(_k)))
