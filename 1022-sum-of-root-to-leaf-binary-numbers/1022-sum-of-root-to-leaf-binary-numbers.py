# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root, bin_string):
            if not root:
                return
            else:
                bin_string.append(str(root.val))
                if not root.left and not root.right:
                     self.sum += int("".join(bin_string), 2)
                if root.left:
                    dfs(root.left, bin_string)
                if root.right:
                    dfs(root.right, bin_string)
                bin_string.pop()
                    
        dfs(root, [])
        return self.sum