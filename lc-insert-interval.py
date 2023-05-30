# https://leetcode.com/problems/insert-interval


# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [start_i, end_i] represent the start and the end of the ith
# interval and intervals is sorted in ascending order by start_i. You are also
# given an interval newInterval = [start, end] that represents the start and end
# of another interval.

# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by start_i and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        new_start, new_end = newInterval
        i = 0
        while i < n and intervals[i][1] < new_start:
            i += 1
        # intervals[i] ends at or after the start of the new interval
        j = i + 1
        while j < n and intervals[j][0] <= new_end:
            j += 1
        # intervals[j] starts after the new interval so this and subsequent
        # should be emitted unchanged

        print(i, j)

        # intervals[i:j] (if non-empty) should be merged
        if i < j <= n:
            merged_start = min(intervals[i][0], new_start)
            merged_end = max(intervals[j - 1][1], new_end)
            intervals[i] = [merged_start, merged_end]
            del intervals[i + 1 : j]
        else:
            intervals.insert(i, newInterval)
        return intervals


if False:
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    f = Solution().insert
    print(f(intervals, newInterval))