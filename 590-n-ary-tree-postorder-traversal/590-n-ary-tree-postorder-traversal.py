"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]
        