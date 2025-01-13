from typing import List


class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

    def backtracking(self, digits, startIdx, path, results):
        if len(digits) == len(path):
            results.append(''.join(path[:]))
            return

        digit = int(digits[startIdx])
        letters = self.letterMap[digit]

        for c in letters:
            path.append(c)
            self.backtracking(digits, startIdx + 1, path, results)
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        self.backtracking(digits, 0, [], results)
        return results
