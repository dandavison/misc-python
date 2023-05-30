# https://leetcode.com/problems/jump-game-ii


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Return length of min-length path to index n-1.
        """
        # This greedy algorithm is optimal, because the future options after
        # jumping to the largest value include the options you'd have if you had
        # jumped to a different (non-largest) value.
        path_length = 0
        while len(nums) > 1:
            if nums[0] >= len(nums) - 1:
                path_length += 1
                break
            # Find the largest-valued cell you can jump to
            _max = 0
            _max_idx = None
            for i in range(1, min(nums[0] + 1, len(nums))):
                if nums[i] > _max:
                    _max, _max_idx = nums[i], i
            nums = nums[_max_idx:]
            path_length += 1
        return path_length


_cache = {}


def memoized(f):
    def g(nums, *args):
        key = tuple(nums)
        if key not in _cache:
            _cache[key] = f(nums)
        return _cache[key]

    return g


@memoized
def jump_1(nums, indent=0):
    # This is a memoized recursion. leetcode wants a more efficient solution
    # than this (i.e. the greedy solution).
    assert nums
    if len(nums) == 1:
        return 0

    min_length = None
    for jump_len in reversed(range(1, min(nums[0] + 1, len(nums)))):
        sub_problem_min_len = jump(nums[jump_len:])
        if sub_problem_min_len is None:
            continue
        length = 1 + sub_problem_min_len
        if length == 1:
            return length
        elif length == 2 and jump_len != len(nums) - 1:
            return length

        if min_length is None or length < min_length:
            min_length = length
    return min_length


# print(Solution().jump([2, 3, 0, 1, 4]))
