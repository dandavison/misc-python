# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii


# You are given an array prices where prices[i] is the price of a given stock on
# the ith day.

# Find the maximum profit you can achieve. You may complete at most two
# transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
from typing import List

class Solution:
    # passes tests
    def maxProfit(self, prices: List[int]) -> int:
        # state machine:
        # --------------
        # no_stock[0] --buy---------> stock[0]
        # no_stock[0] --do-nothing--> no_stock[0]
        # stock[0]    --sell--------> no_stock[1]
        # stock[0]    --do-nothing--> stock[0]
        # no_stock[1] --buy---------> stock[1]
        # no_stock[1] --do-nothing--> no_stock[1]
        # stock[1]    --sell--------> no_stock[2]
        # stock[1]    --do-nothing--> stock[1]
        # no_stock[2] --do-nothing--> no_stock[2]

        max_profit_if_no_stock = [0, float("-inf"), float("-inf")]
        max_profit_if_stock = [float("-inf"), float("-inf")]

        for p in prices:
            max_profit_if_stock[0] = max(
                max_profit_if_no_stock[0] - p,  # buy
                max_profit_if_stock[0],
            )
            max_profit_if_no_stock[1] = max(
                max_profit_if_stock[0] + p,  # sell
                max_profit_if_no_stock[1]
            )
            max_profit_if_stock[1] = max(
                max_profit_if_no_stock[1] - p,  # buy
                max_profit_if_stock[1],
            )
            max_profit_if_no_stock[2] = max(
                max_profit_if_stock[1] + p,  # sell
                max_profit_if_no_stock[2]
            )

        assert max_profit_if_stock[0] <= max_profit_if_no_stock[1]
        assert max_profit_if_stock[1] <= max_profit_if_no_stock[2]
        return int(max(max_profit_if_no_stock))
