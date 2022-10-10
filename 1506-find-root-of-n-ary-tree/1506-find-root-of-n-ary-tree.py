"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        hashMap = {}
        @lru_cache(maxsize = None)
        def dfs(node):
            if node:
                val = node.val
                if val not in hashMap:
                    hashMap[val] = [0, node]
                for child in node.children:
                    hashMap[child.val] = [1, child]
                    dfs(child)
        for node in tree:
            if node.val not in hashMap:
                dfs(node)
        for key, val in hashMap.items():
            if val[0] == 0:
                return val[1]