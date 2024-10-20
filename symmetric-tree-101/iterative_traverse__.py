from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()

            if not leftNode and not rightNode:
                continue
            elif not leftNode and rightNode:
                return False
            elif leftNode and not rightNode:
                return False
            elif rightNode.val != leftNode.val:
                return False

            queue.append(leftNode.right)
            queue.append(rightNode.left)

            queue.append(leftNode.left)
            queue.append(rightNode.right)

        return True

