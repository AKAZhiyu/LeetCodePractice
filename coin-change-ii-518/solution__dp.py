from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 2 dimension
        # coin_num = len(coins)
        # dp = [[0] * (amount + 1) for _ in range(coin_num)]
        # for i in range(amount + 1):
        #     if i % coins[0] == 0:
        #         dp[0][i] = 1
        #
        # for i in range(coin_num):
        #     dp[i][0] = 1
        #
        # for i in range(1, coin_num):
        #     for j in range(1, amount + 1):
        #         if coins[i] > j:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
        #
        # return dp[-1][-1]
        dp = [0] * (amount + 1)

        dp[0] = 1
        coin_num = len(coins)
        for i in range(coin_num):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[-1]




