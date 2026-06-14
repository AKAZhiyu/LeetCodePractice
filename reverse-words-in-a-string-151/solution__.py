class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        result = []
        i = j = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            result.append(s[i + 1: j + 1])
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i

        return " ".join(result)



