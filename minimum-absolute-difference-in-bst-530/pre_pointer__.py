# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.result

    def traversal(self, curr: Optional[TreeNode]) -> None:
        if curr is None:
            return
        self.traversal(curr.left)
        if self.pre is not None:  # 中
            self.result = min(self.result, curr.val - self.pre.val)

        self.pre = curr
        self.traversal(curr.right)
        return

