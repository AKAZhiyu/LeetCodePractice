from random import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, euqal, small = [], [], []

            for num in nums:
                if num == pivot:
                    euqal.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    big.append(num)

            if k <= len(big):
                return quick_select(big, k)
            elif len(nums) - len(small) < k:
                return quick_select(small, k - len(big) - len(euqal))
            else:
                return pivot

        return quick_select(nums, k)
