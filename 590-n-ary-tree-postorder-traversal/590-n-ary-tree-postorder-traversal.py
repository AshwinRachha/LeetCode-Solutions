"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def rec(root):
            if root:
                for c in root.children:
                    rec(c)
                out.append(root.val)

        out = []
        rec(root)
        return out
        