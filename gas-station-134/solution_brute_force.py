from typing import List


class Solution:
    # this will overtime
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for start_idx in range(len(cost)):
            rest = gas[start_idx] - cost[start_idx]
            index = (start_idx + 1) % len(gas)
            while rest > 0 and index != start_idx:
                rest += gas[index] - cost[index]
                index = (index + 1) % len(gas)
            if rest >= 0 and index == start_idx:
                return start_idx

        return -1

