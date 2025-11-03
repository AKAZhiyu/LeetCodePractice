from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        return max(self.robTree(root))

    def robTree(self, node):
        if node is None:
            return 0, 0

        left_tuple = self.robTree(node.left)
        right_tuple = self.robTree(node.right)
        # (without_curr, with_curr)
        with_curr = node.val + left_tuple[0] + right_tuple[0]
        without_curr = max(left_tuple) + max(right_tuple)
        current_tuple = (without_curr, with_curr)
        return current_tuple


