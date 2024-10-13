class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate the string s with itself
        t = s + s

        # Remove the first and the last characters
        t = t[1:-1]

        # If the modified string t still contains the original string s,
        # it means s can be constructed by repeating a substring
        if s in t:
            return True
        return False
