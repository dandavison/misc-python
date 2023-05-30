# https://leetcode.com/problems/clone-graph


from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        # Passes lc tests

        clones = {}

        def clone(node) -> Node:
            if node is None:
                return None
            if node not in clones:
                clones[node] = Node(val=node.val)
                clones[node].neighbors=[clone(n) for n in node.neighbors]
            return clones[node]

        return clone(node)


class Solution_1:
    def cloneGraph(self, node: 'Node') -> 'Node':
    clone = Node(node.val)
    stack, seen = [(node, clone)], {id(node)}
    while stack:
        _node, _clone = stack.pop()
        _clone.neighbors = [Node(v.val) for v in _node.neighbors]
        for neighbor in _node.neighbors:
            if id(neighbor) not in seen:
                stack.append((neighbor, Node(neighbor.val)))
                seen.add(id(neighbor))
    return clone
