from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.vec = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec.clear()
        self.traversal(root)
        for i in range(1, len(self.vec)):
            if self.vec[i - 1] >= self.vec[i]:
                return False
        return True

    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        self.vec.append(root.val)
        self.traversal(root.right)

