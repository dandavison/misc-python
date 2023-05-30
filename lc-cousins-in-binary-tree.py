# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if x == y:
            return False
        else:
            dx, px = depth(x, root, 0, None)
            dy, py = depth(y, root, 0, None)
            return dx == dy and px != py
    

def depth(val, node, n, parent):
    if not node:
        return None
    elif node.val == val:
        return n, parent
    else:
        return (depth(val, node.left, n + 1, node) or
                depth(val, node.right, n + 1, node))
