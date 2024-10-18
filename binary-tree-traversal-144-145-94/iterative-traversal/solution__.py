from typing import Optional, List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []
        # mid left right
        while stack:
            processing = stack.pop()
            result.append(processing.val)
            if processing.right:
                stack.append(processing.right)
            if processing.left:
                stack.append(processing.left)

        return result


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        result = []
        stack.append(root)

        # mid right left
        while stack:
            processing = stack.pop()
            result.append(processing.val)
            if processing.left:
                stack.append(processing.left)
            if processing.right:
                stack.append(processing.right)


        return result[::-1]

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        result = []

        curr = root

        while curr or stack:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

        return result
