# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot
# achieve any profit, return 0.

from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # On each day we can buy-for-first-time, sell, or do-nothing

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
                -p,                          # buy for first time
                max_profit_if_have_stock,    # do-nothing
            )

        assert max_profit_if_have_stock <= max_profit_if_no_stock
        return int(max_profit_if_no_stock)
 

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        IF_HAVE_STOCK, IF_NO_STOCK = 0, 1
        max_profits = [[None, None]] * (len(prices) + 1)
        
        # 0 is the day before we actually start
        before_start = 0
        max_profits[before_start][IF_HAVE_STOCK] = float("-inf") # impossible
        max_profits[before_start][IF_NO_STOCK] = 0

        # 1 is the first day of `prices`
        for today, price in enumerate(prices, 1):
            yesterday = today - 1
            max_profits[today][IF_HAVE_STOCK] = max(
                max_profits[yesterday][IF_HAVE_STOCK],      # DO NOTHING (i.e. HOLD)
                0 - price                                   # BUY (FOR FIRST TIME! SEE COMMENT)
            )
            max_profits[today][IF_NO_STOCK] = max(
                max_profits[yesterday][IF_NO_STOCK],          # DO NOTHING
                max_profits[yesterday][IF_HAVE_STOCK] + price # SELL
            )
        
        last_day_max_profit = max_profits[-1]
        assert last_day_max_profit[IF_NO_STOCK] >= last_day_max_profit[IF_HAVE_STOCK]
        return last_day_max_profit[IF_NO_STOCK]


# One might think that line 58 above would be this:
#
# max_profits[yesterday][IF_NO_STOCK] - price
#
# But that "allows" them to buy and sell multiple times.
# Using -price has the effect of "requiring" that they have no profit yet when they buy.
# I.e. they are buying for the first time.

from dataclasses import dataclass

@dataclass
class State:
    max_profit_if_have_stock: float
    max_profit_if_no_stock: float

    @classmethod
    def initial_state(self) -> "State":
        return State(
            max_profit_if_have_stock=float("-inf"),
            max_profit_if_no_stock=0,
        )
    
    def next_state(self, price: int) -> "State":
        return State(
            max_profit_if_have_stock = max(
                self.max_profit_if_have_stock,  # do nothing
                -price,                         # buy for first time
            ),
            max_profit_if_no_stock = max(
                self.max_profit_if_no_stock,           # do nothing
                self.max_profit_if_have_stock + price  # sell
            )
        )
    
    def best_solution(self) -> float:
        return self.max_profit_if_no_stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state = State.initial_state()
        for data in prices:
            state = state.next_state(data)
        return state.best_solution()
