from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        non_zero_nums = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[non_zero_nums] = nums[i]
                non_zero_nums += 1
        for i in range(non_zero_nums, len(nums)):
            nums[i] = 0
