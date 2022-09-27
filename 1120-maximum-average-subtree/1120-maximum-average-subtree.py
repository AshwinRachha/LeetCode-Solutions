# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        self.max_avg = 0
        def dfs(root, count):
            if not root:
                return [0, 0.0]
            else:
                count_left, left = dfs(root.left, count)
                count_right, right = dfs(root.right, count)
                s = root.val + left + right
                c = count_left + count_right + 1
                avg = s / c
                self.max_avg = max(self.max_avg, avg)
                return [c, s]
        dfs(root, 1)
        return self.max_avg
        