# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        result = []
        if root is None:
            return result
        self.Traversal(root, path, result)
        return result

    def Traversal(self, curr: TreeNode, path: List[int], result: List[str]):
        path.append(curr.val)

        if not curr.right and not curr.left:
            sPath = "->".join(map(str, path))
            result.append(sPath)
            return

        if curr.left:
            self.Traversal(curr.left, path, result)
            path.pop()

        if curr.right:
            self.Traversal(curr.right, path, result)
            path.pop()


