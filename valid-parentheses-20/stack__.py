class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif len(stack) == 0 or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if len(stack) == 0 else False
