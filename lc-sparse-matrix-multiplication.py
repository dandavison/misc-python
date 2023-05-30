# https://leetcode.com/problems/sparse-matrix-multiplication


from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # TODO: passes tests, but this does not take advantage of sparseness
        assert mat1 and mat2
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])
        assert n1 == m2
        output = [[None] * n2 for _ in range(m1)]
        for i in range(m1):
            rowi = mat1[i]
            for j in range(n2):
                oij = 0
                for k in range(n1):
                    oij += rowi[k] * mat2[k][j]
                output[i][j] = oij
        return output
                