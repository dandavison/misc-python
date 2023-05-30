# https://leetcode.com/problems/3sum


from typing import List


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        return sorted(
            {
                (ni, n1, n2)
                for i, ni in enumerate(nums)
                for n1, n2 in get_pairs(nums[i + 1 :], -ni)
            }
        )


def get_pairs(nums, target):
    # yield all pairs in nums that sum to target
    seen = set()
    pairs = []
    for n in nums:
        if target - n in seen:
            pairs.append((target - n, n))
        seen.add(n)
    return pairs


if __name__ == "__main__":
    print("got      ", Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print("should be", [[-1, -1, 2], [-1, 0, 1]])
