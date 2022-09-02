# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(root, p, q):
            if not root:
                return root
            if root.val == p or root.val == q:
                return root
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            
            if left and right:
                return root
            return left or right
        
        def find(root, node):
            if root == None:
                return -1
            distance = -1
            if root.val == node:
                return distance + 1
            else:
                distance = find(root.left, node)
                if distance >= 0:
                    return distance + 1
                else:
                    distance = find(root.right, node)
                    if distance >= 0:
                        return distance + 1
            return distance
                
       
        
        root1 = lca(root, p, q)
        print(root1.val)
        
        dist1 = find(root1, p)
        dist2 = find(root1, q)
        
        return dist1 + dist2
            