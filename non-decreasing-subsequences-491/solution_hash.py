from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.backtracking(results, [], nums, 0)
        return results

    def backtracking(self, results: List[List[int]], path: List[int], nums: List[int], start_idx: int):
        if len(path) > 1:
            results.append(path[:])

        # used_nums = set()
        # from -100 to 100
        used_nums = [0] * 201

        for i in range(start_idx, len(nums)):
            if used_nums[nums[i] + 100] == 1 or (path and path[-1] > nums[i]):
                continue

            used_nums[nums[i] + 100] = 1
            self.backtracking(results, path + [nums[i]], nums, i + 1)
