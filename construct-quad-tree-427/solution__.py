from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] + grid[i][j] - presum[i][j]

        def dfs(x0, y0, x1, y1):
            total = presum[x1][y1] + presum[x0][y0] - presum[x1][y0] - presum[x0][y1]
            total_cells = (y1 - y0) * (x1 - x0)

            if total == 0:
                return Node(0, 1)

            if total == total_cells:
                return Node(1, 1)

            mid_x = (x0 + x1) // 2
            mid_y = (y0 + y1) // 2

            top_left = dfs(x0, y0, mid_x, mid_y)
            top_right = dfs(x0, mid_y, mid_x, y1)
            buttom_left = dfs(mid_x, y0, x1, mid_y)
            buttom_right = dfs(mid_x, mid_y, x1, y1)

            return Node(1, 0, top_left, top_right, buttom_left, buttom_right)

        return dfs(0, 0, m, n)








