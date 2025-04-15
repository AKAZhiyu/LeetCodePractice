from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [0] * n
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[-i - 1] = suffix[-i] * nums[-i]

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result
