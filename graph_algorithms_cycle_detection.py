class CycleDetected(Exception):
    pass


def has_cycle_undirected(graph):
    visited = set()

    def visit(node, parent=None):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor in visited:
                if neighbor != parent:
                    raise CycleDetected()
            else:
                visit(neighbor, node)

    arbitrary_node = next(iter(graph.keys()))
    try:
        visit(arbitrary_node)
        return False
    except CycleDetected:
        return True


print(has_cycle_undirected({"A": ["B"], "B": ["A", "C"], "C": ["B"]}))
print(has_cycle_undirected({"A": ["B"], "B": ["A", "C"], "C": ["B", "A"]}))
