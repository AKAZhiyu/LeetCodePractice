from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = p0 = ListNode(next=head)

        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        curr = p0.next
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp

        # after that, curr is the fist node after reversed list. pre is head
        p0.next.next = curr
        p0.next = pre

        return dummy.next








