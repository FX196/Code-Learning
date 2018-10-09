# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return dummy.next
