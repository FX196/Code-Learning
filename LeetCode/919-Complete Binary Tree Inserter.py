# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.parents = self.get_parents()

    def get_parents(self):
        queue = [self.root]
        parents = []
        while queue:
            node = queue.pop(0)
            if not node.left:
                parents.append(node)
                continue
            queue.append(node.left)
            if not node.right:
                parents.append(node)
            else:
                queue.append(node.right)
        return parents

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.parents[0]
        if not parent.left:
            parent.left = TreeNode(v)
            self.parents.append(parent.left)
            return parent.val
        else:
            parent.right = TreeNode(v)
            self.parents = self.parents[1:]
            self.parents.append(parent.right)
            return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
