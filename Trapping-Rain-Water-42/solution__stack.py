from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) and height[stack[-1]] < height[i]:
                    item_idx = stack.pop()
                    item_height = height[item_idx]
                    if len(stack):
                        rain_height = min(height[stack[-1]], height[i])
                        width = i - stack[-1] - 1
                        result += width * (rain_height - item_height)
                stack.append(i)
        return result


