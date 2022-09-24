# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        def dfs(root, path, currSum):
            if root:
                path.append(root.val)
                currSum += root.val
                if not root.right and not root.left and currSum == targetSum:
                    output.append(path[:])
                if root.left:
                    dfs(root.left, path, currSum)
                if root.right:
                    dfs(root.right, path, currSum)
                path.pop()
                currSum -= root.val
        dfs(root, [], 0)
        return output