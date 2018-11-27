# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = ListNode(0)  # using a temp because the head of the list is changing
        temp.next = head
        curr = temp
        while curr.next and curr.next.next:
            first = curr.next
            sec = curr.next.next
            curr.next = sec
            first.next = sec.next
            sec.next = first
            curr = curr.next.next
        return temp.next
