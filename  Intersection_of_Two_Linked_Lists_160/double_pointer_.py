from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        long_length = self.getListLength(headA)
        short_length = self.getListLength(headB)

        # make A always be the longer
        if long_length < short_length:
            long_length, short_length = short_length, long_length
            headA, headB = headB, headA

        gap = long_length - short_length

        while gap:
            headA = headA.next
            gap -= 1

        while headA:
            if headA is headB:
                return headB
            headA = headA.next
            headB = headB.next

        return None

    def getListLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
