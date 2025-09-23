from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair_len = len(cost)
        if stair_len <= 2:
            return min(cost)
        min_cost = [0] * (stair_len + 1)
        for i in range(2, stair_len + 1):
            min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])
        return min_cost[-1]
