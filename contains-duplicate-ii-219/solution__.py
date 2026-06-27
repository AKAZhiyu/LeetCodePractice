from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        loc_dict = {}
        for i, n in enumerate(nums):
            if n in loc_dict and i - loc_dict[n] <= k:
                return True

            loc_dict[n] = i
        return False

