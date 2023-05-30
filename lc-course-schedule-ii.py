# https://leetcode.com/problems/course-schedule-ii


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return topological_sort(list(range(numCourses)), prerequisites) 


def topological_sort(nodes, edges):
    adj_list = make_adjacency_list(nodes, edges)
    
    unvisited = set(nodes)
    visiting = set()
    sorted_nodes = []
    
    class CycleDetected(Exception):
        pass
    
    def dfs(node):
        if node not in unvisited:
            return
        if node in visiting:
            raise CycleDetected
        visiting.add(node)
        for neighb in adj_list[node]:
            dfs(neighb)
        visiting.remove(node)
        unvisited.remove(node)
        sorted_nodes.append(node)
    
    while unvisited:
        try:
            dfs(next(iter(unvisited)))
        except CycleDetected:
            return []
        
    return sorted_nodes


def make_adjacency_list(nodes, edges):
    adj_list = {v: [] for v in nodes}
    for u, v in edges:
        adj_list[u].append(v)
    return adj_list
