# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, curr_sum):
            nonlocal count
            if not root:
                return
            curr_sum += root.val
            if curr_sum == targetSum:
                count += 1
            count += h[curr_sum - targetSum]
            h[curr_sum] += 1
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            h[curr_sum] -= 1
            
        count = 0
        h = defaultdict(int)
        dfs(root, 0)
        return count
            