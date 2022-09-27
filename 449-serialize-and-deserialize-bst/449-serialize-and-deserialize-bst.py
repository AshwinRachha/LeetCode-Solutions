# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans