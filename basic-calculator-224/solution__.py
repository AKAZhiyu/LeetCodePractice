class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                result += sign * num
                sign = 1 if c == "+" else -1
                num = 0
            elif c == "(":
                stack.append(sign)
                stack.append(result)
                sign = 1
                result = 0
                num = 0
            elif c == ")":
                result += sign * num
                num = 0
                pre_result = stack.pop()
                pre_sign = stack.pop()
                result *= pre_sign
                result += pre_result

        result += sign * num

        return result
