# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, Counter())
        return self.count
    
    def dfs(self,root, counter):
        if not root.left and not root.right:
            counter[root.val] += 1
            self.count += self.checkPalindrome(counter)
            counter[root.val] -= 1
        else:
            counter[root.val] += 1
            if root.left:
                self.dfs(root.left, counter)
            if root.right:
                self.dfs(root.right, counter)
            counter[root.val] -= 1
    
    def checkPalindrome(self, counter):
        found = False
        for k, v in counter.items():
            if v % 2 != 0 and found:
                return False
            elif v % 2 !=0:
                found = True
        return True
        
        
        