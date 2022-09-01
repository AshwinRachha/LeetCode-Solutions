# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root, parent, curr_value):
            if root:
                if parent:
                    if root.val == parent.val + 1:
                        curr_value += 1
                    else:
                        curr_value = 1
            self.longest = max(self.longest, curr_value)
            if root.left:
                dfs(root.left, root, curr_value)
            if root.right:
                dfs(root.right, root, curr_value)
        
        dfs(root, None, 1)
        return self.longest
                            
        
        