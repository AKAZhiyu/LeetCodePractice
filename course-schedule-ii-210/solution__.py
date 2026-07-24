from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        flags = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for curr, pre in prerequisites:
            adjacency[curr].append(pre)

        # True: Acyclic
        # False: Cyclic

        def dfs(x):
            nonlocal adjacency, flags, result

            if flags[x] == 1:
                return False

            if flags[x] == -1:
                return True

            flags[x] = 1
            for i in adjacency[x]:
                if dfs(i) is False:
                    return False

            flags[x] = -1
            result.append(x)

            return True

        for i in range(numCourses):
            if dfs(i) is False:
                return []

        return result

