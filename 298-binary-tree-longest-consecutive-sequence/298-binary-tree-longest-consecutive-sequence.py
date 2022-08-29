# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0
        
        def dfs(parent, child, streak):
            if not parent or child.val == parent.val + 1:
                streak += 1
            elif parent.val != child.val + 1:
                streak = 1
            self.longest = max(self.longest, streak)
            if child.left:
                dfs(child, child.left, streak)
            if child.right:
                dfs(child, child.right, streak)
                
            
        dfs(None, root, 0)
        
        return self.longest
        