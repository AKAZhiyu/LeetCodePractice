# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if root is None:
            return result

        path = []
        self.Traversal(root, path, result)

        return result

    def Traversal(self, curr: TreeNode, path: List[int], result: List[str]):


        path.append(curr.val)

        if not curr.left and not curr.right:
            result.append("->".join(map(str, path)))

        if curr.left:
            self.Traversal(curr.left, path[:], result)
        if curr.right:
            self.Traversal(curr.right, path[:], result)
        return
