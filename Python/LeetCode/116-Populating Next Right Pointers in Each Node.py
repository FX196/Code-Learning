# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = [(root, 1)]
        pre, pre_level = None, None
        while q:
            node, level = q.pop(0)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if pre:
                if pre_level == level:
                    pre.next = node
            pre, pre_level = node, level
