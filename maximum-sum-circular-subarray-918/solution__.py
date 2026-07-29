from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0

        max_sum = float('-inf')
        curr_max = 0

        min_sum = float('inf')
        curr_min = 0

        for num in nums:
            total_sum += num

            curr_max = max(num, num + curr_max)
            max_sum = max(curr_max, max_sum)


            curr_min = min(num, num + curr_min)
            min_sum = min(curr_min, min_sum)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)
