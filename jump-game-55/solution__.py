from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i in range(len(nums)):
            if cover < i:
                break
            cover = max(cover, i + nums[i])

        return cover + 1 >= len(nums)




