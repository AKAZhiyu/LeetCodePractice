from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_value = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self.isValidBST(root.left)

        if self.max_value < root.val:
            self.max_value = root.val
        else:
            return False
        right = self.isValidBST(root.right)

        return left and right

