from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):
            complement = target - value
            if complement in records:
                return [records[complement], index]

            records[value] = index

        return []


