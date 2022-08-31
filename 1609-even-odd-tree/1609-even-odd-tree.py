# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        prev = None
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev:
                        if prev.val >= node.val:
                            return False
                    prev = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.val % 2 != 0:
                        return False
                    if prev:
                        if prev.val <= node.val:
                            return False
                    prev = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            level += 1
            prev = None
        return True
        