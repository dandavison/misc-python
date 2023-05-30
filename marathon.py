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
    after_to_before = standings
    before_to_after = dict((before, after) for after, before in enumerate(after_to_before))
    winner = before_to_after.pop(-1) # winner guaranteed to be present
    [last] = set(after_to_before) - set(before_to_after)  # last is guaranteed to be the only missing key
    before_to_after[last] = -1

    results = []
    curr = winner
    while len(results) < len(after_to_before):
        results.append(curr)
        curr = before_to_after[curr]

    return results

def marathon_no_ties_dave(standings: List[int]) -> List[int]:
    order = [None] * len(standings)
    for behind, ahead in enumerate(standings):
        # student with label `ahead` finishes immediately to the left of `behind`.
        # Since the labels are also array indexes, we record this fact as
        order[ahead + 1] = behind
        # There is one exception: the leftmost entry has no-one to the left, and in this case ahead = -1.
        # But -1 was a well-chosen sentinel value, and the correct assignment is still made!
    return order

def marathon_with_ties(standings):
    graph = defaultdict(list)

    for i, s in enumerate(standings):
        if s != -1:
            graph[s].append(i)

    # Initialize queue with students that finished first
    queue = deque(i for i, s in enumerate(standings) if s == -1)

    order = []
    visited = set()
    while queue:
        student = queue.popleft()
        order.append(student)
        for next_student in graph[student]:
            if next_student not in visited:
                queue.append(next_student)
                visited.add(next_student)

    return order

def marathon_with_ties_dave(standings: List[int]) -> List[int]:
    order = [None] * len(standings)
    for behind, ahead in enumerate(standings):
        # student with label `ahead` finishes in the group to the
        # left of the group that `behind` finishes in.
        # The labels are also array indexes, so we use `ahead` to
        # index into the output array.
        # However, we may have already filled out some entries
        # in `behind`'s finishing group, so we advance to the next empty slot.
        c = 0
        while order[ahead + 1 + c] is not None:
            c += 1
        order[ahead + 1 + c] = behind
        # There is one exception: the leftmost entry has no-one to the left, and in this case ahead = -1.
        # But -1 was a well-chosen sentinel value, and the correct assignment is still made: we assign into the leftmost finishing group.
    return order

marathon_no_ties = marathon_no_ties_dave
marathon_with_ties = marathon_with_ties_dave

def test1():
    expected = [0, 1, 2]
    standings =  [-1, 0, 1]
    results = marathon_no_ties(standings)
    print(results == expected, results)


def test2():
    expected = [1, 0, 2]
    standings = [1, -1, 0]
    results = marathon_no_ties(standings)
    print(results == expected, results)


def test3():
    expected = [[0, 1, 2, 3], [0, 2, 1, 3]]  # 1 and 2 are tied
    standings = [-1, 0, 0, 2]
    results = marathon_with_ties(standings)
    print(results in expected, results)

def test4():
    expected = [[0, 1, 2, 3, 4],
                [1, 0, 2, 3, 4],
                [0, 1, 3, 2, 4],
                [1, 0, 3, 2, 4]] # {0, 1} and {1, 2} are two tied groups

    for standings in [[-1, -1, 0, 0, 3],
                      [-1, -1, 0, 1, 3],
                      [-1, -1, 1, 0, 2],
                      [-1, -1, 1, 1, 2]]:
        results = marathon_with_ties(standings)
        print(results in expected, results)


for test in [test3, test4]:
    print(test.__name__)
    test()
