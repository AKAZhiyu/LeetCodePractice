from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodeDict = {}

        curr = head
        while curr:
            nodeDict[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head
        while curr:
            nodeDict.get(curr).next = nodeDict.get(curr.next)
            nodeDict.get(curr).random = nodeDict.get(curr.random)
            curr = curr.next

        return nodeDict.get(head)
