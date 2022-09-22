class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        if not root:
            return self.res
        if not self.isLeaf(root):
            self.res.append(root.val)
        
        t = root.left
        while t:
            if not self.isLeaf(t):
                self.res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        self.addLeaves(root)
        
        stack = []
        
        t = root.right
        while t:
            if not self.isLeaf(t):
                stack.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while stack:
            self.res.append(stack.pop())
        
        return self.res
        
    def isLeaf(self, root):
        return root.left == None and root.right == None
    
    def addLeaves(self, root):
        if self.isLeaf(root):
            self.res.append(root.val)
        else:
            if root.left:
                self.addLeaves(root.left)
            if root.right:
                self.addLeaves(root.right)
    
    