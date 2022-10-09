# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        stack, s = [], set()
        while stack or root1:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            s.add(target - root1.val)
            root1 = root1.right
        
        while stack or root2:
            while root2:
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            if root2.val in s:
                return True
            root2 = root2.right
        
        return False
        