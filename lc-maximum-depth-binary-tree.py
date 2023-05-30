from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionDFSRecursiveConcurrent:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global_min = float("inf")

        def searcher(node):
            if not node or node.depth >= global_min:
                return
            if not node.left and not node.right:
                with lock():
                    global_min = min(global_min, node.depth)
            else:
                for child in [node.left, node.right]:
                    if child:
                        thread_pool_or_event_loop.submit(lambda: searcher(child))

        thread_pool_or_event_loop.submit(lambda: searcher(root))



class SolutionDFSRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, node, depth):
        if not node:
            return depth
        else:
            return max(self.helper(node.left, depth + 1), self.helper(node.right, depth + 1))

Solution = SolutionDFSRecursive

class SolutionDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs():
            nonlocal max_depth
            stack = []
            if root:
                stack.append((root, 1))
            while stack:
                node, depth = stack.pop()
                max_depth = max(depth, max_depth)
                for child in [node.left, node.right]:
                    if child:
                        stack.append((child, depth + 1))

        dfs()
        return max_depth



class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0

        def bfs():
            nonlocal max_depth
            queue = deque([])
            if root:
                queue.append((root, 1))
            while queue:
                node, depth = queue.popleft()
                max_depth = max(depth, max_depth)
                for child in [node.left, node.right]:
                    if child:
                        queue.append((child, depth + 1))

        bfs()
        return max_depth
