"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ans = []
        def dfs(root):
            if root:
                ans.append(root.val)
                for c in root.children:
                    dfs(c)
        dfs(root)
        return ans
        