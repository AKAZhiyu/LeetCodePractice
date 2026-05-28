from typing import List


class Solution:
    def backtracking(self, n, left, right, path, result):
        if len(path) == n * 2:
            result.append(''.join(path[:]))
            return

        if left < n:
            self.backtracking(n, left + 1, right, path + ['('], result)

        if right < left:
            self.backtracking(n, left, right + 1, path + [')'], result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtracking(n, 0, 0, [], result)
        return result
