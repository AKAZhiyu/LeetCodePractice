from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        k %= n

        curr.next = head

        new_tail = head

        # 0 - 1 - 2
        # 2: new tail = 0, 3 - 2 - 1 = 0
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head

