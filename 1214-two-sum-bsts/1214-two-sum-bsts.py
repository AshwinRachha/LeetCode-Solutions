# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        dic = {}
        def dfs1(root):
            nonlocal dic
            if root:
                dic[root.val] = target - root.val
                if root.left:
                    dfs1(root.left)
                if root.right:
                    dfs1(root.right)
        dfs1(root1)
        
        def dfs2(root):
            if not root:
                return False
            else:
                val = root.val
                if target - val in dic:
                    return True
                return dfs2(root.left) or dfs2(root.right)
        return dfs2(root2)
        