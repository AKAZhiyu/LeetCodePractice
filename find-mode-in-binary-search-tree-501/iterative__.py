# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        prev = None
        curr = root
        max_count = 0
        count = 0
        result = []

        while len(stack) > 0 or curr is not None:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev is None:
                    count = 1
                elif prev.val == curr.val:
                    count += 1
                else:
                    count = 1

                if count == max_count:
                    result.append(curr.val)
                elif count > max_count:
                    result = [curr.val]
                    max_count = count

                prev = curr
                curr = curr.right

        return result

