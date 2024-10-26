from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = []

    def traverse(self, node, path, left_target):
        if not node.left and not node.right and 0 == left_target:
            self.result.append(path[:])
            return

        if not node.left and not node.right:
            return

        if node.left:
            self.traverse(node.left, path[:] + [node.left.val], left_target - node.left.val)

        if node.right:
            self.traverse(node.right, path[:] + [node.right.val], left_target - node.right.val)

        return

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result.clear()

        if not root:
            return self.result

        self.traverse(root, [root.val], targetSum - root.val)

        return self.result
