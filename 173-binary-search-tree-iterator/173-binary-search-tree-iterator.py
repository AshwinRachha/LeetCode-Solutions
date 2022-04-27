# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root):
        self.s = []
        self.cur = root
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.cur is not None:
            self.s.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.s.pop()
        value = self.cur.val
        self.cur = self.cur.right
        return value
    
    def hasNext(self) -> bool:
        return len(self.s) > 0 or self.cur


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()