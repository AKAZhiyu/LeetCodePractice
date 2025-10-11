from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in coins:
            for j in range(1, amount + 1):
                if j >= i and dp[j - i] != float('inf'):
                    dp[j] = min(dp[j - i] + 1, dp[j])

        return dp[-1] if dp[-1] != float('inf') else -1
