from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.max_diameter = 0

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        self.max_diameter = max(l + r, self.max_diameter)

        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_diameter
