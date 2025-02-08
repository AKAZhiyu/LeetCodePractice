from typing import List


class Solution:
    def count_char_intervals(self, s: str) -> List[List[float]]:
        interval_hash_list = [[float('-inf'), float('-inf')] for _ in range(26)]
        hash_filter = []
        for i in range(len(s)):
            if interval_hash_list[ord(s[i]) - ord('a')][0] == float('-inf'):
                interval_hash_list[ord(s[i]) - ord('a')][0] = i
            interval_hash_list[ord(s[i]) - ord('a')][1] = i
        for i in range(len(interval_hash_list)):
            if interval_hash_list[i][0] != float('-inf'):
                hash_filter.append(interval_hash_list[i])
        return hash_filter

    def partitionLabels(self, s: str) -> List[int]:
        result = []
        intervals = self.count_char_intervals(s)
        intervals.sort(key=lambda x: x[0])
        left, right = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                result.append(right - left + 1)
                left = intervals[i][0]
            right = max(right, intervals[i][1])
        result.append(right - left + 1)
        return result
