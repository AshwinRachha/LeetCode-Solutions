# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root, curr_number):
            if not root:
                return
            else:
                curr_number = (curr_number << 1) | root.val
                if not root.left and not root.right:
                     self.sum += curr_number
                dfs(root.left, curr_number)
                dfs(root.right, curr_number)            
        dfs(root, 0)
        return self.sum