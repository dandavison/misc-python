# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state machine
        # state: n_shares_held        
        # 0 --buy--> 1
        # 1 --sell--> 0
        
        max_profit = [
            0,              # initial value
            float("-inf")   # impossible initially
        ]
        for p in prices:
            max_profit[0] = max(
                max_profit[0],
                max_profit[1] + p,  # sell
            )
            max_profit[1] = max(
                max_profit[1],
                max_profit[0] - p,  # buy
            )
        
        return max_profit[0]


class Solution_4:
    def maxProfit(self, prices: List[int]) -> int:
        # On each day we can buy, sell, or do-nothing

        # state machine:
        # --------------
        # no_stock   --buy---------> have_stock
        # no_stock   --do-nothing--> no_stock
        # have_stock --sell--------> no_stock
        # have_stock --do-nothing--> have_stock

        # Initialize
        max_profit_if_no_stock = 0
        max_profit_if_have_stock = float("-inf")  # impossible initially

        for p in prices:
            max_profit_if_no_stock = max(
                max_profit_if_no_stock,       # do-nothing
                max_profit_if_have_stock + p, # sell
            )
            max_profit_if_have_stock = max(
                max_profit_if_no_stock - p,  # buy
                max_profit_if_have_stock,    # do-nothing
            )

        assert max_profit_if_have_stock <= max_profit_if_no_stock
        return int(max_profit_if_no_stock)


from itertools import chain


class Solution_3:
    def maxProfit(self, prices: List[int]) -> int:
        # Whenever we see the price go down,
        # we buy at the last minimum and sell at the peak we just passed
        last_min = None
                
        pairs = zip(prices, chain(prices[1:], [None]))
        
        profit = 0
        for p, p_next in pairs:
            if p_next is None or p_next < p:
                if last_min is not None and last_min < p:
                    profit += p - last_min
                    last_min = None
            if last_min is not None:
                last_min = min(last_min, p)
            else:
                last_min = p

        return profit
        

import functools

class Solution_2:
    # timeout / memory exceeded
    def maxProfit(self, prices: List[int]) -> int:
        return max_profit(False, tuple(prices))


@functools.lru_cache(maxsize=32)
def max_profit(have, prices):
    p = prices[0]
    if len(prices) == 1:
        if have:
            return p
        else:
            return 0
    else:
        if not have:
            buy = -p + max_profit(True, prices[1:])
            no_buy = max_profit(False, prices[1:])
            return max(buy, no_buy)
        else:
            sell = p + max_profit(False, prices[1:])
            no_sell = max_profit(True, prices[1:])
            return max(sell, no_sell)
