# Operation [start time, end time, usage]
# Your input is a bunch of operations ^^^
# Find an interval where the total combined usage from all operations was maximal.

# Example:
# 0                     10
# |---------5-----------|
#         3                    12
#         |---------3----------|
#                  8                     15
#                  |----------2----------|
#
# |   5   |   8    |10  |  5   |    2    |

# Input:
# [(0, 10, 5), (3, 12, 3), (8, 15, 2)]

# Output:
# [8, 10, 10]

from typing import Iterable, List

START, END = "s", "e"


def find_max_interval(ops: List[tuple]) -> tuple:
    events = sorted(_get_events(ops))

    total_usage = 0
    max_interval_start, max_interval_end, max_total_usage = None, None, 0

    in_max = False
    for time, delta in events:
        total_usage += delta
        if total_usage >= max_total_usage:
            max_interval_start, max_total_usage = time, total_usage
            in_max = True
        else:
            if in_max == True:
                max_interval_end = time
                in_max = False

    return max_interval_start, max_interval_end, max_total_usage


def _get_events(ops: List[tuple]) -> Iterable[tuple]:
    for start_time, end_time, usage in ops:
        yield (start_time, usage)
        yield (end_time, -usage)


print(find_max_interval([(0, 10, 5), (3, 12, 3), (8, 15, 2)]))
