from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [0]

        for i in range(1, len(nums) * 2):
            while stack and nums[stack[-1] % len(nums)] < nums[i % len(nums)]:
                if result[stack[-1] % len(nums)] == -1:
                    result[stack[-1] % len(nums)] = nums[i % len(nums)]
                stack.pop()
            stack.append(i)
        return result
