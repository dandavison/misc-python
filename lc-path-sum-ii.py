"""
https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum, return all
root-to-leaf paths where the sum of the node values in the path equals
targetSum. Each path should be returned as a list of the node values, not node
references.

A root-to-leaf path is a path starting from the root and ending at any leaf
node. A leaf is a node with no children.
"""
from typing import List, Optional, Generator

class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> List[List[int]]:
        return list(_all_paths_to_leaves(root, targetSum))


def _all_paths_to_leaves(node, targetSum):
    if node is None:
        return
    elif not (node.left or node.right):
        if node.val == targetSum:
            yield [node.val]
    else:
        for child in [node.left, node.right]:
            for child_path in _all_paths_to_leaves(child, targetSum - node.val):
                yield [node.val] + child_path


class Solution_2:
    # passes; recursive
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> List[List[int]]:
        paths = []

        def visit(node, path, path_sum):
            if not node:
                return
            path = path + [node.val]
            path_sum += node.val
            if not (node.left or node.right):
                if path_sum == targetSum:
                    paths.append(path)
            else:
                visit(node.left, path, path_sum)
                visit(node.right, path, path_sum)
            
        visit(root, [], 0)
        return paths


class Solution_1:
    # passes; stack-based DFS
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val], root.val)]
        paths = []
        while stack:
            node, path, path_sum = stack.pop()        
            if not node.left and not node.right and path_sum == targetSum:
                paths.append(path)
            else:
                if node.left:
                    stack.append((node.left, path + [node.left.val], path_sum + node.left.val))
                if node.right:
                    stack.append((node.right, path + [node.right.val], path_sum + node.right.val))

        return paths

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

