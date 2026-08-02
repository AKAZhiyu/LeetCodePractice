import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]

        for _ in range(k):
            val, i, j = heapq.heappop(h)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))

        return result

