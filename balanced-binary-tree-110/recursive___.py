# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)


