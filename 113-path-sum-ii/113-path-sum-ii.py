# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, currentPath, currentSum):
            if root:
                currentSum += root.val
                currentPath.append(root.val)
                if not root.left and not root.right and currentSum == targetSum:
                    ans.append(currentPath[:])
                if root.left:
                    dfs(root.left, currentPath, currentSum)
                if root.right:
                    dfs(root.right, currentPath, currentSum)
                currentPath.pop()
        dfs(root, [], 0)         
        return ans
        
        