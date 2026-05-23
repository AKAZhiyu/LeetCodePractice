from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1

        curr = head
        p0 = dummy = ListNode(next=head)
        pre = None

        while n >= k:
            n -= k
            for _ in range(k):
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt

            nxt = p0.next  # origin head, curr queue end
            p0.next.next = curr
            p0.next = pre
            p0 = nxt

        return dummy.next