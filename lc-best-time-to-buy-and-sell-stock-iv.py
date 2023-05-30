# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_profit_if_no_stock = [0] * (k + 1)

        # Note that we only actually need k values here, since
        # max_profit_if_stock[k] corresponds to being about to make our (k+1)th
        # transaction.
        max_profit_if_stock = [float("-inf")] * (k + 1)
        
        for p in prices:
            for j in range(k + 1):
                max_profit_if_stock[j] = max(
                    max_profit_if_no_stock[j] - p,  # buy
                    max_profit_if_stock[j]  # do-nothing
                )
                max_profit_if_no_stock[j] = max(
                    max_profit_if_stock[j-1] + p if j > 0 else 0,  # sell
                    max_profit_if_no_stock[j]  # do-nothing
                )
                
        return max(max_profit_if_no_stock)
