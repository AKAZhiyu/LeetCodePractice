class Solution:
    def decodeString(self, s: str) -> str:
        times, stack, result = 0, [], ""
        for c in s:
            if '0' <= c <= '9':
                times = times * 10 + int(c)
            elif c == '[':
                stack.append([times, result])
                times, result = 0, ''
            elif c == ']':
                last_times, last_result = stack.pop()
                result = last_result + last_times * result
            else:
                result += c
        return result