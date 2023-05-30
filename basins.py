"""
A group of farmers has some elevation data, and we're going to help them
understand how rainfall flows over their farmland. We'll represent the land as
a two dimensional array of altitudes and use the following model, based on the
idea that water flows downhill:

If a cell's four neighbouring cells all have higher altitudes, we call this
cell a sink; water collects in sinks.

Otherwise, water will flow to the neighbouring cell with the lowest altitude.
If a cell is not a sink, you may assume it has a unique lowest neighbor and
that this neighbor will be lower than the cell. Cells that drain into the same
sink - directly or indirectly - are said to be part of the same basin.

Your challenge is to partition the map into basins. In particular, given a map
of elevations, your code should partition the map into basins and output the
sizes of the basins, in descending order.

Assume the elevation maps are square. Input will begin with a line with one
integer, S, the height (and width) of the map. The next S lines will each
contain a row of the map, each with S integers - the elevations of the S cells
in the row . Some farmers have small land plots such as the examples below ,
while some have larger plots. However, in no case will a farmer have a plot of
land larger than S = 5000.

Your code should output a space separated list of the basin sizes, in
descending order. (Trailing spaces are ignored.)

A few examples are below .

Input:
3
1 5 2
2 4 7
3 6 9
Output:
7 2
The basins, labeled with A's and B's, are:
A A B
A A B
A A A

Input:
1
10
Output:
1
There is only one basin in this case.

Input:
5
1 0 2 5 8
2 3 4 7 9
3 5 7 8 9
1 2 5 4 2
3 3 5 2 1
Output:
11 7 7
The basins, labeled with A's, B's, and C's, are:
A A A A A
A A A A A
B B A C C
B B B C C
B B C C C

Input:
4
0 2 1 3
2 1 0 4
3 3 3 3
5 5 2 1
Output:
7 5 4
The basins, labeled with A's, B's, and C's, are:
A A B B
A B B B
A B B C
A C C C
"""

from typing import List
from typing import NewType
from typing import Optional
from sys import stdin

import networkx as nx

Land = NewType("Land", List[List[Optional[int]]])


def read_land(s: int) -> Land:
    """Return an array of dimension (s+1)x(s+1), padded with sentinel values"""
    rows: Land = [[None] * (s + 1)]
    for i in range(s):
        row = [None]
        row.extend(map(int, stdin.readline().split()))
        row.append(None)
        rows.append(row)
    rows.append([None] * (s + 1))
    return rows


def make_graph(land: Land) -> nx.DiGraph:
    """An edge exists from a to b if water flows from a to b."""
    g = nx.DiGraph()
    for i in range(1, len(land) - 1):
        for j in range(1, len(land) - 1):
            here = to = (i, j)
            to_elevation = land[i][j]
            neighbour_indices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for (ii, jj) in neighbour_indices:
                candidate_elevation = land[ii][jj]
                if candidate_elevation is not None:
                    if candidate_elevation < to_elevation:
                        to_elevation = candidate_elevation
                        to = (ii, jj)
                if to == here:
                # sink
                g.add_node(here)
            else:
                g.add_edge(here, to)
    return g


S = int(stdin.readline())
land = read_land(S)
graph = make_graph(land)
basins = nx.weakly_connected_components(graph)
print(" ".join(str(len(basin)) for basin in sorted(basins, key=len, reverse=True)))

input1 = """3
1 5 2
2 4 7
3 6 9
"""

input2 = """1
10
"""

input3 = """5
1 0 2 5 8
2 3 4 7 9
3 5 7 8 9
1 2 5 4 2
3 3 5 2 1
"""

input4 = """4
0 2 1 3
2 1 0 4
3 3 3 3
5 5 2 1
"""

