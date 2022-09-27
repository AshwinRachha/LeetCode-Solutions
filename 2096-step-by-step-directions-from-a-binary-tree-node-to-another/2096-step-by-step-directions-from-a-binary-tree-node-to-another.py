class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def getLCA(root, startValue, destValue):
            if not root:
                return None
            if root.val == startValue or root.val == destValue:
                return root
            left = getLCA(root.left, startValue, destValue)
            right = getLCA(root.right, startValue, destValue)
            
            if left and right:
                return root
            if left and not right:
                return left
            else:
                return right
            
        node = getLCA(root, startValue,destValue)
        stack = [(node, "")]
        ps, pd = "", ""
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd