from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result


    def backtracking(self, n, k, start, path, result):
        if len(path) == k:
            result.append(path[:])
            return

        # for purning, make sure n - start + 1 >= k - len(path)
        # thus start <= n + 1 - k + len(path)
        for i in range(start, n + 1 - k + len(path) + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()


