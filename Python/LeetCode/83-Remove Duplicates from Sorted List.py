# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        node = dummy = ListNode(None)
        dummy.next = head
        while node.next.next:
            if node.next.val == node.next.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
