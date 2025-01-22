from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        prev_diff, curr_diff = 0, 0
        result = 1
        for i in range(len(nums) - 1):
            curr_diff = nums[i + 1] - nums[i]
            if (prev_diff >= 0 > curr_diff) or (prev_diff <= 0 < curr_diff):
                result += 1
                prev_diff = curr_diff
        return result

