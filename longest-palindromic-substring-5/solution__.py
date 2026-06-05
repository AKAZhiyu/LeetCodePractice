class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        begin = end = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for l in range(2, n + 1):
            for i in range(n):
                j = i + l - 1
                if j > n - 1:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i > end - begin:
                    begin, end = i, j

        return s[begin: end + 1]

