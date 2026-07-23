from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.value = {}  # self.value[x] = x / root

    def is_connected(self, x, y):
        return x in self.parent and y in self.parent and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None
            self.value[x] = 1

    def find(self, x):
        root = x
        base = 1

        while self.parent[root] != None:
            root = self.parent[root]
            base *= self.value[root]

        while x != root:
            original_root = self.parent[x]
            self.value[x] *= base
            base /= self.value[original_root]

            self.parent[x] = root
            x = original_root

        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            # self.value[x] = x / root_x
            # x / y = val
            # root_x / root_y = (x / self.value[x]) / (y / self.value[y])
            self.value[root_x] = val * self.value[y] / self.value[x]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()

        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        result = [-1] * len(queries)

        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                # a / b = (uf.values[a] / root) / (uf.values[b] / root)
                result[i] = uf.value[a] / uf.value[b]

        return result
