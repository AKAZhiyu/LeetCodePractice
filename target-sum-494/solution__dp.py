from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # x positive sum
        # sum - x negative sum
        # x = (target + sum) / 2

        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 == 1:
            return 0

        bagSize = (target + total) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1

        for num in nums:
            for j in range(bagSize, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]

        return dp[bagSize]


