from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # I, J -> J, N - I - 1

                # i, j -> j, n - i - 1
                # j, n - i - 1 -> n - i - 1 , n - j - 1
                # n - i - 1 , n - j - 1 -> n - j - 1, i
                # n - j - 1, i -> i, j

                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
