from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(root):
            if root is None:
                return 0

            left_path = dfs(root.left)
            right_path = dfs(root.right)
            nonlocal result
            result = max(left_path + right_path + root.val, result)
            return max(max(left_path, right_path) + root.val, 0)

        dfs(root)
        return result





