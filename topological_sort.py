import graph as g

def topologicalSort(myGraph) :
  nodes = []
  visiting = set()
  
  # make adjacency list
  adj = {}
  for k, v in myGraph.items():
    adj.setdefault(k, []).append(v)

  def dfs(node):
    assert node not in visiting, "Not a DAG"
    visiting.add(node)
    nodes.append(node)
    for neighbor in adj[node]:
      dfs(neighbor)
    visiting.remove(node)

  # roots are nodes with no parent
  roots = myGraph.keys() - set(myGraph.values())
  for root in roots:
    dfs(root)

  return nodes
