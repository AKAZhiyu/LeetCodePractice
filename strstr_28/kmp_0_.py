from typing import List


class Solution:
    def getNext(self, nextList, s):

        # j is the end of the prefix
        # and also the length of the current longest common prefix and suffix
        j = 0
        nextList[0] = 0

        # i is the end of the suffix
        for i in range(1, len(s)):

            while j > 0 and s[j] != s[i]:
                j = nextList[j - 1]

            if s[j] == s[i]:
                j += 1

            nextList[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        nextList = [0] * len(needle)

        self.getNext(nextList, needle)

        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nextList[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                return i - j + 1

        return -1




