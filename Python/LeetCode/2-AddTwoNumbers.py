# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        node = head
        excess = 0
        while l1 and l2:
            val = excess + l1.val + l2.val
            excess, val = val // 10, val % 10
            node.next = ListNode(val)
            l1, l2 = l1.next, l2.next
            node = node.next
        else:
            n = None
            if l1:
                n = l1
            elif l2:
                n = l2
            if excess:
                node.next = Solution.addTwoNumbers(Solution, ListNode(excess), n)
            else:
                node.next = n
        return head.next
