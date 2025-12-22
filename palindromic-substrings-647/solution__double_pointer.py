class Solution(object):
    def extend(self, s, i, j, n):
        result = 0
        while 0 <= i and j < n and s[i] == s[j]:
            result += 1
            j += 1
            i -= 1
        return result


    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0

        for i in range(n):
            result += self.extend(s, i, i, n)
            result += self.extend(s, i, i + 1, n)
        return result


