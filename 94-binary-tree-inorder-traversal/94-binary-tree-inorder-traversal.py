# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        ans = []
        while stack:
            while root:
                root = root.left
                stack.append(root)
            if stack:
                root = stack.pop()
                if root:
                    ans.append(root.val)
                    root = root.right
                    stack.append(root)
        
        return ans