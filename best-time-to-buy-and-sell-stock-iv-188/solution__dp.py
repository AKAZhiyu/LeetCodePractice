class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n)]

        for i in range(1, 2 * k + 1, 2):
            dp[0][i] = -prices[0]

        for i in range(1, n):
            # from 1 to 2k
            for j in range(1, 2 * k, 2):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                dp[i][j + 1] = max(dp[i - 1][j] + prices[i], dp[i - 1][j + 1])
        return dp[-1][-1]


