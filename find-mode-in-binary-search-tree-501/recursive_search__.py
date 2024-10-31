# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
        self.max_count = 0
        self.count = 0
        self.pre = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.result.clear()
        self.max_count = 0
        self.count = 0
        self.pre = None

        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.traverse(root.left)

        if self.pre is None:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1

        self.pre = root

        if self.count == self.max_count:
            self.result.append(root.val)
        elif self.count > self.max_count:
            self.result.clear()
            self.result.append(root.val)
            self.max_count = self.count

        self.traverse(root.right)

