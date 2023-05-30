# https://leetcode.com/problems/balanced-binary-tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return getHeightIfBalanced(root) is not None
                
def getHeightIfBalanced(root: Optional[TreeNode], height=0) -> Optional[int]:
    if root is None:
        return height
    else:
        if (h1 := getHeightIfBalanced(root.left, height + 1)) is None:
            return None
        if (h2 := getHeightIfBalanced(root.right, height + 1)) is None:
            return None
        
        if h2 > h1:
            h1, h2 = h2, h1
        if h1 - h2 > 1:
            return None
        else:
            return h1
