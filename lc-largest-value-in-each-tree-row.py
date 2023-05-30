# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # By Catherine
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest_values = []

        queue = deque([(0, root)])
        while queue:
            level, node = queue.popleft()
            if node is None:
                continue

            next_level = level + 1

            if len(largest_values) == level:
                largest_values.append(node.val)
            else:
                largest_values[level] = max([largest_values[level], node.val])

            queue.append((next_level, node.left))
            queue.append((next_level, node.right))

        return largest_values
