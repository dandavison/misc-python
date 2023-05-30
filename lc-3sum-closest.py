# https://leetcode.com/problems/3sum-closest


import bisect

class Solution:
    # passes
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        best = float("inf")
        for left in range(n-2):
            mid, right = left + 1, n - 1
            while mid < right:
                curr = nums[left] + nums[mid] + nums[right]
                if abs(target - curr) < abs(target - best):
                    best = curr
                if curr > target:
                    right -= 1
                else:
                    mid += 1
                    
        return best



class Solution_2:
    def threeSumClosest(self, nums, target):
        # I think this is O(N^2) but it is timing out on leetcode, and it seems
        # many/all accepted solutions are O(N^2)
        # EDIT: see "two-pointer"-based solution above
        pairwise_sums = sorted(compute_pairwise_sums(nums))  # O(N^2)
        closest, delta_min = None, float("inf")
        for i, n1 in enumerate(nums):  # O(N)
            pairwise_sum = find_closest_sum(pairwise_sums, target - n1, i)  # O(N)
            delta = n1 + pairwise_sum - target
            if False:
                print(
                    {
                        "n1": n1,
                        "pairwise_sum": pairwise_sum,
                        "target": target,
                        "delta": delta,
                        "target+delta": target + delta,
                    }
                )
            if abs(delta) < abs(delta_min):
                delta_min = delta
                closest = target + delta
        return closest


def compute_pairwise_sums(nums):
    sums = []
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i + 1 :], i + 1):
            sums.append(((n1 + n2), i, j))
    return sums


def find_closest_sum(pairwise_sums, target, excluding):
    pairwise_sums = [s for (s, i, j) in pairwise_sums if excluding not in [i, j]]
    i = bisect.bisect_right(pairwise_sums, target)
    if i == len(pairwise_sums):
        return pairwise_sums[-1]
    elif i == 0:
        return pairwise_sums[0]
    else:
        val_to_right = pairwise_sums[i]
        val_to_left = pairwise_sums[i - 1]
        return (
            val_to_right
            if val_to_right - target < target - val_to_left
            else val_to_left
        )


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    # print(Solution().threeSumClosest([0, 0, 1], 2))
