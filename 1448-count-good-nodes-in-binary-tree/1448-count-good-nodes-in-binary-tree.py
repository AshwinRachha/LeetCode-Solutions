# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        num_good = 0
        
        queue = deque([(root, float('-inf'))])
        
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good += 1
                max_so_far = node.val
            if node.right:
                queue.append((node.right, max_so_far))
            if node.left:
                queue.append((node.left, max_so_far))
        
        return num_good
                
        