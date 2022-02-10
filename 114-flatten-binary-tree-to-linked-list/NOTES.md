def flattenTree(self, node):
if not node:
return None
if not node.left and not node.right:
return node
leftTail = self.flattenTree(node.left)
rightTail = self.flattenTree(node.right)
if leftTail:
leftTail.right = node.right
node.right = node.left
node.left = None
return rightTail if rightTail else leftTail