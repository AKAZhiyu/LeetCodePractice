from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_idx = 0
        for i in range(len(s)):
            if child_idx < len(g) and g[child_idx] <= s[i]:
                child_idx += 1
        return child_idx
