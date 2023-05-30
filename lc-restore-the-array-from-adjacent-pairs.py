# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs


from collections import Counter

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph, root = build_graph(adjacentPairs)

        array = []
        visited = set()

        def dfs(u):
            array.append(u)
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        dfs(root)
        return array
    

def dfs_stack(graph, root):
    stack, seen = [root], {root}
    path = [root]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in seen:
                stack.append(neighbor)
                seen.add(neighbor)
                path.append(neighbor)
    return path
    
    
def build_graph(pairs):
    adjacency = {}
    counts = Counter()
    for a, b in pairs:
        counts[a] += 1
        counts[b] += 1
        adjacency.setdefault(a, []).append(b)
        adjacency.setdefault(b, []).append(a)

    root = next(k for k, v in counts.items() if v == 1)
    
    return adjacency, root
    