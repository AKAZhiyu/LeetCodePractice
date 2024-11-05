# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.right)
        root.val += self.pre
        self.pre = root.val

        self.traverse(root.left)

        return

