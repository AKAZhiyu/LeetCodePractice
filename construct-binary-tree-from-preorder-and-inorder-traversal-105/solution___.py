# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_value = preorder[0]
        root = TreeNode(val=root_value)

        if len(preorder) == len(inorder) == 1:
            return root

        delimiter_idx = inorder.index(root_value)
        inorder_left = inorder[:delimiter_idx]
        inorder_right = inorder[delimiter_idx + 1:]

        left_length = len(inorder_left)

        preorder_left = preorder[1: left_length + 1]
        preorder_right = preorder[left_length + 1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
