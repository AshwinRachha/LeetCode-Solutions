# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        dic = {}
        
        def dfs(root):
            if not root:
                return None
            if root in dic:
                return dic[root]
            node = NodeCopy(root.val)
            dic[root] = node
            node.left = dfs(root.left)
            node.right = dfs(root.right)
            node.random = dfs(root.random)
            return node
        
        return dfs(root)