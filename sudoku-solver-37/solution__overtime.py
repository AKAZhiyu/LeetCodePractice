from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for i in range(9)]
        col_used = [set() for i in range(9)]
        box_used = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
        self.backtracking(board, row_used, col_used, box_used, 0, 0)
        return

    def backtracking(self, board: List[List[str]],
                     row_used: List[Set[str]],
                     col_used: List[Set[str]],
                     box_used: List[Set[str]],
                     start_row: int,
                     start_col: int) -> bool:
        for i in range(start_row, 9):
            for j in range(start_col, 9):
                if board[i][j] != '.':
                    continue
                for k in "123456789":
                    if k in row_used[i] or k in col_used[j] or k in box_used[(i // 3) * 3 + j // 3]:
                        continue
                    if self.is_valid(i, j, k, board):
                        row_used[i].add(k)
                        col_used[j].add(k)
                        box_used[(i // 3) * 3 + j // 3].add(k)
                        board[i][j] = k

                        if self.backtracking(board,
                                             row_used,
                                             col_used,
                                             box_used,
                                             start_row=i if j < 8 else i + 1,
                                             start_col=j + 1 if j < 8 else 0):
                            return True

                        row_used[i].remove(k)
                        col_used[j].remove(k)
                        box_used[(i // 3) * 3 + j // 3].remove(k)
                        board[i][j] = '.'
                return False
        return True

    def is_valid(self, row: int, col: int, val: str, board: List[List[str]]):
        for i in range(9):
            if board[row][i] == val:
                return False

        for i in range(9):
            if board[i][col] == val:
                return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == val:
                    return False

        return True
