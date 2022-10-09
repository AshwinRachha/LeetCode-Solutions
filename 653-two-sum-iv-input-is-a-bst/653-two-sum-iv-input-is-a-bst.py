# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        dic = {}
        
        def dfs(root):
            nonlocal dic
            if not root:
                return False
            else:
                val = root.val
                if k - val in dic:
                    return True
                dic[val] = k-val
                return dfs(root.left) or dfs(root.right)
        return dfs(root)