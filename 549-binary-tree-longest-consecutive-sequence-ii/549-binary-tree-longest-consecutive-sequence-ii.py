# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root):
            if not root:
                return 0, 0
            incr, decr = 1, 1
            left_i, left_d = dfs(root.left)
            right_i, right_d = dfs(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    incr = left_i + 1
                if root.left.val == root.val - 1:
                    decr = left_d + 1
            if root.right:
                if root.right.val == root.val + 1:
                    incr = max(incr, 1 + right_i)
                if root.right.val == root.val - 1:
                    decr = max(decr, 1 + right_d)
            self.longest = max(self.longest, incr + decr - 1)
            return incr, decr
        dfs(root)        
        return self.longest
        