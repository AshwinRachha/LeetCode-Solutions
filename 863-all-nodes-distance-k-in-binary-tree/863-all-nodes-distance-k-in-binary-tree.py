# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, par):
            if root:
                root.par = par
                if root.left:
                    dfs(root.left, root)
                if root.right:
                    dfs(root.right, root)
        dfs(root, None)
        queue = deque([(target, 0)])
        seen = set()
        seen.add(target)
        ans = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                ans.append(node.val)
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist + 1))
                    
        return ans