from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0

        def dfs(root):
            nonlocal result, k
            if not root:
                return
            dfs(root.left)
            k -= 1
            if k == 0:
                result = root.val
            dfs(root.right)

        dfs(root)

        return result

