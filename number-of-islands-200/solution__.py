from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1 or grid[i][j] != '1':
                return

            grid[i][j] = 0

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1

        return result