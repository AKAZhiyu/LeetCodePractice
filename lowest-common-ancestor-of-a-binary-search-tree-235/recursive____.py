# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root
        return self.traverse(root, p, q)

    def traverse(self, root, p, q):
        if root is None:
            return root

        if root.val < p.val and root.val < q.val:
            right = self.traverse(root.right, p, q)
            if right is not None:
                return right

        if root.val > p.val and root.val > q.val:
            left = self.traverse(root.left, p, q)
            if left is not None:
                return left

        return root

