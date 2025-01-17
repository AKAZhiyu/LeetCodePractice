from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.backtracking(nums, len(nums) * [False], results, [])
        return results

    def backtracking(self, nums, used, results, path):
        if len(path) == len(nums):
            results.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.backtracking(nums, used, results, path)
                used[i] = False
                path.pop()

