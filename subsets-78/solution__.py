from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.backtracking(nums, 0, results, [])
        return results

    def backtracking(self, nums, start_idx, results, path):
        results.append(path[:])

        for i in range(start_idx, len(nums)):
            self.backtracking(nums, i + 1, results, path + [nums[i]])



