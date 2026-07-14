from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dum, greater_dum = ListNode(), ListNode()
        smaller, greater = smaller_dum, greater_dum

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next
        smaller.next = greater_dum.next
        greater.next = None

        return smaller_dum.next
