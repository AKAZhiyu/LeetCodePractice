class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)
        return dp[n]
