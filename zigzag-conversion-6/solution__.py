class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        result = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            result[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag

        return "".join(result)
