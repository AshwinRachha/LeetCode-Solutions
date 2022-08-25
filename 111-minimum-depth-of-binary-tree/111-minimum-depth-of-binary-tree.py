# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_height = float('inf')
        if not root:
            return 0
        def dfs(node, height):
            if node:
                if not node.left and not node.right:
                    self.min_height = min(self.min_height, height + 1)
                dfs(node.left, height + 1)
                dfs(node.right, height + 1)
        dfs(root, 0)
        return self.min_height
        