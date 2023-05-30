# https://leetcode.com/problems/jump-game-ii-2


class Solution:
    def jump(self, nums: List[int]) -> int:
        # The min number of jumps is found by:
        # For each possible jump from here, compute 1 + min_num_jumps_having_taken_that_jump
        # Return the minimum over these values
        return jump(nums)


_cache = {}


def jump(nums):
    key = tuple(nums)
    if key in _cache:
        return _cache[key]

    assert nums
    if len(nums) == 1:
        _cache[key] = 0
        return 0
    elif nums[0] == 0:
        _cache[key] = None
        return None

    min_length = None
    possible_jumps = range(1, min(nums[0] + 1, len(nums) - 1 + 1))
    for jump_size in reversed(possible_jumps):

        sub_problem_min = jump(nums[jump_size:])
        if sub_problem_min is None:
            continue

        length = 1 + sub_problem_min

        if length in [1, 2]:
            _cache[key] = length
            return length

        if min_length is None or length < min_length:
            min_length = length

    _cache[key] = min_length
    return min_length
