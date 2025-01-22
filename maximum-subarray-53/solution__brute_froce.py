from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                count += nums[j]
                result = max(count, result)
        return result



