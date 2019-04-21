# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.maxDiffH(root)[0]

    def maxDiffH(self, root):
        """

        :param root:
        :return: maxDiff, max, min
        """
        maxDiff = 0
        max_ = min_ = root.val
        if root.left:
            s_d, s_max, s_min = self.maxDiffH(root.left)
            maxDiff = max(maxDiff, s_d)
            max_ = max(max_, s_max)
            min_ = min(min_, s_min)

        if root.right:
            s_d, s_max, s_min = self.maxDiffH(root.right)
            maxDiff = max(maxDiff, s_d)
            max_ = max(max_, s_max)
            min_ = min(min_, s_min)

        maxDiff = max(abs(max_ - root.val), abs(min_ - root.val), maxDiff)

        return maxDiff, max_, min_


a = TreeNode(3)
b = TreeNode(0)
c = TreeNode(2)
d = TreeNode(1)
d.right = c
c.right = b
b.left = a

s = Solution()
print(s.maxAncestorDiff(d))
