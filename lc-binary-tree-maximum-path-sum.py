# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List, Generator
import itertools


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        print("paths")
        for path in enumerate_root_to_tip_paths(root.right if root else None):
            print(path)
        print("_____________")
        # return max(max_subarray_sum(path) for path in enumerate_root_to_tip_paths(root))


def enumerate_tip_to_tip_paths(node):
    if not node:
        yield []
        return
    left_paths = enumerate_root_to_tip_paths(node.left)
    right_paths = enumerate_root_to_tip_paths(node.right)
    for l_path in left_paths:
        for r_path in right_paths:
            yield list(reversed(l_path)) + [node.val] + r_path


def enumerate_root_to_tip_paths(node):
    # print(node.val if node else "null")
    if not node:
        yield []
        return
    for path in itertools.chain(
        enumerate_root_to_tip_paths(node.left), enumerate_root_to_tip_paths(node.right)
    ):
        yield [node.val] + path


def max_subarray_sum(arr):
    # "Kadane's algorithm"
    global_max = local_max = 0
    for el in arr:
        local_max = el + max(local_max, 0)
        global_max = max(local_max, global_max)
    return global_max


if True:

    tree = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=3, left=None, right=None),
            right=TreeNode(val=4, left=None, right=None),
        ),
        right=TreeNode(val=5, left=None, right=TreeNode(val=6, left=None, right=None)),
    )

    f = Solution().maxPathSum
    print(f(tree))
