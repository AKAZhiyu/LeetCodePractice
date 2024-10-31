# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.vec = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec.clear()
        self.traversal(root)

        min_diff = abs(self.vec[1] - self.vec[0])
        for i in range(1, len(self.vec) - 1):
            temp = abs(self.vec[i + 1] - self.vec[i])
            if temp < min_diff:
                min_diff = temp

        return min_diff

    def traversal(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.traversal(root.left)
        self.vec.append(root.val)
        self.traversal(root.right)
        return
