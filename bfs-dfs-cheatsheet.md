# BFS vs DFS vs Recursion

**Core insight:** BFS and DFS are the same algorithm—only the container differs.

| Method | Container | Operation | Explores |
|--------|-----------|-----------|----------|
| BFS | Queue | `popleft()` | Level by level |
| DFS (iterative) | Stack | `pop()` | Deep first |
| DFS (recursive) | Call stack | `return` | Deep first |

---

## The Graph

```
        A           Level 0
       / \
      B   C         Level 1
     / \   \
    D   E   F       Level 2
```

---

## Code: Visit all reachable nodes

```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

# BFS — Queue (FIFO)
def bfs(start):
    queue, seen = deque([start]), {start}
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return result

# DFS — Stack (LIFO)
def dfs(start):
    stack, seen = [start], {start}
    result = []
    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return result

# DFS — Recursion (implicit stack)
def dfs_rec(start, seen=None):
    if seen is None:
        seen = set()
    seen.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in seen:
            result.extend(dfs_rec(neighbor, seen))
    return result

if __name__ == "__main__":
    print("bfs:    ", " ".join(bfs('A')),     " (level order)")
    print("dfs:    ", " ".join(dfs('A')),     " (deep first)")
    print("dfs_rec:", " ".join(dfs_rec('A')), " (deep first)")
```

**Output:**
```
bfs:     A B C D E F  (level order)
dfs:     A C F B E D  (deep first)
dfs_rec: A B D E C F  (deep first)
```

---

## When to use which?

| Use case | Choose |
|----------|--------|
| Shortest path (unweighted) | BFS |
| Does path exist? | Either |
| Explore all possibilities | DFS |
| Tree depth/backtracking | DFS or recursion |

---

## Appendix: Step-by-step traces

### BFS: Queue (FIFO) → `A B C D E F`

Process oldest first. Explores level-by-level like ripples in a pond.

```
Step  Visit   Queue (left=front)     Why
────  ─────   ──────────────────     ────────────────────────────
1     A       [B, C]                 Start at A, add its neighbors
2     B       [C, D, E]              B was added first, process it
3     C       [D, E, F]              C was next in line
4     D       [E, F]                 D has no neighbors
5     E       [F]                    E has no neighbors
6     F       []                     Done!
```

### DFS (stack): Stack (LIFO) → `A C F B E D`

Process newest first. Dives deep before backtracking.

```
Step  Visit   Stack (right=top)      Why
────  ─────   ──────────────────     ────────────────────────────
1     A       [B, C]                 Start at A, add its neighbors
2     C       [B, F]                 C was last added, pop it first
3     F       [B]                    F has no neighbors, backtrack
4     B       [D, E]                 Back to B, add its neighbors
5     E       [D]                    E was last added
6     D       []                     Done!
```

### DFS (recursive): Call Stack → `A B D E C F`

Same as stack DFS, but processes neighbors in order (first neighbor fully explored before second).

```
dfs_rec(A)
├── visit A
├── dfs_rec(B)          ← first neighbor, go deep
│   ├── visit B
│   ├── dfs_rec(D)
│   │   └── visit D
│   └── dfs_rec(E)
│       └── visit E
└── dfs_rec(C)          ← second neighbor, after B is done
    ├── visit C
    └── dfs_rec(F)
        └── visit F

Result: A B D E C F
```
