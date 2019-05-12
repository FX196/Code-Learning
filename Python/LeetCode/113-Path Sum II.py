# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        children = []
        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)
        if not children:
            if root.val == s:
                return [[root.val]]
            else:
                return []
        else:
            paths = sum([self.pathSum(child, s - root.val) for child in children], [])
            ans = [[root.val] + path for path in paths if path]
            return ans
