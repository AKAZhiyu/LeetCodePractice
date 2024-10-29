from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        pre = None
<<<<<<< HEAD
        curr = root

        while curr is not None or len(stack) > 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left

            else:
                curr = stack.pop()
                if pre is not None and pre.val >= curr.val:
                    return False
                pre = curr
                curr = curr.right
=======
        cur = root

        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                if pre is not None and pre.val >= cur.val:
                    return False
                pre = cur
                cur = cur.right
>>>>>>> origin/master
        return True

