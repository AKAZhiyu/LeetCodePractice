from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.backtracking(candidates, target, [], 0, results)
        return results

    def backtracking(self, candidates, target, path, start_idx, results):
        if sum(path) > target:
            return

        if sum(path) == target:
            results.append(path[:])
            return

        for i in range(start_idx, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target, path, i, results)
            path.pop()
