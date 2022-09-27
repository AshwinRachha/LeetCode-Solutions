# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        def dfs(root):
            if not root:
                return [0, 0]
            else:
                nLeft, sumLeft = dfs(root.left)
                nRight, sumRight = dfs(root.right)
                count = nLeft + nRight + 1
                summation = sumLeft + sumRight + root.val
                avg = summation // count
                #print(summation, avg, count, float(root.val))
                if avg == root.val:
                    self.count += 1
                return [count, summation]
        dfs(root)   
        return self.count
                
            