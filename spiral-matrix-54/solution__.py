from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while True:
            for i in range(l, r + 1):
                result.append(matrix[u][i])
            u += 1
            if u > d:
                break
            for i in range(u, d + 1):
                result.append(matrix[i][r])
            r -= 1
            if r < l :
                break
            for i in range(r, l - 1, -1):
                result.append(matrix[d][i])
            d -= 1
            if d < u :
                break
            for i in range(d, u - 1, -1):
                result.append(matrix[i][l])
            l += 1
            if r < l :
                break
        return result

