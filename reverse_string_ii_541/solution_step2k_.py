class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        l = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k < len(l):
                l[i:i + k] = reversed(l[i:i + k])
            else:
                l[i:] = reversed(l[i:])

        return ''.join(l)

