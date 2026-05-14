import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # matrix[i][j] = matrix[j][n - 1 - i]
        tmp = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = tmp[i][j]



