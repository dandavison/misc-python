# https://leetcode.com/problems/path-sum-iii/
from collections import Counter

from typing import List, Optional

class Solution:
    # passes
    # This is `subarray_sum_equals_k` "done over a tree"
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> int:
        count = 0
        seen = Counter({0: 1})        

        def visit(node, cum_sum):
            if not node:
                return

            nonlocal count
            cum_sum += node.val
            count += seen[cum_sum - targetSum]

            seen[cum_sum] += 1
            visit(node.left, cum_sum)
            visit(node.right, cum_sum)
            seen[cum_sum] -= 1

        visit(root, 0)
        return count

class Solution_1:
    # from LC solutions/discussion
    def pathSum(self, root, targetSum):
        count = 0
        seen = Counter({targetSum: 1})
        
        def visit(node, cum_sum):
            if not node:
                return None

            nonlocal count
            cum_sum += node.val
            count += seen[cum_sum]  

            seen[cum_sum + targetSum] += 1
            visit(node.left, cum_sum)
            visit(node.right, cum_sum)
            seen[cum_sum + targetSum] -= 1

        
        visit(root, 0)
        
        return count





from collections import Counter

class Solution_2:
    # Times out
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = path_sums(root)
        return sums["extensible"][targetSum] + sums["non-extensible"][targetSum]
    

def path_sums(root: Optional[TreeNode]) -> dict:
    if not root:
        # print("null node")
        return {
            "extensible": Counter(),
            "non-extensible": Counter(),
        }
    sums_left = path_sums(root.left)
    sums_right = path_sums(root.right)
    
    sums_extensible = sums_left["extensible"] + sums_right["extensible"]
    sums_non_extensible = sums_left["non-extensible"] + sums_right["non-extensible"]
    
    return {
        # The "extensible" paths that this node passes to its parent are
        # (1) paths formed by extending its children's extensible paths to include itself, and
        # (2) the path consisting of itself only
        "extensible": extend_sums(sums_extensible, root.val) + Counter({root.val: 1}),
        # The "non-extensible" paths that this node passes to its parent are all the
        # non-extensible paths that its children have accumulated, and also the extensible paths
        # of its children (but without adding itself to these)
        "non-extensible": sums_extensible + sums_non_extensible
    }
    # print(f"Node(val={root.val}) returning: {return_}")


def extend_sums(counts: Counter, val: int) -> Counter:
    return Counter({(path_sum + val): count for path_sum, count in counts.items()})







