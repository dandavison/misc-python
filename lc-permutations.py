from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        perms = []
        for i in range(len(nums)):
            for sub_perm in self.permute(nums[:i] + nums[i + 1 :]):
                perms.append([nums[i]] + sub_perm)
        return perms


class Solution2:
    def permute(self, vals_at_node: List[int]) -> List[List[int]]:
        # The variable names in this function refer to the way of thinking about the problem as as
        # a tree of "choices". I.e. Each branch represents a choice of a val to go first, and the
        # branch leads to a child node which represents a smaller permutations problem (permute the
        # other vals).
        def get_perms():
            for choice, vals_at_child_node in split(vals_at_node):
                for child_node_perm in self.permute(vals_at_child_node):
                    yield [choice] + child_node_perm

        if len(vals_at_node) > 1:
            return list(get_perms())
        else:
            return [vals_at_node]


def split(vals: List[int]):
    for i in range(len(vals)):
        yield vals[i], vals[:i] + vals[i + 1 :]
