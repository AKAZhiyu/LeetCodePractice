from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        self.backtracking(nums, len(nums) * [False], results, [])
        return results

    def backtracking(self, nums, used, results, path):
        if len(path) == len(nums):
            results.append(path[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                continue

            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.backtracking(nums, used, results, path)
                used[i] = False
                path.pop()
