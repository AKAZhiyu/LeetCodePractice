class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        # Reverse the whole string first
        s = s[::-1]
        # Then reverse the word separately
        return ' '.join([word[::-1] for word in s.split()])
