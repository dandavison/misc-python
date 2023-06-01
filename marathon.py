# https://leetcode.com/discuss/interview-question/355686/google-marathon

# n students [0, ..., n-1] participate in a marathon.
# You are given an int array standings where standings[i] = j means that student j finished just before student i.
# standings[k] = -1 means that k is the first student.
# There are no ties. List out the students in the order in which they finished the marathon.
#
# Follow-up: now allow ties.
from typing import Any, Dict, List, TypeVar
from collections import defaultdict, deque

def marathon_no_ties(standings: List[int]) -> List[int]:
    edges = {left: right for right, left in enumerate(standings)}
    results = []
    curr = edges.pop(-1)
    while True:
        results.append(curr)
        if curr in edges:
            curr = edges[curr]
        else:
            # curr is last
            return results
    raise Exception("Invalid input")

def marathon_with_ties(standings) -> List[int]:
    adj_list = defaultdict(list)
    for right, left in enumerate(standings):
        adj_list[left].append(right)

    leftmost_group = adj_list.pop(-1)
    # BFS
    queue = deque(leftmost_group)
    results = []
    while queue:
        left = queue.popleft()
        results.append(left)
        queue.extend(adj_list[left])

    return results


def test1():
    expected = [[0, 1, 2]]
    standings =  [-1, 0, 1]
    for marathon in [marathon_no_ties, marathon_with_ties]:
        results = marathon(standings)
        assert results in expected, (marathon.__name__, standings, expected, results)


def test2():
    expected = [[1, 0, 2]]
    standings = [1, -1, 0]
    for marathon in [marathon_no_ties, marathon_with_ties]:
        results = marathon(standings)
        assert results in expected, (marathon.__name__, standings, expected, results)


def test3():
    expected = [[0, 1, 2, 3], [0, 2, 1, 3]]  # 1 and 2 are tied
    standings = [-1, 0, 0, 2]
    marathon = marathon_with_ties
    results = marathon(standings)
    assert results in expected, (marathon.__name__, standings, expected, results)

def test4():
    expected = [[0, 1, 2, 3, 4],
                [1, 0, 2, 3, 4],
                [0, 1, 3, 2, 4],
                [1, 0, 3, 2, 4]] # {0, 1} and {1, 2} are two tied groups

    for standings in [[-1, -1, 0, 0, 3],
                      [-1, -1, 0, 1, 3],
                      [-1, -1, 1, 0, 2],
                      [-1, -1, 1, 1, 2]]:
        marathon = marathon_with_ties
        results = marathon(standings)
        assert results in expected, (marathon.__name__, standings, expected, results)


for test in [test1, test2, test3, test4]:
    print(test.__name__)
    test()
