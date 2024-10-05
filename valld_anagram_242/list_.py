class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        record = [0] * 26
        for letter in s:
            record[ord(letter) - ord('a')] += 1
        for letter in t:
            record[ord(letter) - ord('a')] -= 1

        for i in record:
            if i != 0:
                return False

        return True
