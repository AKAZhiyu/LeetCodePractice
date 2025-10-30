from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) > i:
                    continue

                if dp[i - len(word)] and word == s[i - len(word): i]:
                    dp[i] = True
        return dp[-1]


