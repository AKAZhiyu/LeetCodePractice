from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        majority = nums[0]
        for num in nums:
            if votes == 0:
                majority = num
            votes += 1 if majority == num else -1


        return majority
