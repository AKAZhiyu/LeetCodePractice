from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = dict()
        result = set()

        for num in nums1:
            table[num] = table.get(num, 0) + 1

        for num in nums2:
            if num in table:
                result.add(num)

        return list(result)

