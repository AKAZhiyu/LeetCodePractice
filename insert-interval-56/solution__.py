from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])

        for x0, x1 in intervals:
            if result and x0 <= result[-1][-1]:
                result[-1][-1] = max(result[-1][-1], x1)
            else:
                result.append([x0, x1])
        return result
