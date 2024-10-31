# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        prev = None
        result = float('inf')

        while len(stack) > 0 or cur is not None:
            if cur is not None:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                if prev is not None:
                    result = min(result, cur.val - prev.val)
                prev = cur
                cur = cur.right

        return result

