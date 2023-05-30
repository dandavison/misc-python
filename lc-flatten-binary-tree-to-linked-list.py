"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child
pointer points to the next node in the list and the left child pointer is always
null. The "linked list" should be in the same order as a pre-order traversal of
the binary tree.
"""
from typing import Optional


class Solution:
    def flatten(self, root: Optional["TreeNode"]) -> None:
        # Do not return anything, modify root in-place instead.
        nodes = list(preorder(root))
        for i in range(1, len(nodes)):
            nodes[i-1].left = None
            nodes[i-1].right = nodes[i]
            

def preorder(node):
    if node:
        yield node
        yield from preorder(node.left)
        yield from preorder(node.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

