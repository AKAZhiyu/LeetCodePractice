from collections import deque
from typing import List

class MonoDeque(deque):
    """To find the maximum/minimum value within a range,
       a monotonic queue is generally used."""

    # left-in right-out
    # from small to big
    def __init__(self):
        super().__init__()

    def pop(self, x):
        if x == self[-1]:
            super().pop()

    def push(self, x):
        while self and x > self[0]:
            self.popleft()
        self.appendleft(x)

    def front(self):
        return self[-1]

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        mono_queue = MonoDeque()

        for i in range(k): # 0 k-1
            mono_queue.push(nums[i])
        result.append(mono_queue.front())

        for i in range(k, len(nums)): # k n-1
            mono_queue.push(nums[i])
            mono_queue.pop(nums[i - k])
            result.append(mono_queue.front())

        return result


