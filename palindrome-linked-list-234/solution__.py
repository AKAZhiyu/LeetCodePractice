# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        h2 = head2 = self.reverseList(mid)
        while head2:
            if head2.val != head.val:
                return False
            head = head.next
            head2 = head2.next
        self.reverseList(h2)
        return True











