from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            # if temperatures[i] <= temperatures[stack[-1]]:
            #     stack.append(i)
            # else:
            #     while len(stack) and temperatures[stack[-1]] < temperatures[i]:
            #         item_idx = stack.pop()
            #         result[item_idx] = i - item_idx
            #     stack.append(i)
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                item_idx = stack.pop()
                result[item_idx] = i - item_idx
            stack.append(i)
        return result
