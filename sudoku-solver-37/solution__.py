from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        Bad python, have to reduce loop nums.
        So we use sets to eliminate is_valid,
        use next_idx to reduce loop.
        '''

        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
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
        if start_row == 9:
            return True

        next_row, next_col = (start_row, start_col + 1) if start_col < 8 else (start_row + 1, 0)

        if board[start_row][start_col] != '.':
            return self.backtracking(board, row_used, col_used, box_used, next_row, next_col)

        val: str
        for val in "123456789":
            if val in row_used[start_row] or \
               val in col_used[start_col] or \
               val in box_used[(start_row // 3) * 3 + start_col // 3]:
                continue
            board[start_row][start_col] = val
            row_used[start_row].add(val)
            col_used[start_col].add(val)
            box_used[(start_row // 3) * 3 + start_col // 3].add(val)
            if self.backtracking(board, row_used, col_used, box_used, next_row, next_col):
                return True
            board[start_row][start_col] = '.'
            row_used[start_row].remove(val)
            col_used[start_col].remove(val)
            box_used[(start_row // 3) * 3 + start_col // 3].remove(val)
        return False
