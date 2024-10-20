# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return True if root is None else self.compare(root.left, root.right)

    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)

        return outside and inside
