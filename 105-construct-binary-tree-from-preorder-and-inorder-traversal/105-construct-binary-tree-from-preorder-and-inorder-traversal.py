# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        dic = {}
        for i, n in enumerate(inorder):
            dic[n] = i
        index = 0
        def convert(left, right):
            nonlocal index
            if right < left:
                return None
            node = TreeNode(preorder[index])
            index += 1
            pivot = dic[node.val]
            node.left = convert(left, pivot-1)
            node.right = convert(pivot + 1, right)
            return node
        root = convert(0, len(preorder)-1)
        return root
        