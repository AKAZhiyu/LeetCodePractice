from typing import List


class Solution:
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # n, m = len(nums1), len(nums2)
        #
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        #
        # result = 0
        #
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if nums1[i - 1] == nums2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #             result = max(result, dp[i][j])
        # return result
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [0] * (m + 1)
        result = 0
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1

                else:
                    dp[j] = 0
                result = max(result, dp[j])
        return result








