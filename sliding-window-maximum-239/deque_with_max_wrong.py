from collections import deque
from typing import List

from collections import deque

class MaxDeque(deque):
    def __init__(self, *args):
        super().__init__(*args)
        # 初始化最大值变量
        self.max_value = max(self) if self else None

    def append(self, value):
        super().append(value)
        # 更新最大值
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def appendleft(self, value):
        super().appendleft(value)
        # 更新最大值
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def pop(self):
        value = super().pop()
        # 如果移除的是最大值，则需要重新计算最大值
        if value == self.max_value:
            self.max_value = max(self) if self else None
        return value

    def popleft(self):
        value = super().popleft()
        # 如果移除的是最大值，则需要重新计算最大值
        if value == self.max_value:
            self.max_value = max(self) if self else None
        return value

    def get_max(self):
        # 返回当前最大值
        return self.max_value


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MaxDeque()
        result = []
        for i in range(k): #先将前k的元素放进队列
            que.appendleft(nums[i])
        result.append(que.get_max()) #result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop() #滑动窗口移除最前面元素
            que.appendleft(nums[i]) #滑动窗口前加入最后面的元素
            result.append(que.get_max()) #记录对应的最大值
        return result