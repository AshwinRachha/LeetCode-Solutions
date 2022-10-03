# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dic = {}
        max_width = 0
        def dfs(node, row, col):
            nonlocal max_width
            if not node:
                return
            if row not in dic:
                dic[row] = col
            max_width = max(max_width, col - dic[row] + 1)
            dfs(node.left, row + 1, 2 * col)
            dfs(node.right, row + 1, 2 * col + 1)
        dfs(root, 0, 0)
        return max_width
            
            