from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        result = 0
        cnt[0] = 1

        def dfs(root, s):
            if root is None:
                return

            nonlocal result
            s += root.val
            result += cnt[s - targetSum]

            cnt[s] += 1
            dfs(root.left, s)
            dfs(root.right, s)
            cnt[s] -= 1

        dfs(root, 0)
        return result

