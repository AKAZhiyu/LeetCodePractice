
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _sum_numbers(self, root, total=0):
        if not root:
            return 0

        total = total * 10 + root.val

        if not root.left and not root.right:
            return total

        left = self._sum_numbers(root.left, total)
        right = self._sum_numbers(root.right, total)

        return left + right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._sum_numbers(root)
