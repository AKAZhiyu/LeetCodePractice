class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.isStackEmpty(self.out_stack):
            self.transferStack(self.in_stack, self.out_stack)

        return self.out_stack.pop()

    def peek(self) -> int:
        to_pop = self.pop()
        self.out_stack.append(to_pop)
        return to_pop

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def isStackEmpty(self, stack):
        if len(stack) == 0:
            return True
        else:
            return False

    def transferStack(self, in_stack, out_stack):
        while len(in_stack):
            temp = in_stack.pop()
            out_stack.append(temp)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()