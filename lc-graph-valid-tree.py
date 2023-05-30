"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""
from typing import List, TypeVar, Set, Dict, Tuple

class CycleDetected(Exception): pass

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # An undirected graph is a tree iff it is acyclic and connected
        nodes = set(range(n))
        adj_list = make_adjacency_list(nodes, edges)

        visited = set()

        def visit(node, from_node):
            if node in visited:
                raise CycleDetected
            visited.add(node)
            for neighb in adj_list[node]:
                if neighb != from_node:
                    visit(neighb, node)
        try:
            visit(next(iter(nodes)), None)
        except CycleDetected:
            return False

        return visited == nodes


T = TypeVar("T")

def make_adjacency_list(nodes: Set[T], edges: List[Tuple[T, T]]) -> Dict[T, List[T]]:
    adj_list = {v: [] for v in nodes}
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    return adj_list

print(Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
