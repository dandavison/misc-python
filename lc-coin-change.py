from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def _coinChange(amount):
            if amount == 0:
                return 0
            else:
                return 1 + min((_coinChange(amount - coin)
                                for coin in coins
                                if coin <= amount), default=float("inf")))

        n_coins = _coinChange(amount)
        return n_coins if n_coins < float("inf") else -1
