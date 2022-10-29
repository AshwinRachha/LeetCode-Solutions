# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        def dfs1(node):
            if not node:
                return
            copyMap[node] = NodeCopy(node.val)
            dfs1(node.left)
            dfs1(node.right)
            return node
        def dfs2(root):
            if not root:
                return
            if root.left:
                    copyMap[root].left = copyMap[root.left]
            if root.right:
                copyMap[root].right = copyMap[root.right]
            if root.random:
                copyMap[root].random = copyMap[root.random]
                    
            dfs2(root.left)
            dfs2(root.right)
            return root
        copyMap = {}
        dfs1(root)
        dfs2(root)
        return copyMap[root]
        