# https://leetcode.com/problems/network-delay-time


import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = make_adjacency_list(range(1, n+1), times)

        total_times = {}
        heap = [(0, k)]
        
        while heap:
            time, node = heapq.heappop(heap)
            
            if node not in total_times:
                total_times[node] = time
                for neighb_time, neighb in adj_list[node]:
                    heapq.heappush(heap, (time + neighb_time, neighb))
                    
        return max(total_times.values()) if len(total_times) == n else -1

        
def make_adjacency_list(nodes, edges):
    adj_list = {v: [] for v in nodes}
    for u, v, w in edges:
        adj_list[u].append((w, v))
    return adj_list
