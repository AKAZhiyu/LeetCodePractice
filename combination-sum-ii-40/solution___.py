from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.backtracking(candidates, [], 0, results, target)
        return results

    def backtracking(self, candidates, path, start_idx, results, target):
        if sum(path) == target:
            results.append(path[:])
            return

        if sum(path) > target:
            return

        for i in range(start_idx, len(candidates)):
            if i > start_idx and candidates[i - 1] == candidates[i]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, path, i + 1, results, target)
            path.pop()
