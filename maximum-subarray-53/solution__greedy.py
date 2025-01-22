from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        count = 0
        for num in nums:
            count += num
            result = max(result, count)
            if count < 0:
                count = 0
        return result
