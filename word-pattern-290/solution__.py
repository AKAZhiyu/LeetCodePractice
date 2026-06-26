class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split()
        return list(map(pattern.index, pattern)) == list(map(temp.index, temp))