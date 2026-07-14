from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(next=head)
        while curr.next and curr.next.next:
            val = curr.next.val
            if val == curr.next.next.val:
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next

            else:
                curr = curr.next

        return dummy.next


# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = pre = ListNode(next=head)
#         curr = head
#
#         while curr:
#             val = curr.val
#             while curr.next and val == curr.next.val:
#                 curr = curr.next
#
#             if pre.next == curr:
#                 pre = pre.next
#             else:
#                 pre.next = curr.next
#             curr = curr.next
#
#         return dummy.next
