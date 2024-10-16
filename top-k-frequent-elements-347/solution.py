from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1

        min_heap = []

        for key, value in freq_map.items():
            if len(min_heap) >= k:
                heapq.heappushpop(min_heap, (value, key))
            else:
                heapq.heappush(min_heap, (value, key))

        result = [0] * k

        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(min_heap)[1]
        return result






