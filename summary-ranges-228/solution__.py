from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        i = 0

        while i < n:
            low = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            high = i

            if low < high:
                result.append(str(nums[low]) + '->' + str(nums[high]))
            else:
                result.append(str(nums[low]))

            i += 1
        return result
