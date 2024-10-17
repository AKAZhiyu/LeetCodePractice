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

        result = []

        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))

        return result


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []

        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)

        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []

        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))

        return result





