from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = {}
        for idx, char in enumerate(s):
            char_dict[char] = idx

        results = []
        start, end = 0, 0
        for idx, char in enumerate(s):
            end = max(end, char_dict[char])
            if end == idx:
                results.append(end - start + 1)
                start = idx + 1
        return results
