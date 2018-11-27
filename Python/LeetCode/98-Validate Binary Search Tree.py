# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -10 ** 32, 10 ** 32)

    def isValid(self, root, min_val, max_val):
        if not root:
            return True
        else:
            r_val = root.val
            if r_val >= max_val or r_val <= min_val:
                return False
            return self.isValid(root.left, min_val, r_val) and self.isValid(root.right, r_val, max_val)
