from typing import List


class Solution:
    # this will overtime
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, current_sum, total_sum = 0, 0, 0

        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                current_sum = 0
                start = i + 1

        if total_sum < 0:
            return -1

        return start
