# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val == key:

            if root.left is not None and root.right is None:
                return root.left
            elif root.right is not None and root.left is None:
                return root.right
            elif root.right is None and root.left is None:
                return None
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left

                curr.left = root.left
                return root.right
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            if root.val < key:
                root.right = self.deleteNode(root.right, key)

        return root



