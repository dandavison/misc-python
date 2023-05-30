# https://leetcode.com/problems/merge-intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []        
        if not intervals:
            return output
        (s, e), *intervals = sorted(intervals)
        for s_i, e_i in intervals:
            if s_i > e:
                output.append((s, e))
                s, e = s_i, e_i
            else:
                e = max(e, e_i)
                
        output.append((s, e))
        return output
