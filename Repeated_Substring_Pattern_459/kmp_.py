class Solution:

    def findNext(self, next_list, s):
        j = 0
        next_list[0] = 0

        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = next_list[j - 1]

            if s[j] == s[i]:
                j += 1

            next_list[i] = j


    def repeatedSubstringPattern(self, s: str) -> bool:
        # kmp method
        if len(s) == 0:
            return False

        next_list = [0] * len(s)

        self.findNext(next_list, s)
        # The condition len(s) % (len(s) - next_list[-1]) checks
        # if the length of the string is divisible by the length of the repeating substring.
        if next_list[-1] != 0 and len(s) % (len(s) - next_list[-1]) == 0:
            return True

        return False



