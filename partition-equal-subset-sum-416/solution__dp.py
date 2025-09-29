from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [0] * (total + 1)

        for n in nums:
            for j in range(total, n - 1, -1):
                dp[j] = max(dp[j], n + dp[j - n])

        if dp[target] == target:
            return True
        else:
            return False
