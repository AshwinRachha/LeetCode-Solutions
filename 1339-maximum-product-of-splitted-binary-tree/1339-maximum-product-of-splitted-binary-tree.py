# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs1(root):
            nonlocal s
            if root:
                s += root.val
                dfs1(root.left)
                dfs1(root.right)
        dfs1(root)
        ans = 0
        
        def dfs2(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs2(root.left)
            right = dfs2(root.right)
            subtree_sum = root.val + left + right
            ans = max(ans, (s-subtree_sum) * subtree_sum)
            return subtree_sum
        dfs2(root)
        return ans % (10**9 + 7)