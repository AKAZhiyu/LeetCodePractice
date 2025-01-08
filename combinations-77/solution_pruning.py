from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self.backtracking(n, k, [], 1, results)
        return results

    def backtracking(self, n, k, path, start_index, results):
        if len(path) == k:
            results.append(path[:])
            return
        # For pruning, we shall consider if there is enough element for us to choose
        # we shall make sure that: in our backtracking, our start_index <= n - (k - len(path)) + 1
        # origin is (n + 1 - start_index > k - len(path))
        for i in range(start_index, n - (k - len(path)) + 1 + 1):
            path.append(i)
            self.backtracking(n, k, path, i + 1, results)
            path.pop()
