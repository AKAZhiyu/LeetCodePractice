from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.binary_search(nums, target + 1) - 1
        return [left, right]

    def binary_search(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left
