from typing import List


class Solution:
    # this will overtime
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cost_fill_sum = 0
        min_fill = float('inf')

        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            cost_fill_sum += rest
            if min_fill > cost_fill_sum:
                min_fill = cost_fill_sum

        if cost_fill_sum < 0:
            return -1

        if min_fill >= 0:
            return 0

        for i in range(len(gas) - 1, -1, -1):
            rest = gas[i] - cost[i]
            min_fill += rest
            if min_fill >= 0:
                return i

        return -1