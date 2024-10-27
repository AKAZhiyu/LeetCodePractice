# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_value = postorder[-1]
        root = TreeNode(val=root_value)

        if len(postorder) == len(inorder) == 1:
            return root

        delimiter_idx = inorder.index(root_value)
        inorder_left = inorder[:delimiter_idx]
        inorder_right = inorder[delimiter_idx + 1:]

        left_length = len(inorder_left)

        postorder_left = postorder[:left_length]
        postorder_right = postorder[left_length: -1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
