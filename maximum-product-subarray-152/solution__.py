from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')

        p_max, p_min = 1, 1

        for x in nums:
            candidates = [p_max * x, x, p_min * x]
            p_max = max(candidates)
            p_min = min(candidates)
            result = max(result, p_max)


        return result
