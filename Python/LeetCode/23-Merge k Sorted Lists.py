# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        q = []
        for l in lists:
            if l:
                heappush(q, (l.val, id(l), l))

        while q:
            _, _, curr.next = heappop(q)
            curr = curr.next
            if curr.next:
                heappush(q, (curr.next.val, id(curr.next), curr.next))

        return head.next
