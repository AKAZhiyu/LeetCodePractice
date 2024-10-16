from typing import List
from operator import add, sub, mul


def div(x, y):
    return int(x / y)


class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': div}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                operation = self.op_map[token]

                stack.append(int(operation(operand1, operand2)))
        return stack.pop()
