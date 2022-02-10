# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flattenTree(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            left = flattenTree(root.left)
            right = flattenTree(root.right)
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            return right if right else left
        
        flattenTree(root)
            
