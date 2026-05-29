from typing import List


class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l


    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)