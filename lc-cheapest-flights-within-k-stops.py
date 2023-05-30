import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = make_adjacency_list(flights)
        
        heap = [(0, src, -1)]  # cost, dst
        cost = {}
        while heap:
            cost_from_src, city, n_stops = heapq.heappop(heap)
            # print(city, "cost:", cost_from_src, "stops", n_stops)

            _, previous_n_stops = cost.get(city, (None, None))
            if previous_n_stops is None or n_stops < previous_n_stops:
                # print(f"cost[{city}] = {cost_from_src}")
                cost[city] = (cost_from_src, n_stops)
                # print("pushing:")
                for price, to in adj_list.get(city, []):
                    c = cost_from_src + price if n_stops < k else float("inf")
                    # print(f"\t{to} cost: {c} stops: {n_stops + 1}")
                    heapq.heappush(heap,
                                   (c,
                                    to,
                                    n_stops + 1))
                                
        min_cost, _ = cost.get(dst, (None, None))
        if min_cost is not None and min_cost < float("inf"):
            return min_cost
        else:
            return -1


class Solution_DP(object):
    # https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115623/10-line-python-DP-solution-O(N2*K)-time-O(N)-space
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        INF = float('inf')
        mn = [INF]*n
        mn[src] = 0
        
        for k in range(K+1):
            newmn = mn[:]
            for a, b, cost in flights:
                newmn[b] = min(newmn[b], mn[a] + cost)
            mn = newmn
            
        return mn[dst] if mn[dst] != INF else -1


class Solution_DFS:
    # Times out
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = make_adjacency_list(flights)
    
        max_length = k + 1

        def _get_paths(src, path_to_src=None):
            if path_to_src is None:
                path_to_src = []
            if len(path_to_src) > max_length:
                return
            if dst == src:
                yield path_to_src
            else:
                for weight, neighb in adj_list.get(src, []):
                    yield from _get_paths(neighb, path_to_src + [weight])

    
        paths = list(_get_paths(src))
        
        if not paths:
            return -1
        else:
            return min(map(sum, paths))


def make_adjacency_list(edges: List[List[int]]) -> Dict[int, Tuple[int, int]]:
    adj_list = defaultdict(list)
    for _from, to, price in edges:
        adj_list[_from].append((price, to))
    
    return dict(adj_list)
