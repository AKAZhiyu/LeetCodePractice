from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0

        leftMax = [0] * length
        rightMax = [0] * length

        leftMax[0] = height[0]
        for i in range(1, length):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        rain_sum = 0
        for i in range(length):
            rain_sum += min(rightMax[i], leftMax[i]) - height[i]

        return rain_sum


