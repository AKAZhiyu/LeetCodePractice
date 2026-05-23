from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbers(l1, l2, carry=0)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry != 0 else None

        if l1 is None:
            l1, l2 = l2, l1

        total = l1.val + (l2.val if l2 is not None else 0) + carry

        l1.val = total % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else l2, total // 10)
        return l1


