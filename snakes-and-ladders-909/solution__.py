class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        result = 0
        n = len(board)
        queue = [1]
        visited = [False] * (n * n + 1)

        def get_next(y):
            nonlocal n, board
            r, c = divmod(y - 1, n)
            r_idx = -1 - r
            # VERY IMPORTANT:
            # For offset c range from 0 to n - 1, Forward c, Backward n - 1 - c
            c_idx = c if r % 2 == 0 else n - 1 - c
            return y if board[r_idx][c_idx] == -1 else board[r_idx][c_idx]

        while queue:
            next_queue = []

            for x in queue:
                if x == n * n:
                    return result

                for y in range(x + 1, min(x + 6, n * n) + 1):
                    destination = get_next(y)
                    if visited[destination] == False:
                        visited[destination] = True
                        next_queue.append(destination)

            queue = next_queue
            result += 1

        return -1
