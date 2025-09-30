from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [0] * (total + 1)

        for i in stones:
            for j in range(total, i - 1, -1):
                dp[j] = max(dp[j], i + dp[j - i])

        return total - dp[target] * 2



