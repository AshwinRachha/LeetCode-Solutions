# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 0)])
        width = 0
        while queue:
            size = len(queue)
            _, level_head_index = queue[0]
            for _ in range(size):
                node, index = queue.popleft()
                if node.left:
                    queue.append([node.left, 2*index])
                if node.right:
                    queue.append([node.right, 2*index + 1])
                    
            width = max(width, index - level_head_index + 1)
        return width
        
        