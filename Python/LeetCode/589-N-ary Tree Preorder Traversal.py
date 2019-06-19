from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if root.children:
            return [root.val] + sum([self.preorder(child) for child in root.children], [])
        else:
            return [root.val]
