"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def __init__(self):
        self.cheat = None
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        self.cheat = root
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        return self.cheat

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))