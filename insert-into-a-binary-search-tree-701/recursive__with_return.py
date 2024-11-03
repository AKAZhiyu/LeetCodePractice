from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        self.pre = None
        self.traverse(root, val)

        return root

    def traverse(self, root, val):
        if root is None:
            node = TreeNode(val)
            if self.pre.val < val:
                self.pre.right = node
            else:
                self.pre.left = node
            return

        self.pre = root

        if root.val < val:
            self.traverse(root.right, val)
            return
        if root.val > val:
            self.traverse(root.left, val)
            return
