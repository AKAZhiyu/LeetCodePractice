from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        rotted = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotted.append((i, j))

        result = 0
        while fresh and rotted:
            result += 1
            temp = rotted
            rotted = []

            for x, y in temp:
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        rotted.append((i, j))
                        grid[i][j] = '2'

        return result if not fresh else -1

