# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):    
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = dic[val]
            root.right = build_tree(index + 1, right)
            root.left = build_tree(left, index - 1)
            return root
        
        dic = {n : i for i, n in enumerate(inorder)}
        return build_tree(0, len(inorder)-1)