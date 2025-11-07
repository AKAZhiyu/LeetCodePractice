from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # four states
        # (buy/brought, sell, frozen, sold)
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = dp[i - 1][1]
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2])

        return max(dp[-1])


