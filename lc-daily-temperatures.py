from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We'll maintain a stack holding all indexes for which we haven't found a higher temperature.
        # Suppose we encounter index i with a higher temperature than some previous index j.
        # The key observation is that i displaces not just j but all subsequent stack entries
        # (if it did not then there would exist some index k later in the stack than j but with higher temp,
        # but that violates the stack membership condition).
        # The result is that every value is pushed once and popped once, hence time complexity is O(N).
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result


class SolutionOrig:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        i = n - 1
        max_temp = temperatures[i]
        seen = {max_temp: i}

        while i > 0:
            i -= 1
            temp = temperatures[i]
            max_temp = max(temp, max_temp)
            seen[temp] = i
            result[i] = min((seen[t] - i for t in range(temp + 1, max_temp + 1) if t in seen), default=0)

        return result
