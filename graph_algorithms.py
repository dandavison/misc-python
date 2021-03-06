from collections import defaultdict, deque
from typing import Any, List, Tuple


class Queue:
    def __init__(self, items):
        self.queue = deque(items.copy())

    def add(self, item):
        self.queue.append(item)

    def retrieve(self):
        return self.queue.popleft()

    def __bool__(self):
        return bool(self.queue)

    def __repr__(self):
        return repr(self.queue)


class Stack:
    def __init__(self, items):
        self.stack = items.copy()

    def add(self, item):
        self.stack.append(item)

    def retrieve(self):
        return self.stack.pop()

    def __bool__(self):
        return bool(self.stack)

    def __repr__(self):
        return repr(self.stack)


class Graph:
    # Partially implement networkx API
    # https://networkx.org/documentation/stable/tutorial.html
    _directed = False

    def __init__(self):
        self._edges = []

    def connected_component_bfs(self, root):
        return self._connected_component_traversal(root, Queue)

    def connected_component_dfs(self, root):
        return self._connected_component_traversal(root, Stack)

    def all_paths_bfs(self, start, end):
        return self._all_paths_traversal(start, end, Queue)

    def all_paths_dfs(self, start, end):
        return self._all_paths_traversal(start, end, Stack)

    def shortest_path(self, start, end):
        return next(self.all_paths_bfs(start, end), None)

    def all_paths_dfs_recursive(self, start, end, path=None):
        if path is None:
            path = [start]
        if start == end:
            yield path
        for neighbor in self._adjacency_list[start] - set(path):
            yield from self.all_paths_dfs_recursive(neighbor, end, path + [neighbor])

    def _all_paths_traversal(self, start, end, container_cls):
        container = container_cls([(start, [start])])
        while container:
            node, path = container.retrieve()
            for neighbour in self._adjacency_list[node] - set(path):
                extended_path = path + [neighbour]
                if neighbour == end:
                    yield extended_path
                else:
                    container.add((neighbour, extended_path))

    def _connected_component_traversal(self, root, container_cls):
        if not self._adjacency_list:
            return
        container, seen = container_cls([root]), {root}
        component = []
        while container:
            node = container.retrieve()
            component.append(node)
            for neighbour in self._adjacency_list[node] - seen:
                container.add(neighbour)
                seen.add(neighbour)
        return component

    def connected_component_dfs_recursive(self, root, component=None, seen=None):
        if not root:
            return
        if seen is None:
            seen = set()
        if component is None:
            component = []
        component.append(root)
        seen.add(root)
        for neighbour in self._adjacency_list[root] - seen:
            self.connected_component_dfs_recursive(neighbour, component, seen)
        return component

    def add_edges_from(self, edges: List[Tuple[Any, Any]]):
        if self._directed:
            self._edges.extend({edge for edge in edges})
        else:
            self._edges.extend({tuple(sorted(edge)) for edge in edges})
        self._adjacency_list = self._make_adjacency_list()

    def _make_adjacency_list(self):
        adj = defaultdict(set)
        for u, v in self._edges:
            adj[u].add(v)
            adj[v].add(u)
        return dict(adj)


if __name__ == "__main__":
    G1 = Graph()
    G1.add_edges_from(
        [("A", "B"), ("B", "C"), ("B", "D"), ("C", "F"), ("D", "E"), ("E", "F")]
    )
    print("\nBFS\n---")
    print(G1.connected_component_bfs("A"))

    print("\nDFS\n---")
    print(G1.connected_component_dfs("A"))

    print("\nDFS rec\n-------")
    print(G1.connected_component_dfs_recursive("A"))

    print("\nall paths BFS\n-------")
    for path in G1.all_paths_bfs("A", "F"):
        print(path)

    print("\nall paths DFS\n-------")
    for path in G1.all_paths_dfs("A", "F"):
        print(path)

    print("\nall paths DFS rec\n-------")
    for path in G1.all_paths_dfs_recursive("A", "F"):
        print(path)

    print("\nshortest path\n-------")
    print(G1.shortest_path("A", "F"))
