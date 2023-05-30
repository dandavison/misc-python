# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        no_stock = 0
        stock = float("-inf")
        
        for p in prices:
            no_stock, stock = (
                max(stock + p - fee, no_stock),
                max(no_stock - p, stock)
            )
            
        return no_stock
