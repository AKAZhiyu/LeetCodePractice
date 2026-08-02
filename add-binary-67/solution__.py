class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1

        carry = 0
        while i >= 0 or j >= 0 or carry != 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            total = x + y + carry
            quotient, remainder = divmod(total, 2)
            result.append(str(remainder))
            carry = quotient
            i -= 1
            j -= 1

        return ''.join(result[::-1])

