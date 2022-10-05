# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            temp = TreeNode(val)
            temp.left = root
            return temp
        dummy = root
        queue = deque([(root, 1)])
        while queue:
            size = len(queue)
            node, d = queue.popleft()
            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))
            if d == depth - 1:
                left, right = node.left, node.right
                tempLeft, tempRight = TreeNode(val), TreeNode(val)
                node.left, node.right = tempLeft, tempRight
                tempLeft.left, tempRight.right = left, right                
        return dummy
                
            
            
        