# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        n_left, n_right = numbers[left], numbers[right]                
        while n_left + n_right != target:
            if n_left + n_right < target:
                left += 1
                n_left = numbers[left]
            else:
                right -= 1
                n_right = numbers[right]              
        return [left + 1, right + 1]
            
    def twoSum_1(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers, 1):
            try:
                return sorted([i, seen[target - n]])
            except KeyError:
                seen[n] = i
        