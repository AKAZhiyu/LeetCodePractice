from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val, max_val = 1, len(nums)

        while min_val < max_val:
            mid = (min_val + max_val) // 2

            cnt = sum(min_val <= num <= mid for num in nums)

            if cnt > (mid - min_val + 1):
                max_val = mid
            else:
                min_val = mid + 1

        return min_val