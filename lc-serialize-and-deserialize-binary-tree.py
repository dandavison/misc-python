# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import Iterable, Optional

class Codec:
    sep = ","

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.sep.join(self._serialize_val(val) for val in self._iter_vals_bfs(root))

    def deserialize(self, data):
        nodes = map(self._make_node, filter(bool, data.split(self.sep)))
        try:
            root = next(nodes)
        except StopIteration:
            return None
        else:
            queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            for attr in ["left", "right"]:
                try:
                    child = next(nodes)
                except StopIteration:
                    break
                else:
                    setattr(node, attr, child)
                    queue.append(child)
        return root

    @staticmethod
    def _serialize_val(val: Optional[int]) -> str:
        return "null" if val is None else str(val)

    def _make_node(self, str_val: str) -> Optional[TreeNode]:
        return None if str_val == "null" else TreeNode(int(str_val))

    def _iter_vals_bfs(self, node) -> Iterable[Optional[int]]:
        curr_depth = 0
        queue = deque([(node, curr_depth)])
        level = []
        while queue:
            node, depth = queue.popleft()
            if depth > curr_depth:
                if any(val is not None for val in level):
                    yield from iter(level)
                    level = []
                    curr_depth = depth
                else:
                    break
            if node:
                level.append(node.val)
                for child in [node.left, node.right]:
                    queue.append((child, depth + 1))
            else:
                level.append(None)



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
