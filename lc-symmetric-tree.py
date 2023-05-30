# https://leetcode.com/problems/symmetric-tree/
from typing import Iterable, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            # Uses O(N) space; could do in O(1) space by zipping generators
            return list(get_values(root.left, flip=False)) == list(get_values(root.right, flip=True))

def get_values(node: Optional[TreeNode], flip: bool) -> Iterable[Optional[int]]:
    if node is None:
        yield None
    else:
        children = [node.left, node.right]
        if flip:
            children = reversed(children)
        for child in children:
            yield from get_values(child, flip)
        yield node.val
