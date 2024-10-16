from collections import deque

class MyStack:

    def __init__(self):
        # only use append, popleft method
        self.sim_stack = deque()
    def push(self, x: int) -> None:
        self.sim_stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.sim_stack) - 1):
            temp = self.sim_stack.popleft()
            self.sim_stack.append(temp)
        return self.sim_stack.popleft()

    def top(self) -> int:
        temp = self.pop()
        self.push(temp)
        return temp
    def empty(self) -> bool:
        return len(self.sim_stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()