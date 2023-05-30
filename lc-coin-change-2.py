"""
https://leetcode.com/problems/coin-change-2/

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins, reverse=True)
        
        @cache
        def get_combs(amount):
            if amount == 0:
                return {()}
            else:
                combs = set()

                for coin in coins:
                    if coin <= amount:
                        for sub_comb in get_combs(amount - coin):
                            combs.add((coin,) + sub_comb)                        

                return {tuple(sorted(comb)) for comb in combs}
        
        combs = get_combs(amount)
        return len(combs)
    