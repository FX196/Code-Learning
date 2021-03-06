# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = right_depth = 1
        if root.left:
            left_depth = self.maxDepth(root.left) + 1
        if root.right:
            right_depth = self.maxDepth(root.right) + 1
        return max(left_depth, right_depth)
