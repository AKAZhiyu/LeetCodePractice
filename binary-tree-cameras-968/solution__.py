# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode], result: List[int]) -> int:
        """
        from down to top
        node status:
        has camera - 1
        no camera but monitored - 2
        no camera and no monitored - 0
        """
        if not root:
            return 2

        left = self.traverse(root.left, result)
        right = self.traverse(root.right, result)

        if left == right == 2:
            return 0
        elif left == 0 or right == 0:
            result[0] += 1
            return 1
        else:
            return 2

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = [0]
        if self.traverse(root, result) == 0:
            result[0] += 1
        return result[0]
