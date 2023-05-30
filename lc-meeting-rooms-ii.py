# https://leetcode.com/problems/meeting-rooms-ii


from heapq import heappush, heappop
from typing import Iterable, List, Tuple


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for a, b in intervals:
            heappush(events, (a, 1))
            heappush(events, (b, -1))
        n = n_max = 0
        while events:
            delta = heappop(events)[1]
            n += delta
            if delta > 0:
                n_max = max(n, n_max)
        return n_max


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = sorted(_get_events(intervals))

        n_overlapping = 0
        max_n_overlapping = 0
        for _, delta in events:
            n_overlapping += delta
            max_n_overlapping = max(max_n_overlapping, n_overlapping)

        return max_n_overlapping


def _get_events(intervals: List[List[int]]) -> Iterable[Tuple[float, int]]:
    for start, end in intervals:
        yield (start, 1)
        yield (end, -1)
