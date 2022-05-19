# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        s = 0
        h = float('-inf')
        
        def dfs(root, curr_height):
            nonlocal s, h;
            if root:
                if not root.left and not root.right:
                    if curr_height > h:
                        s = root.val
                        h = curr_height
                    elif curr_height == h:
                        s += root.val
                dfs(root.left, curr_height + 1)
                dfs(root.right, curr_height + 1)
                
        dfs(root, 0)
        
        return s
        