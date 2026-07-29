from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)

            cur.next = node
            cur = cur.next

        return dummy.next

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, listA, listB):
        dummy = curr = ListNode()
        while listA and listB:
            if listA.val < listB.val:
                curr.next = listA
                listA = listA.next
            else:
                curr.next = listB
                listB = listB.next

            curr = curr.next

        curr.next = listA if listA else listB
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                curr_result = self.merge2Lists(l1, l2)
                merged_lists.append(curr_result)
            lists = merged_lists

        return lists[0]
        '''