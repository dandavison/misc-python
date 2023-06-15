# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        no_stock = 0
        no_stock_cooldown = float("-inf")
        stock = float("-inf")

        for p in prices:
            no_stock, no_stock_cooldown, stock  = (
                max(no_stock_cooldown, no_stock),
                stock + p,
                max(no_stock - p, stock)
            )

        return int(max(no_stock, no_stock_cooldown))
