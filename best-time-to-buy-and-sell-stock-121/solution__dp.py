from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        # (hold, not hold) total money profit
        # hold => dp[i][0] = max(-prices[i], dp[i-1][0])
        # not hold => dp[i][1] = max(prices[i] + dp[i-1][0], dp[i-1][i])
        dp = [[0, 0]] * days
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(prices[i] + dp[i - 1][0], dp[i - 1][1])

        return dp[-1][-1]
