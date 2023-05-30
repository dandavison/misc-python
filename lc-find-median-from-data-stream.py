# https://leetcode.com/problems/find-median-from-data-stream


class MedianFinder:
    def __init__(self):
        # 3, 1, 7, 6, 2 => 3
        self.p = float("+inf")  # 1
        self.q = float("-inf")  # 3

    def addNum(self, num: int) -> None:
        if self.p > num:
            self.p = num
        if self.q < num:
            self.q = num

    def findMedian(self) -> float:
        pass


from heapq import heappush, heappop, heapify


class MedianFinder_0:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heappush(self.heap, num)

    def findMedian(self) -> float:
        values = []
        while self.heap:
            values.append(heappop(self.heap))
        assert values
        n = len(values)
        if n % 2 == 0:
            right = values[n // 2]
            left = values[n // 2 - 1]
            result = (left + right) / 2
        else:
            result = values[n // 2]
        self.heap = values
        heapify(self.heap)
        return result
