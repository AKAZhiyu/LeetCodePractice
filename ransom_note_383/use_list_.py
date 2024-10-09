class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomList = [0] * 26
        magazineList = [0] * 26

        for char in ransomNote:
            ransomList[ord(char) - ord('a')] += 1

        for char in magazine:
            magazineList[ord(char) - ord('a')] += 1

        return all(ransomList[i] <= magazineList[i] for i in range(26))