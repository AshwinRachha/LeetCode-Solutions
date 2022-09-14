# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.start = None
        def dfs(root, par = None):
            if root:
                if root.val == start:
                    self.start = root
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root)
        seen = {start}
        queue = deque([(self.start, 0)])
        while queue:
            root, distance = queue.popleft()
            for nei in (root.left, root.right, root.par):
                if nei and nei.val not in seen:
                    seen.add(nei.val)
                    queue.append((nei, distance + 1))
        return distance