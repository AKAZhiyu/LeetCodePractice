from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        curr = self.stack.pop()
        node = curr.right
        while node:
            self.stack.append(node)
            node = node.left
        return curr.val


    def hasNext(self) -> bool:
        return len(self.stack) > 0


