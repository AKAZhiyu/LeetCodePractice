# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = root.left
        right = root.right

        leftDepth, rightDepth = 0, 0

        while left:
            leftDepth += 1
            left = left.left

        while right:
            rightDepth += 1
            right = right.right

        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
