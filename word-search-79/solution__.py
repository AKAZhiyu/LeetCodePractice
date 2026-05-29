from typing import List


class Solution:
    def backtracking(self, board, word, i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] == '' or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        board[i][j] = ''
        result = self.backtracking(board, word, i + 1, j, k + 1) or self.backtracking(board, word, i - 1, j, k + 1) or self.backtracking(board, word, i, j + 1, k + 1) or self.backtracking(board, word, i, j - 1, k + 1)
        board[i][j] = word[k]

        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range((len(board[0]))):
                if self.backtracking(board, word, i, j, 0):
                    return True

        return False
