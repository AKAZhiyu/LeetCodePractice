from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.backtracking(nums, 0, [], results)
        return results

    def backtracking(self, nums, start_idx, path, results):
        results.append(path[:])

        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i - 1]:
                continue
            self.backtracking(nums, i + 1, path[:] + [nums[i]], results)

