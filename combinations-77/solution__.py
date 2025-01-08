from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, [], 1, result)
        return result

    def backtracking(self, n, k, path, start_idx, result):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start_idx, n + 1):
            path.append(i)
            self.backtracking(n, k, path, i + 1, result)
            path.pop()

