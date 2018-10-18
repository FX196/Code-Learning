# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                second_slow = head
                while second_slow != slow:
                    slow = slow.next
                    second_slow = second_slow.next
                return slow
        return None


"""
Say the non-cycle length is L, and slow has traveled L + C when it meets with fast.
Fast must travel 2L + 2C to catch up. Let the cycle size be N.
Full cycle is also how much more fast pointer has traveled than slow pointer at meeting point.

L + C + N = 2L + 2C
N = L + C

We can start another slow pointer from head. It must meet with slow at the node where the cycle starts.
"""
