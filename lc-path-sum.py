# https://leetcode.com/problems/path-sum


from typing import Optional

class Solution:
    # passes
    def hasPathSum(self, root: Optional["TreeNode"], targetSum: int) -> bool:
        return dfs(root, targetSum)

def dfs(node, targetSum):
    if not node:
        return False
    elif not node.left and not node.right:
        return targetSum == node.val
    else:
        return (
            dfs(node.left, targetSum - node.val) or
            dfs(node.right, targetSum - node.val)
        )
