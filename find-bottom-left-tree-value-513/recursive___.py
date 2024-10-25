# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = float('-inf')
        self.result = None

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):

        if not node.left and not node.right and depth > self.max_depth:
            self.result = node.val
            self.max_depth = depth

        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1

        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1

        return
