class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        #soltion 2 LCA
        def getLCA(root,p,q):
            if not root: return None
            if root.val==p or root.val==q:
                return root
            L=getLCA(root.left,p,q)
            R=getLCA(root.right,p,q)
            if L and R:
                return root
            return L or R
    
            
        
        LCA=getLCA(root,startValue,destValue)
        ps,pd="",""
        stack = [(LCA, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
                
        return "U"*len(ps) + pd