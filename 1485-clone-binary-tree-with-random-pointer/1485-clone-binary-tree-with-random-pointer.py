# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        nodeArr = {}
    
        def dfs(root):
            if not root: return None
            if root in nodeArr: return nodeArr[root]
            nRoot = NodeCopy(root.val)
            nodeArr[root] = nRoot
            nRoot.left = dfs(root.left)
            nRoot.right = dfs(root.right)
            nRoot.random = dfs(root.random)
            return nRoot

        return dfs(root)