# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        node = root
        while q:
            node = q.pop(0)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val

    # simply do level order traversal from right to left. return the last node.
