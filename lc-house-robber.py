"""
https://leetcode.com/problems/house-robber/solution/

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # state machine
        # states: canrob, wait
        # canrob --rob--> wait
        # canrob --donothing--> canrob
        # wait --donothing--> canrob
        
        max_money = {
            "can_rob": 0,
            "wait": float("-inf"),
        }
        
        for num in nums:            
            can_rob, wait = max_money["can_rob"], max_money["wait"]
            max_money["can_rob"] = max(
                can_rob, # donothing
                wait,    # donothing                
            )
            max_money["wait"] = can_rob + num  # rob

        return max(max_money["can_rob"], max_money["wait"])
