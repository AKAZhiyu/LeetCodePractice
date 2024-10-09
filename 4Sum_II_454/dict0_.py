from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()

        for n1 in nums1:
            for n2 in nums2:
                temp = n1 + n2
                if temp in hashmap:
                    hashmap[temp] += 1
                else:
                    hashmap[temp] = 1
        count = 0

        for n3 in nums3:
            for n4 in nums4:
                temp = - (n3 + n4)
                if temp in hashmap:
                    count += hashmap[temp]

        return count

