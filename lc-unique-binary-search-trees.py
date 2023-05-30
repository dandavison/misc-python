# https://leetcode.com/problems/unique-binary-search-trees/submissions/
import functools


class Solution:
    @functools.cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        n_trees = 0
        for n_left in range(n):
            n_right = n - n_left - 1
            n_trees += self.numTrees(n_left) * self.numTrees(n_right)
        return n_trees
