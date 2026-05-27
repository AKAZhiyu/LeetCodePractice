from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # T: Acyclic F: Cyclic
        def dfs(i, adjacency, flags):
            # Found by other nodes
            if flags[i] == -1:
                return True

            # Found by curr nodes
            if flags[i] == 1:
                return False

            flags[i] = 1

            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False

            flags[i] = -1
            return True

        flags = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for curr, pre in prerequisites:
            adjacency[pre].append(curr)

        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False

        return True