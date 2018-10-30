# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next
