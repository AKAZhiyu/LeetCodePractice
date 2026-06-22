from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')

        total = left = 0
        for i in range(n):
            total += nums[i]

            while total >= target:
                result = min(result, i - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= n else 0



