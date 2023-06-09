from collections import deque

graph = {
    "a": [("b", 7), ("c", 3)],
    "b": [("a", 7), ("d", 2), ("e", 6)],  # ("c", 1), 
    "c": [("a", 3), ("d", 2)],            # ("b", 1), 
    "d": [("b", 2), ("c", 2), ("e", 4)],
    "e": [("b", 6), ("d", 4)],
}


def dfs(start):
    stack, visited = [start], {start}

    # path = [a, c, d, e, b]
    # stack = []
    # visited = {a, b, c, d, e}
    while stack:
        node = stack.pop()
        print("visiting", node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)


def dfs_recursive(start):
    visited = set()

    def dfs(node):
        print("visiting", node)
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)


def bfs(start):
    queue, visited = deque([start]), {start}

    while queue:
        node = queue.popleft()
        print("visiting", node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def dijkstra(start):
    def _dijkstra():
        queue = deque([start])
        
        while queue:
            prev = queue.popleft()
            w_prev, _ = distances[prev]
            for w, neighbor in adj_list[prev]:
                if distances[neighbor] == float("inf"):
                    queue.append(neighbor)
                distances[neighbor] = min(distances[neighbor],
                                            (w + w_prev, prev))



print("should be", ["a", "c", "d", "e", "b"])
dfs("a")

print("should be", ["a", "b", "d", "c", "e"])
dfs_recursive("a")

print("should be", ["a", "b", "c", "d", "e"])
bfs("a")
