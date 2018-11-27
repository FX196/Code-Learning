/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
package LeetCode;

class Solution_Add_Two_Numbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return partialAdd(l1, l2, 0);
    }

    public ListNode partialAdd(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null) return carry == 0 ? null : new ListNode(carry);
        int val1 = l1 == null ? 0 : l1.val;
        int val2 = l2 == null ? 0 : l2.val;
        int node_val = (val1 + val2 + carry) % 10;
        int next_carry = (val1 + val2 + carry) / 10;
        ListNode node = new ListNode(node_val);
        node.next = partialAdd(l1 == null ? null : l1.next, l2 == null ? null : l2.next, next_carry);
        return node;
    }
}