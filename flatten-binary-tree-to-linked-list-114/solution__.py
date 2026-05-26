from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = None

        def traverse(root):
            if root is None:
                return

            nonlocal head
            traverse(root.right)
            traverse(root.left)
            root.left = None
            root.right = head
            head = root

        traverse(root)
        return root



