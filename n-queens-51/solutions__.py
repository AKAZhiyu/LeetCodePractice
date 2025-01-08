from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n, 0, chessboard, results)
        return results

    def backtracking(self, n: int, row: int, chessboard: List[str], result: List[List[str]]) -> None:
        if row == n:
            result.append(chessboard[:])
            return

        for col in range(n):
            if self.is_valid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col + 1:]
                self.backtracking(n, row + 1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]

    def is_valid(self, row: int, col: int, chessboard: List[str]):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j <= len(chessboard) - 1:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True
