from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_list = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_list[i - 1] = max(candy_list[i - 1], candy_list[i] + 1)

        return sum(candy_list)
