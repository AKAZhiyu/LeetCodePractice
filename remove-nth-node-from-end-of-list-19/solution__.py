from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = back = dummy = ListNode(next=head)
        for _ in range(n):
            front = front.next

        while front.next is not None:
            front, back = front.next, back.next

        back.next = back.next.next

        return dummy.next
