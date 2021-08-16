'''

Given n nodes and edges of an undirected graph. How many triangles are there in this graph? Triangle is a cycle of length 3.

Example 1:

Input: n = 6, edges = [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]
Output: 7


ne^2

'''
def count_triangles_2(n, edges):
    edges_set, edges_dict = _create_lookup_structures(edges)

    triangles = set()
    for edge_1 in edges_set:
        for node in edge_1:
            for edge_2 in edges_dict[node]:
                if edge_1 != edge_2:
                    # Identify the edge that would make this a triangle
                    a, b = sorted(set(edge_1 + edge_2) - {node})
                    # If the edge (a, b) exists, then we have found a triangle
                    if (a, b) in edges_set:
                        triangles.add(_canonicalize((a, b, node)))
    return len(triangles)


def _create_lookup_structures(edges):
    edges_set = set()
    edges_dict = defaultdict(set)
    for edge in edges:
        edge = _canonicalize(edge)
        edges_set.add(edge)
        a, b = edge
        edges_dict[a].add(edge)
        edges_dict[b].add(edge)
    return edges_set, edges_dict


def _canonicalize(path):
    return tuple(sorted(path))



from collections import defaultdict

def count_triangles(n, edges):
    nodes = list(range(n))
    edges = _preprocess_edges(edges)
    triangles = set()
    for node in nodes: # n
        for triangle in _get_triangles(node, edges): # e^2
            triangles.add(triangle)
    return len(triangles)


def _preprocess_edges(edges):
    edge_dict = defaultdict(set)
    for (a, b) in edges:
        canonical_edge = [a, b]
        edge_dict[a].add(canonical_edge)
        edge_dict[b].add(canonical_edge)
    return edge_dict


def _get_triangles(node, edges):
    # e^2 worst case
    triangles = []
    node_edges = list(edges[node])
    for i in range(len(node_edges)):
        for j in range(i+1, len(node_edges)):
            edge_i, edge_j = node_edges[i], node_edges[j]
            a, b = sorted(set(edge_i + edge_j) - {node})
            if tuple(sorted([a, b])) in edges[a]:
                triangles.append(tuple(sorted([node, a, b])))
    return triangles

print(count_triangles_2(3, [[0, 1], [0, 2], [1, 2]]))  # 1
print(count_triangles_2(5, [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [2, 4]]))  # 2
print(count_triangles_2(6, [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]))  # 7
