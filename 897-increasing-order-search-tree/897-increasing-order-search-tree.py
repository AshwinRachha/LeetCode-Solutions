# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = head = TreeNode(None)
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.root.right = TreeNode(root.val)
            self.root = self.root.right
            dfs(root.right)
        dfs(root)
        return head.right