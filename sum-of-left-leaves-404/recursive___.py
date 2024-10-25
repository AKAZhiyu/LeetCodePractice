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
        if root.left is None and root.right is None:
            return 0

        # left_value = self.sumOfLeftLeaves(root.left)
        # if root.left and root.left.left is None and root.left.right is None:
        #     left_value = root.left.val
        #
        # right_value = self.sumOfLeftLeaves(root.right)
        #
        # return left_value + right_value

        left_value = 0
        if root.left and root.left.left is None and root.left.right is None:
            left_value = root.left.val

        return left_value + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

