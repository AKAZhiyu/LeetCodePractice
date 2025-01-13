from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        self.backtracking(n, k, 1, [], results)
        return results


    def backtracking(self, targetSum, k, currentIdx, path, results):
        if targetSum < sum(path):
            return

        if len(path) == k:
            if sum(path) == targetSum:
                results.append(path[:])
        # for i in range(currentIdx, 10):
        # make sure:
        # n - start + 1 >= k - len(path)
        # start <= n - (k - len(path)) + 1

        for i in range(currentIdx, 9 - (k - len(path)) + 1 + 1):
            path.append(i)
            self.backtracking(targetSum, k, i + 1, path, results)
            path.pop()
