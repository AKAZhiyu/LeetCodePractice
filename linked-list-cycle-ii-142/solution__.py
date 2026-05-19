from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while True:
            if not (fast and fast.next):
                return

            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break

        # f = 2s, f = s + nb
        # Currently, slow: n circle * b circle length; fast: 2nb
        # position in nb + a
        fast = head
        while fast is not slow:
            fast, slow = fast.next, slow.next
        return fast