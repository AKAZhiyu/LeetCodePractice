from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = [[False] * 9 for _ in range(9)]
        col_has = [[False] * 9 for _ in range(9)]
        box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                x = int(col) - 1
                if row_has[i][x] == True or col_has[j][x] == True or box_has[i // 3][j // 3][x] == True:
                    return False

                row_has[i][x] = True
                col_has[j][x] = True
                box_has[i // 3][j // 3][x] = True

        return True


