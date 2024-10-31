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
        self.freq_map = defaultdict(int)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.freq_map.clear()
        self.traverse(root)
        max_value = max(self.freq_map.values())
        result = []
        for k, v in self.freq_map.items():
            if v == max_value:
                result.append(k)
        return result

    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.freq_map[root.val] += 1
        self.traverse(root.left)
        self.traverse(root.right)

