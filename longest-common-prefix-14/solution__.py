from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for j, c in enumerate(result):
            for s in strs:
                if j == len(s) or s[j] != c:
                    return result[:j]

        return result
