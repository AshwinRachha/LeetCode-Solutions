# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        stack, ans = [root], []
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return ans