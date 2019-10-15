# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        def visit(s, node):
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            if not children:
                return int(s + str(node.val))
            else:
                s+=str(node.val)
                return sum([visit(s, child) for child in children])
        return visit("", root)