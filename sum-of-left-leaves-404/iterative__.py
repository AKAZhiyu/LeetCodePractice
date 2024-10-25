# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        total = 0
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr.left and curr.left.left is None and curr.left.right is None:
                total += curr.left.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return total