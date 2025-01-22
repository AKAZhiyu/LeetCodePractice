from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        bisc_index = len(s) - 1
        for i in range(len(g) - 1, -1, -1):
            if bisc_index >= 0 and g[i] <= s[bisc_index]:
                bisc_index -= 1
                result += 1
        return result
