from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def visit(p, q):
            if not (p and q):
                return not (p or q)
            else:
                return p.val == q.val and visit(p.left, q.left) and visit(p.right, q.right)
        return visit(p, q)
