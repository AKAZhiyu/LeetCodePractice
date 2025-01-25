from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        steps, current_cover, next_cover = 0, 0, 0

        for i in range(len(nums)):
            next_cover = max(next_cover, nums[i] + i)

            if i == current_cover:
                current_cover = next_cover
                steps += 1
                if next_cover >= len(nums) - 1:
                    break

        return steps

