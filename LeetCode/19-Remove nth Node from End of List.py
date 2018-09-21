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
        fast = head
        slow = head
        while n:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            fast, slow = fast.next, slow.next
        if slow.next:
            if not slow == head:
                slow.next = slow.next.next
                return head
            else:
                return head.next
        return None

    # TODO: Edge Cases