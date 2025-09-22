class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 1:
            return 1

        climb_ways = [1] * (n + 1)
        for i in range(2, n + 1):
            climb_ways[i] = climb_ways[i - 1] + climb_ways[i - 2]

        return climb_ways[-1]
