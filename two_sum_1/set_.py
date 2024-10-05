from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in records:
                return [nums.index(complement), i]
            records.add(num)
