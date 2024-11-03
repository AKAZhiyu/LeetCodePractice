from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        pre = None
        cur = root

        while cur:
            pre = cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left

        if pre.val < val:
            pre.right = TreeNode(val)
        else:
            pre.left = TreeNode(val)

        return root

