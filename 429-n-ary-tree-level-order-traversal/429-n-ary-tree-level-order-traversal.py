"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        
        while queue:
            
            size = len(queue)
            ans.append([])
            for _ in range(size):
                
                node = queue.popleft()
                ans[-1].append(node.val)
                for c in node.children:
                    queue.append(c)
                
        
        return ans
        