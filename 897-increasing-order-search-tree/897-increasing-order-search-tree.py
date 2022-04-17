# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, arr):
        if root:
            self.dfs(root.left, arr)
            arr.append(root.val)
            self.dfs(root.right, arr)
        return arr
    
    def make_tree(self, arr, index):
        node = None
        if index < len(arr):
            node = TreeNode(arr[index])
            node.left = None
            node.right = self.make_tree(arr, index + 1)
        return node
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        arr = self.dfs(root, [])
        return self.make_tree(arr, 0)
    
        