# https://leetcode.com/problems/course-schedule


class Solution:
    # passes
    # time: O(E + V^2)
    # space: (E + V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We can finish all courses iff the graph is a DAG
        nodes = list(range(numCourses))
        adj_list = make_adjacency_list(nodes, prerequisites)
        try:
            traverse_in_topological_sort_order(adj_list)
        except _CycleEncountered:
            return False
        else:
            return True
        

def traverse_in_topological_sort_order(adj_list):
    unvisited = set(adj_list.keys())
    visiting = set()
    
    def visit(node):
        if node not in unvisited:
            return
        elif node in visiting:
            raise _CycleEncountered
        else:
            visiting.add(node)
            for neighb in adj_list[node]:
                visit(neighb)
            visiting.remove(node)
            unvisited.remove(node)

    while unvisited:
        visit(next(iter(unvisited)))
    
        
class _CycleEncountered(Exception):
    pass


def make_adjacency_list(nodes, edges):
    adj_list = {node: [] for node in nodes}
    for a, b in edges:
        adj_list[a].append(b)
    return adj_list
