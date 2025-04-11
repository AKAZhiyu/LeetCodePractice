from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        accumulator = [0] * (len(nums) + 1)
        counter = Counter()

        for i in range(len(nums)):
            accumulator[i + 1] = accumulator[i] + nums[i]

        for i in range(len(accumulator)):
            result += counter[accumulator[i] - k]
            counter[accumulator[i]] += 1

        return result


