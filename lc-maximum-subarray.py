# https://leetcode.com/problems/maximum-subarray/
from typing import List

# Most of the functions below are alternative implementations of "Kadane's algorithm",
# i.e. whenever the current running total becomes negative, reset it to zero.
    

from dataclasses import dataclass

@dataclass
class State:
    curr_sum: float
    max_sum: float
        
    @classmethod
    def initial_state(cls) -> "State":
        return cls(
            curr_sum = float("-inf"),
            max_sum = float("-inf")
        )

    def next_state(self, data: float) -> "State":
        curr_sum = data + max(self.curr_sum, 0)
        return State(
            curr_sum=curr_sum,
            max_sum = max(curr_sum, self.max_sum)                        
        )
    
    def best_solution(self) -> float:
        return self.max_sum
        

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        state = State.initial_state()
        for data in nums:
            state = state.next_state(data)
        return state.best_solution()


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        return kadane(nums)

def kadane_explicit_table(self, nums: List[int]) -> int:
    # This version makes it clear that it's a similar structure to other "Dynamic Programming"
    # algorithms that work by moving left to right through an table, filling out one column at a time,
    # using the values in the column to the left.
    curr_sum = [float("-inf")] * len(nums)
    curr_sum[0] = max_sum = nums[0]
    for i, n in enumerate(nums[1:], 1):
        curr_sum[i] = n + max(curr_sum[i - 1], 0)
        max_sum = max(curr_sum[i], max_sum)
    return max_sum

def kadane_single_variable(self, nums: List[int]) -> int:
    curr_sum = max_sum = nums[0]
    for n in nums[1:]:
        curr_sum = n + max(curr_sum, 0)
        max_sum = max(curr_sum, max_sum)
    return max_sum
    
def kadane(nums):
    max_sum = float("-inf")

    local_sum = 0
    for n in nums:
        local_sum += n
        max_sum = max(max_sum, local_sum)
        if local_sum < 0:
            local_sum = 0
            
    return int(max_sum)


def kadane_2(nums):
    if not nums:
        return 0
    max_sum = local_sum = nums[0]
    for n in nums[1:]:
        if local_sum > 0:
            local_sum += n
        else:
            local_sum = n
        max_sum = max(local_sum, max_sum)
    return max_sum


def n_squared(self, nums: List[int]) -> int:
    if not nums:
        return 0
    _max = nums[0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            # print(nums[i:j])
            _max = max(_max, sum(nums[i:j]))
    return _max


def enumerate_subarrays(arr):
    """
    Print all non-empty contiguous subarrays.
    >>> enumerate_subarrays([0, 1, 2])
    [0]
    [0, 1]
    [0, 1, 2]
    [1]
    [1, 2]
    [2]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            print(nums[i:j])


if __name__ == "__main__":
    f = Solution().maxSubArray
    f([0, 1, 2])
