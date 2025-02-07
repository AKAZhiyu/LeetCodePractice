from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])

        non_overlaps = 1
        interval_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if interval_end <= intervals[i][0]:
                interval_end = intervals[i][1]
                non_overlaps += 1

        return len(intervals) - non_overlaps
