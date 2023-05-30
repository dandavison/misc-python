# https://leetcode.com/problems/interleaving-string/

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # return recursion_on_string_slices(s1, s2, s3)
        return bfs(s1, s2, s3)


# https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
#
# Define a grid with s1 and s2 written along the top and side, i.e. in which
# cell (i, j) contains (s1[i], s2[j]). Now consider the graph formed by the
# points of intersection of the lines of this grid. We start in the top-left,
# i.e. with no characters consumed so far from either string. An edge exists to
# the right (consume first char from s1) and down (consume first char from s2).
# s3 is an interleaving of s1 and s2 if a path exists from the top-left to
# bottom-right such that the edges of the path spell the word s3.


from collections import deque


def bfs(s1, s2, s3):
    # In BFS we use a queue: i.e. FIFO; we process oldest-encountered nodes first.
    m, n, p = len(s1), len(s2), len(s3)
    if p != m + n:
        return False
    queue, seen = deque([(0, 0)]), set([(0, 0)])
    while queue:
        i, j = queue.popleft()
        if (i, j) == (m, n):
            return True
        right = (i + 1, j)
        if i < m and right not in seen and s1[i] == s3[i + j]:
            queue.append(right)
            seen.add(right)
        down = (i, j + 1)
        if j < n and down not in seen and s2[j] == s3[i + j]:
            queue.append(down)
            seen.add(down)
    return False


def dfs(s1, s2, s3):
    # Passes all tests
    # In DFS we use a stack: i.e. LIFO; we process recently-encountered nodes first.
    m, n, p = len(s1), len(s2), len(s3)
    if p != m + n:
        return False
    stack, seen = [(0, 0)], set([(0, 0)])
    while stack:
        i, j = stack.pop()
        if (i, j) == (m, n):
            return True
        right = (i + 1, j)
        if i < m and right not in seen and s1[i] == s3[i + j]:
            stack.append(right)  # type: ignore
            seen.add(right)
        down = (i, j + 1)
        if j < n and down not in seen and s2[j] == s3[i + j]:
            stack.append(down)  # type: ignore
            seen.add(left)
    return False


def dfs_recursive(s1, s2, s3):
    # DNW
    m, n, p = len(s1), len(s2), len(s3)
    if p != m + n:
        return False
    if p == 0:
        return True
    if m and s1[1] == s3[1]:
        if dfs_recursive(s1[1:], s2, s3[1:]):
            return True
    if n and s2[1] == s3[1]:
        if dfs_recursive(s1, s2[1:], s3[1:]):
            return True
    return False


@functools.cache
def recursion_on_string_slices(s1, s2, s3):
    # Passes all tests

    # s3 is an interleaving of s1 and s2 if s3[0] comes from one of them and
    # s3[1:] is an interleaving of the remainders.
    if not s3:
        return not (s1 or s2)
    else:
        return bool(
            s1
            and s3[0] == s1[0]
            and recursion_on_string_slices(s1[1:], s2, s3[1:])
            or s2
            and s3[0] == s2[0]
            and recursion_on_string_slices(s1, s2[1:], s3[1:])
        )


if False:
    f = Solution().isInterleave

    print(f("a", "b", "a"))
