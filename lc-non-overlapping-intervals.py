from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # sort by end time
        intervals = sorted(intervals, key=lambda start__end: start__end[1])

        n_removed = 0
        (curr_start, curr_end), *intervals = intervals
        for start, end in intervals:
            if start < curr_end:
                n_removed += 1
            else:
                curr_start, curr_end = start, end

        return n_removed
