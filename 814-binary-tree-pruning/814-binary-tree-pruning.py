# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            
            if root is None:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
            
            return root.val or left or right
        
        return root if dfs(root) else None
        
        